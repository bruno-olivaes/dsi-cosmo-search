import hashlib, json
from pathlib import Path
import numpy as np

def sha256_file(path):
    h = hashlib.sha256()
    with open(path, 'rb') as f:
        for chunk in iter(lambda: f.read(8192), b''):
            h.update(chunk)
    return h.hexdigest()

def verify_manifest(manifest_path, data_dir):
    with open(manifest_path) as f:
        manifest = json.load(f)
    if not manifest:
        print("Manifest vazio (esperado antes do Stage B).")
        return
    for fname, expected in manifest.items():
        fpath = Path(data_dir) / fname
        if not fpath.exists():
            raise FileNotFoundError(f"Missing: {fpath}")
        actual = sha256_file(fpath)
        if actual != expected:
            raise ValueError(f"Hash mismatch {fname}")
    print("All hashes verified.")

def load_planck_tt(data_dir, binning='binned'):
    """Carrega espectro TT binned e constrói covariância diagonal."""
    data_dir = Path(data_dir)
    spec = data_dir / f'COM_PowerSpect_CMB-TT-{binning}_R3.01.txt'
    if not spec.exists():
        raise FileNotFoundError(f"Dados do Planck ausentes em {data_dir}")
    # Formato: l, Dl, -dDl, +dDl, BestFit
    data = np.loadtxt(spec)
    ell = data[:, 0]
    Dl = data[:, 1]
    dDl_minus = data[:, 2]
    dDl_plus = data[:, 3]
    # Incerteza simétrica média
    sigma_l = 0.5 * (dDl_minus + dDl_plus)
    cov = np.diag(sigma_l ** 2)
    return ell, Dl, cov

