import numpy as np
from src.model import log_periodic_factor, model_null


def test_no_modulation_when_eps_zero():
    k = np.logspace(-3, -1, 100)
    assert np.allclose(log_periodic_factor(k, eps=0.0, ln_lambda=1.0, phi=0.0), 1.0)


def test_periodicity():
    ln_lambda = 1.0
    k1, k2 = 0.1, 0.1 * np.exp(ln_lambda)
    f1 = log_periodic_factor(k1, eps=0.1, ln_lambda=ln_lambda, phi=0.3)
    f2 = log_periodic_factor(k2, eps=0.1, ln_lambda=ln_lambda, phi=0.3)
    assert np.isclose(f1, f2, atol=1e-10)


def test_model_null_returns_P0():
    k = np.logspace(-3, -1, 50)
    P0 = np.ones_like(k)
    assert np.allclose(model_null(k, P0, A=1.0), P0)

