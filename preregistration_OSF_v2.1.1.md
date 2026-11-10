# OSF Pre-Registration Form (v2.1.1)

## Metadata Overview
- **Registration Type:** Open-Ended Registration
- **Title:** Pre-registration: A certified, radix-agnostic search for Discrete Scale Invariance in the CMB and LSS
- **Primary Investigator:** Bruno Luçardo Olivaes (Independent Researcher, Brazil; ORCID: 0009-0003-8857-7945)
- **License:** MIT Open-Source License
- **Repository:** https://github.com/bruno-olivaes/dsi-cosmo-search
- **Data File Hash (SHA-256):** `ed2b8b51b033e668e661f6cf4eb7705f15bcaf358189dfc4a4481cc7020130cd`
- **Official Random Seed:** `507719` (drawn cryptographically via Python `secrets.randbelow`)

---

## 1. Study Information

### Description & Theoretical Hypothesis
Discrete Scale Invariance (DSI) posits that continuous scale invariance in cosmological perturbations is broken to a discrete scaling group characterized by a fundamental ratio $\lambda > 1$. The cosmological observable signature is a log-periodic oscillatory modulation superposed onto the primordial perturbation spectrum:
$$P(k) = P_0(k) \left[ 1 + \varepsilon \cos\left( \frac{2\pi}{\ln\lambda} \ln\frac{k}{k_0} + \phi \right) \right]$$
where $\varepsilon$ is the modulation amplitude, $\omega = 2\pi/\ln\lambda$ is the angular log-frequency conjugate to $u = \ln(k/k_0)$, and $\phi$ is an arbitrary phase.

This study implements a pre-registered, radix-agnostic search protocol designed to test for the presence of DSI modulations without prior prejudice toward specific values of $\lambda$ (e.g., golden ratio, integer bases, etc.), while rigorously controlling the family-wise error rate and the Look-Elsewhere Effect (LEE).

---

## 2. Pre-Registered Observational Data

### Planck 2018 CMB Data
- **Dataset:** Official Planck 2018 Release 3 (PR3) binned TT angular power spectrum $D_\ell = \ell(\ell+1)C_\ell/2\pi$.
- **Source:** NASA/IPAC Infrared Science Archive (IRSA) official mirror:
  `https://irsa.ipac.caltech.edu/data/Planck/release_3/ancillary-data/cosmoparams/COM_PowerSpect_CMB-TT-binned_R3.01.txt`
- **Multipole Range:** $N = 215$ bins spanning $\ell \in [30, 2508]$.
- **Cryptographic Hash (SHA-256):**
  `ed2b8b51b033e668e661f6cf4eb7705f15bcaf358189dfc4a4481cc7020130cd`
- **Covariance:** Diagonal covariance constructed from the observational asymmetric error bars: $\sigma_\ell = \frac{1}{2}(\Delta D_\ell^- + \Delta D_\ell^+)$.

---

## 3. Analysis Plan & Sequential Three-Stage Protocol

The protocol is strictly algorithmic with zero manual tuning or post-selection parameters:

### Stage 1: Radix-Agnostic Spectral Detection
1. Compute residuals against the Planck best-fit baseline $\Lambda\mathrm{CDM}$ model: $y = D_\ell^{\mathrm{obs}} - D_\ell^{\Lambda\mathrm{CDM}}$.
2. Map multipoles to logarithmic wavenumber coordinates: $u = \ln(k/k_0)$, with pivot $k_0 = 0.05\,\mathrm{Mpc}^{-1}$.
3. Evaluate the heteroscedastic normalized Lomb-Scargle periodogram across the dense frequency continuum $\omega \in [0.04, 60.0]$ (corresponding to scale factors $\lambda \in [1.1, 148]$).
4. Identify the global maximum peak $(\hat\omega_{\mathrm{peak}}, P_{\mathrm{peak}})$.

### Stage 2: Non-Linear Parametric Refinement
1. Initialize a bounded non-linear least-squares fit (`curve_fit` with Trust Region Reflective algorithm) using the candidate frequency from Stage 1:
   $$f(u) = A \cos(\omega u + \phi)$$
2. Extract the refined parameters $(\hat A, \hat\omega, \hat\phi)$ and their parameter covariance matrix $\Sigma_{\theta}$.
3. Reconstruct the preferred scaling factor and propagate standard error via the analytical delta method:
   $$\hat\lambda = \exp\left( \frac{2\pi}{\hat\omega} \right), \quad \sigma_\lambda = \hat\lambda \frac{2\pi}{\hat\omega^2} \sigma_\omega$$

### Stage 3: Multi-Gate Integrity Certification
A candidate is certified as a genuine cosmological detection if and only if all five integrity gates evaluate to `True`:
1. **Gate 1 (Resolvability):** $\hat\omega \in [\omega_{\min}, \omega_{\max}]$ with Rayleigh margin $\Delta\omega \ge 2\pi / \Delta u_{\mathrm{span}}$.
2. **Gate 2 (Amplitude Significance):** Fitted amplitude must exceed twice the root-mean-square noise: $\hat A > 2.0 \times \mathrm{RMS}(y)$.
3. **Gate 3 (Precision Gate):** Fractional parameter uncertainty must satisfy $\sigma_\lambda / \hat\lambda < 0.20$.
4. **Gate 4 (Look-Elsewhere Corrected Significance):** The non-parametric empirical $p$-value from a bootstrap-of-maximum null distribution of $B = 1000$ phase-scrambled surrogate datasets must satisfy $p_{\mathrm{corrected}} < 0.05$.
5. **Gate 5 (Model Selection Criterion):** The difference in Bayesian Information Criterion against the base $\Lambda\mathrm{CDM}$ model must satisfy $\Delta\mathrm{BIC} = \mathrm{BIC}_{\mathrm{null}} - \mathrm{BIC}_{\mathrm{DSI}} > 10.0$ (Jeffreys' threshold for strong evidence).

---

## 4. Prior Calibration & Sanity Verification

Before unblinding the empirical Planck data, the pipeline achieved:
- **Sanity Check (a) — Signal Recovery:** Reconstructed $\hat\lambda = 1.6201$ for an injected weak DSI signal of $\lambda = 1.62$ ($\varepsilon = 0.05$) with a relative metrological error of $0.0085\%$.
- **Sanity Check (c) — False-Positive Control:** $0.00\%$ false positives across $N = 200$ pure Gaussian $\Lambda\mathrm{CDM}$ realizations ($0/200$), confirming zero noise mining.
- **Sanity Check (b) — Null Realization:** Confirmed null detection on public Planck 2018 PR3 data ($p = 0.976$, `certified: false`).

---

## 5. Execution & Data Provenance
- Execution script: `python scripts/run_planck.py --seed 507719`
- Outputs: `results_planck.json`
- Verification repository: https://github.com/bruno-olivaes/dsi-cosmo-search
