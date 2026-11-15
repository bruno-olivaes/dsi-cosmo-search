import numpy as np
from src.protocol import run_protocol


def test_detects_and_certifies_injected_signal():
    rng = np.random.default_rng(1)
    k = np.logspace(-3, -0.5, 300)
    u = np.log(k)
    omega_true = 2.0 * np.pi / np.log(1.62)
    y = 0.05 * np.cos(omega_true * u + 0.3) + rng.normal(0.0, 0.01, size=len(k))
    cov = np.full(len(k), 0.01)
    r = run_protocol(k, y, cov=cov, seed=1)
    assert 'stage2' in r, f"stage2 ausente: {r}"
    assert abs(r['stage2']['lambda_hat'] - 1.62) / 1.62 < 0.05
    assert r['stage3']['gate_amplitude'] is True
    assert r['certified'] is True


def test_rejects_pure_gaussian_noise():
    rng = np.random.default_rng(2026)
    k = np.logspace(-3, -0.5, 300)
    y = rng.normal(0.0, 0.01, size=len(k))
    cov = np.full(len(k), 0.01)
    r = run_protocol(k, y, cov=cov, seed=2026)
    assert r['certified'] is False
    assert r['stage3']['delta_bic'] < 10.0
