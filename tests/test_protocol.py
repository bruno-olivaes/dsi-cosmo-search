import numpy as np
from src.protocol import run_protocol


def test_detects_injected_signal():
    k = np.logspace(-3, -0.5, 300)
    u = np.log(k)
    omega_true = 2.0 * np.pi / np.log(1.62)
    y = 0.05 * np.cos(omega_true * u + 0.3)
    r = run_protocol(k, y, cov=None, seed=1)
    assert 'stage2' in r, f"stage2 ausente: {r}"
    assert abs(r['stage2']['lambda_hat'] - 1.62) / 1.62 < 0.05

