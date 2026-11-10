# dsi-cosmo-search: Pre-Registered Search for Discrete Scale Invariance in Cosmological Spectra

[![Release](https://img.shields.io/github/v/release/bruno-olivaes/dsi-cosmo-search?color=blue)](https://github.com/bruno-olivaes/dsi-cosmo-search/releases/tag/v2.1.1)
[![Paper PDF](https://img.shields.io/badge/Paper-PDF_Manuscript-red.svg)](manuscript/main.pdf)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python: 3.12](https://img.shields.io/badge/Python-3.12+-green.svg)](https://www.python.org/)
[![Planck 2018 PR3](https://img.shields.io/badge/Data-Planck%202018%20PR3-orange.svg)](https://irsa.ipac.caltech.edu/data/Planck/release_3/)
[![Pre-Registration](https://img.shields.io/badge/Pre--Registration-OSF%20v2.1.1-purple.svg)](https://osf.io/)

Open-source scientific pipeline implementing a certified, radix-agnostic, three-stage statistical estimation protocol to search for **Discrete Scale Invariance (DSI)** in cosmological perturbation spectra.

Includes full validation benchmarks, false-positive protection against noise mining, official Stage B execution on the **Planck 2018 PR3** temperature power spectrum, mock replication for the **DESI DR2** matter power spectrum, and complete LaTeX manuscript sources.

---

## 🌌 Summary of Scientific Findings

| Dataset | Candidate Mode | Preferred Ratio $\hat\lambda$ | Empirical Significance ($p_{\mathrm{corrected}}$) | Gate Status | Verdict |
| :--- | :---: | :---: | :---: | :---: | :---: |
| **Synthetic DSI ($\varepsilon = 0.05$)** | $\omega = 13.018$ | $\hat\lambda = 1.6201$ (True: $1.62$) | $p < 0.05$ | All 5 Gates \textsc{Passed} | **Recovered** (0.0085% error) |
| **$\Lambda\mathrm{CDM}$ Noise ($N = 200$)** | Any mode | N/A | $p > 0.05$ | Failed Gates 2, 4, 5 | **Zero False Positives** (0.00%) |
| **Planck 2018 PR3 TT Binned** | $\hat\omega = 4.4371$ | $\hat\lambda = 4.1208 \pm 0.3092$ | $p_{\mathrm{corrected}} = 0.975$ | Failed Gates 2, 4, 5 | **Null Confirmed** ($\varepsilon_{95\%} < 0.05$) |
| **DESI DR2 Replication Mock** | $\hat\omega = 4.0759$ | $\hat\lambda = 4.6718 \pm 0.4187$ | $p_{\mathrm{corrected}} = 0.314$ | Failed Gates 2, 4, 5 | **Null Confirmed** |

* **Zero Look-Elsewhere Fallacy:** Peak significance is corrected using a non-parametric bootstrap-of-maximum phase-scrambled surrogate ensemble ($B = 1000$ iterations).
* **Metrological Precision:** High-precision recovery ($\Delta\lambda / \lambda < 0.01\%$) on synthetic calibration without post-selection bias.

---

## 🔒 Data Provenance & Integrity

The official Planck 2018 binned TT power spectrum is hashed and verified against our pre-registered manifest:
- **File:** `data/planck/COM_PowerSpect_CMB-TT-binned_R3.01.txt`
- **Official Source:** [NASA/IPAC IRSA Planck PR3 Mirror](https://irsa.ipac.caltech.edu/data/Planck/release_3/ancillary-data/cosmoparams/COM_PowerSpect_CMB-TT-binned_R3.01.txt)
- **SHA-256 Digest:** `ed2b8b51b033e668e661f6cf4eb7705f15bcaf358189dfc4a4481cc7020130cd`
- **Cryptographic Blind Seed:** `507719`

---

## 🛠️ Quickstart & Reproduction

### 1. Installation
Clone the repository and install the standard scientific Python environment:
```bash
git clone https://github.com/bruno-olivaes/dsi-cosmo-search.git
cd dsi-cosmo-search
pip install numpy scipy astropy dynesty matplotlib pytest
```

### 2. Unit Tests
Execute the automated test suite:
```bash
pytest tests/ -v
# 4 passed in ~7s
```

### 3. Sanity & Calibration Checks
```bash
# Fast check (10 signal recoveries, 20 noise realizations, Planck check b)
python scripts/run_sanity.py --stage both --n-a 10 --n-c 20

# Full calibration check
python scripts/run_sanity.py --stage both --n-a 50 --n-c 200
```

### 4. Official Stage B Execution (Planck 2018)
```bash
python scripts/run_planck.py --seed 507719
```
Outputs are written to `results_planck.json`.

### 5. Mock DESI Replication
```bash
python scripts/generate_desi_mock.py
python scripts/run_desi.py --seed 507719
```
Outputs are written to `results_desi.json`.

### 6. Compile the Scientific Manuscript
```bash
cd manuscript
pdflatex main.tex
pdflatex main.tex
# Produces main.pdf (4 pages, two-column format)
```

---

## 📁 Repository Architecture

```
dsi-cosmo-search/
├── data/
│   ├── planck/
│   │   └── COM_PowerSpect_CMB-TT-binned_R3.01.txt   # Planck 2018 PR3 binned TT data
│   └── desi/
│       └── pk_desi_dr2.txt                          # DESI DR2 replication mock
├── manuscript/
│   ├── main.tex                                     # LaTeX paper with Appendix A & B
│   └── main.pdf                                     # Compiled 4-page PDF manuscript
├── preregistration/
│   └── protocol_v2.1.md                             # Pre-registered protocol specification
├── scripts/
│   ├── create_manifest.py                           # SHA-256 manifest builder
│   ├── generate_desi_mock.py                        # DESI mock generator
│   ├── run_sanity.py                                # Pre-flight calibration suite
│   ├── run_planck.py                                # Stage B execution on Planck 2018
│   └── run_desi.py                                  # Stage B execution on DESI mock
├── src/
│   ├── data_loader.py                               # Heteroscedastic CMB & LSS data ingestion
│   ├── likelihood.py                                # Gaussian log-likelihood & Cholesky solver
│   ├── model.py                                     # DSI log-periodic modulation formulations
│   ├── protocol.py                                  # 3-Stage estimation & 5 integrity gates
│   └── synthetic.py                                 # Synthetic realization generator
├── tests/
│   ├── test_model.py                                # Physics & periodicity unit tests
│   └── test_protocol.py                             # Signal recovery unit tests
├── arxiv_submission/
│   ├── 00README.txt                                 # arXiv compilation guide
│   ├── main.tex                                     # Source LaTeX document
│   └── main.pdf                                     # Pre-compiled article
├── arxiv_submission.zip                             # Ready-to-upload arXiv archive
├── data_manifest.json                               # Cryptographic data hashes
├── environment.yml                                  # Conda environment definition
├── results_planck.json                              # Stage B Planck results
└── results_desi.json                                # Stage B DESI mock results
```

---

## 📜 Citation & License

If you use this protocol or code in your research, please cite:
```bibtex
@article{olivaes2026dsi,
  title={Constraints on Primordial Discrete Scale Invariance from the Planck 2018 Temperature Power Spectrum},
  author={Olivaes, Bruno Lucardo},
  journal={arXiv preprint},
  year={2026},
  url={https://github.com/bruno-olivaes/dsi-cosmo-search}
}
```

Licensed under the [MIT License](LICENSE).
