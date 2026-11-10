"""Sanity check v2.1.
Uso:
  python scripts/run_sanity.py --stage ac
  python scripts/run_sanity.py --stage both data/planck/
"""
import sys, os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import argparse
import numpy as np
from src.synthetic import generate_lcdm, generate_dsi
from src.protocol import run_protocol


def check_a(n=50):
    k = np.logspace(-3.0, -0.5, 300)
    P0 = np.ones_like(k)
    cov = np.eye(len(k)) * (0.01 ** 2)
    lam_true = 1.62
    recovered = []
    for i in range(n):
        d = generate_dsi(k, P0, cov, eps=0.05, ln_lambda=np.log(lam_true), seed=i)
        r = run_protocol(k, d, cov=cov, seed=i)
        if r['certified']:
            recovered.append(r['stage2']['lambda_hat'])
    if not recovered:
        print("(a) FAIL: no recoveries")
        return False
    med = float(np.median(recovered))
    err = abs(med - lam_true) / lam_true
    print(f"(a) lambda_median={med:.4f} (true={lam_true}) rel_err={err:.4%} n={len(recovered)}/{n}")
    return err < 0.005


def check_c(n=200):
    k = np.logspace(-3.0, -0.5, 300)
    P0 = np.ones_like(k)
    cov = np.eye(len(k)) * (0.01 ** 2)
    fp = 0
    for i in range(n):
        d = generate_lcdm(k, P0, cov, seed=1000 + i)
        r = run_protocol(k, d, cov=cov, seed=1000 + i)
        if r['certified']:
            fp += 1
    rate = fp / n
    print(f"(c) false_positive_rate={rate:.2%}")
    return rate <= 0.01


def check_b(data_dir):
    try:
        from src.data_loader import load_planck_tt
        ell, Dl, cov = load_planck_tt(data_dir, binning='binned')
    except FileNotFoundError as e:
        print(f"(b) SKIPPED: {e}")
        return None
    u = np.log(ell)
    baseline = np.polyval(np.polyfit(u, Dl, 3), u)
    r = run_protocol(ell, Dl - baseline, cov=cov, seed=42)
    print(f"(b) planck_certified={r['certified']} gates={r['stage3']}")
    return not r['certified']


if __name__ == '__main__':
    ap = argparse.ArgumentParser()
    ap.add_argument('--stage', default='ac', choices=['ac', 'both'])
    ap.add_argument('--n-a', type=int, default=50)
    ap.add_argument('--n-c', type=int, default=200)
    ap.add_argument('data_dir', nargs='?', default='data/planck/')
    args = ap.parse_args()

    a = check_a(n=args.n_a)
    c = check_c(n=args.n_c)
    if args.stage == 'both':
        b = check_b(args.data_dir)
    else:
        b = None
        print("(b) SKIPPED (stage=ac)")

    print()
    ok = a and c and (b is not False)
    if ok and b is None:
        print("OK SANITY PASSED (parcial: a e c). Falta (b) antes do Stage B.")
    elif ok:
        print("OK SANITY PASSED (completo). Stage B liberado.")
    else:
        print(f"FAIL SANITY FAILED: a={a} b={b} c={c}")

