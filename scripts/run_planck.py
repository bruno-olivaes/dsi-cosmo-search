"""Stage B: análise do Planck 2018. Rodar UMA vez com semente registrada."""
import sys, os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import argparse, json
import numpy as np
from src.data_loader import verify_manifest, load_planck_tt
from src.protocol import run_protocol


def main(data_dir, seed):
    verify_manifest('data_manifest.json', data_dir)
    ell, Dl, cov = load_planck_tt(data_dir, binning='binned')
    u = np.log(ell)
    baseline = np.polyval(np.polyfit(u, Dl, 3), u)
    r = run_protocol(ell, Dl - baseline, cov=cov, seed=seed)
    out = {'seed': seed, 'result': r}
    with open('results_planck.json', 'w') as f:
        json.dump(out, f, indent=2, default=float)
    print(json.dumps(out, indent=2, default=float))


if __name__ == '__main__':
    ap = argparse.ArgumentParser()
    ap.add_argument('data_dir', nargs='?', default='data/planck/')
    ap.add_argument('--seed', type=int, required=True)
    args = ap.parse_args()
    main(args.data_dir, args.seed)

