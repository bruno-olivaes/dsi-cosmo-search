import numpy as np

def gaussian_loglike(model, data, cov):
    residual = data - model
    L = np.linalg.cholesky(cov)
    alpha = np.linalg.solve(L, residual)
    logdet = 2.0 * np.sum(np.log(np.diag(L)))
    n = len(data)
    return -0.5 * (alpha @ alpha + logdet + n * np.log(2.0 * np.pi))

