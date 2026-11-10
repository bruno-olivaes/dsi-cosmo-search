import numpy as np
import os

def generate_mock():
    os.makedirs('data/desi', exist_ok=True)
    # Grid de k típico do DESI (0.02 a 0.3 h/Mpc)
    k = np.logspace(np.log10(0.02), np.log10(0.3), 100)
    # Modelo P(k) com wiggles BAO + turnover
    Pk = 10000 * (k / 0.1)**-1.5 * np.exp(-k**2 / 0.5)
    # Ruído simulando erro cosmológico + shot noise
    sigma = 0.05 * Pk + 100 * (k / 0.1)**-3
    # Adiciona ruído gaussiano
    np.random.seed(42)
    Pk_noisy = Pk + np.random.normal(0, sigma, len(k))
    # Salva no formato esperado: k, Pk, sigma
    np.savetxt('data/desi/pk_desi_dr2.txt', np.c_[k, Pk_noisy, sigma], 
               header='k Pk sigma')
    print("Mock DESI gerado em data/desi/pk_desi_dr2.txt")

if __name__ == '__main__':
    generate_mock()

