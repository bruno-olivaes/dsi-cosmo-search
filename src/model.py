import numpy as np

K0_PIVOT = 0.05

def log_periodic_factor(k, eps, ln_lambda, phi, k0=K0_PIVOT):
    omega = 2.0 * np.pi / ln_lambda
    return 1.0 + eps * np.cos(omega * np.log(k / k0) + phi)

def model_null(k, P0, A):
    return A * P0

def model_dsi(k, P0, A, eps, ln_lambda, phi):
    return A * P0 * log_periodic_factor(k, eps, ln_lambda, phi)

