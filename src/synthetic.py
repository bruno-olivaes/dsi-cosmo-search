import numpy as np
from .model import model_null, model_dsi

def generate_realization(model_values, cov, seed):
    rng = np.random.default_rng(seed)
    L = np.linalg.cholesky(cov)
    return model_values + L @ rng.standard_normal(len(model_values))

def generate_lcdm(k, P0, cov, A=1.0, seed=42):
    return generate_realization(model_null(k, P0, A), cov, seed)

def generate_dsi(k, P0, cov, A=1.0, eps=0.05, ln_lambda=1.0, phi=0.0, seed=42):
    return generate_realization(model_dsi(k, P0, A, eps, ln_lambda, phi), cov, seed)

