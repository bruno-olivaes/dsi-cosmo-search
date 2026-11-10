"""Stage B (Replicação): análise do DESI DR2 P(k)."""
import sys, os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import argparse, json
import numpy as np
from src.protocol import run_protocol


def main(data_file, seed):
    data = np.loadtxt(data_file)
    k, Pk = data[:, 0], data[:, 1]
    u = np.log(k)
    baseline = np.polyval(np.polyfit(u, Pk, 3), u)
    r = run_protocol(k, Pk - baseline, cov=None, seed=seed)
    out = {'seed': seed, 'result': r}
    with open('results_desi.json', 'w') as f:
        json.dump(out, f, indent=2, default=float)
    print(json.dumps(out, indent=2, default=float))


if __name__ == '__main__':
    ap = argparse.ArgumentParser()
    ap.add_argument('data_file', nargs='?', default='data/desi/pk_desi_dr2.txt')
    ap.add_argument('--seed', type=int, required=True)
    args = ap.parse_args()
    main(args.data_file, args.seed)

