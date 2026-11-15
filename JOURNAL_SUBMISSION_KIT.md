
# 📬 JOURNAL SUBMISSION KIT: Professional Cover Letters

This document provides ready-to-submit, formal cover letters for the four high-impact papers in the portfolio, tailored to their respective target peer-reviewed journals.

Author: **Bruno Luçardo Olivaes**  
Affiliation: **Independent Researcher, Brazil**  
Email: **brunoolivaes@gmail.com**  
ORCID: **[0009-0003-5351-446X](https://orcid.org/0009-0003-5351-446X)**  

---

## 1. Paper 1: Monthly Notices of the Royal Astronomical Society (MNRAS)

- **Target Journal:** *Monthly Notices of the Royal Astronomical Society* (Oxford University Press / RAS)
- **Manuscript Title:** *Constraints on Primordial Discrete Scale Invariance from the Planck 2018 Temperature Power Spectrum*
- **Subject Category:** Cosmology: cosmic microwave background, cosmological parameters, early Universe, methods: data analysis

```text
Dear Editor-in-Chief and Editorial Board of MNRAS,

Please find enclosed our manuscript entitled "Constraints on Primordial Discrete Scale Invariance from the Planck 2018 Temperature Power Spectrum", which we submit for consideration as an original research paper in the Monthly Notices of the Royal Astronomical Society.

Discrete Scale Invariance (DSI) and associated log-periodic oscillations in primordial cosmological perturbation spectra have garnered persistent theoretical interest as signatures of complex inflaton potentials, limit-cycle inflation, and non-trivial vacuum geometries. However, unconstrained grid searches in spectral analysis frequently fall prey to the look-elsewhere effect, trial factors, and post-selection bias.

In this work, we present the first fully pre-registered, radix-agnostic search for primordial DSI applied to the official Planck 2018 PR3 binned temperature power spectrum. To guarantee methodological immunity against noise-mining:
1. To ensure strict protection against post-hoc parameter tuning and the Look-Elsewhere Effect, the complete five-gate statistical pipeline and decision thresholds were locked prior to final data evaluation via an immutable, cryptographically verifiable Git tag (`v2.1.2`) permanently archived on CERN/Zenodo (DOI: 10.5281/zenodo.24121677), coupled with SHA-256 integrity verification of the official NASA/IPAC Planck PR3 bandpowers.
2. The empirical significance of candidate modes is evaluated against a non-parametric ensemble of 1,000 phase-scrambled surrogate datasets.
3. The most prominent residual candidate relative to the official Planck BestFit baseline (hat{lambda} = 1.2938 +/- 0.0072) fails the amplitude, look-elsewhere, and information-criterion gates, yielding a post-trial significance of p_corrected = 0.998 and Delta-BIC = -49.80, consistent with Gaussian cosmic variance.
4. We establish certified 95% CL upper limits on the primordial modulation amplitude (epsilon < 0.05) across a wide scaling factor domain lambda in [1.1, 148].
5. We replicate the protocol on synthetic Large-Scale Structure mock spectra matching the baseline precision of the Dark Energy Spectroscopic Instrument (DESI) DR2, confirming identical null behavior.

All code, data checksum manifests, pre-registered protocols (v2.1.2), and verification pipelines are open-source and permanently archived. Given MNRAS's dedication to observational cosmology, rigorous statistical methodologies, and reproducible science, we believe this manuscript will be of high interest to your readership.

This manuscript is original, has not been published elsewhere, and is not currently under consideration by any other journal. All authors approve of this submission.

Suggested Reviewers:
- Prof. Licia Verde (ICREA / University of Barcelona) - Expertise in CMB statistics, cosmological parameter estimation, and large-scale structure.
- Prof. David Spergel (Simons Foundation / Princeton University) - Expertise in CMB data analysis and cosmological model testing.
- Prof. Hiranya Peiris (University of Cambridge / UCL) - Expertise in inflationary signatures, primordial features, and non-standard CMB spectra.

Sincerely,

Bruno Luçardo Olivaes
Independent Researcher, Brazil
Email: brunoolivaes@gmail.com
ORCID: 0009-0003-5351-446X
Repository: https://github.com/bruno-olivaes/dsi-cosmo-search
Zenodo DOI: 10.5281/zenodo.24121677
```

---

## 2. Paper 2: Review of Scientific Instruments (RSI)

- **Target Journal:** *Review of Scientific Instruments* (AIP Publishing)
- **Manuscript Title:** *Spectral Analysis of Systematic Residuals in Casimir Force Measurements: Lossless Vector Re-Audit, Statistical Pitfalls, and KPFM Patch-Potential Metrology*
- **Subject Category:** Nanotechnology, Precision Metrology, Surface Force Instrumentation, Statistical Signal Processing

```text
Dear Editor of Review of Scientific Instruments,

We submit for your consideration the manuscript entitled "Spectral Analysis of Systematic Residuals in Casimir Force Measurements: Lossless Vector Re-Audit, Statistical Pitfalls, and KPFM Patch-Potential Metrology" as an original research article in Review of Scientific Instruments.

Precision measurements of quantum vacuum phenomena—such as the Casimir effect, Casimir-Polder interactions, and non-Newtonian gravity searches—rely on atomic force microscopy (AFM) and Kelvin probe force microscopy (KPFM) operating at separation distances below 1 micrometer. In recent literature, several experimental groups have reported anomalous oscillatory residuals in force-distance curves, attributing them to exotic quantum corrections or discrete scale invariance.

In this paper, we conduct a systematic metrological audit demonstrating that such oscillatory residuals can be purely instrumental and mathematical artifacts induced by:
1. High-order polynomial detrending suffering from the Runge phenomenon near boundary domains.
2. Natural cubic spline interpolations producing synthetic log-periodic phase undulations under non-uniform spatial sampling.
3. Uncompensated electrostatic patch potentials in Kelvin probe measurements.

We establish a rigorous, gate-certified data-processing protocol that replaces unconstrained spline and polynomial subtractions with a physically motivated {1, z^-4, z^-5} inverse-power baseline and direct heteroscedastic Generalized Lomb-Scargle periodograms (Baluev FAP = 0.163; chi^2/dof = 1.14), supplemented by first-principles Speake-Trenner integration of 2D KPFM patch maps (P proportional to d^-2.29). Beyond demonstrating how polynomial detrending induces Runge boundary oscillations against $z^{-4}$ tails and how cubic splines attenuate short-wavelength ($\lambda = 7.5$ nm) signal variance by 22.6% across the full irregular scan (degrading the 90% Minimum Detectable Level by $2.27\times$), we provide an explicit first-order Taylor expansion proof showing that experimental contact-point calibration offsets ($\delta z_0$) generate a spurious $-4 C_4 \delta z_0 z^{-5}$ term that is analytically absorbed by our physical $\{1, z^{-4}, z^{-5}\}$ baseline. We submit this manuscript under the standard subscription track (zero APC).

We benchmark this protocol on lossless vector-extracted residuals of Decca et al. (PRL 91, 050402, 2003; N = 497 pressure and N = 288 force residuals) and raw 2D KPFM data from de Jong et al. (Nat. Phys. 2025), demonstrating complete elimination of spurious Runge/Gaussian-threshold artifacts while preserving an empirical sensitivity of MDL_90 = 0.54 sigma_F.

Given RSI's leadership in physical instrumentation, experimental metrology, and the identification of experimental systematic errors, this work provides timely, actionable guidance for laboratories conducting precision surface-force measurements worldwide.

The manuscript represents original work, is not concurrently under review elsewhere, and has been approved by the author.

Suggested Reviewers:
- Prof. Ricardo Decca (Indiana University - Purdue University Indianapolis) - Leading experimentalist in Casimir force measurements and precision AFM metrology.
- Prof. Umar Mohideen (University of California, Riverside) - Pioneer in experimental Casimir force precision measurements using AFM.
- Dr. Jeremy Munday (University of California, Davis) - Specialist in Casimir-Lifshitz force instrumentation and nanoscale surface metrology.

Sincerely,

Bruno Luçardo Olivaes
Independent Researcher, Brazil
Email: brunoolivaes@gmail.com
ORCID: 0009-0003-5351-446X
Repository: https://github.com/bruno-olivaes/casimir-afm-spectroscopy
Zenodo DOI: 10.5281/zenodo.24121687
```

---

## 3. Paper 4: Quantum Science and Technology (QST)

- **Target Journal:** *Quantum Science and Technology* (IOP Publishing)
- **Manuscript Title:** *When Harmonic ZNE Fails: A Comparative Benchmark of Error Mitigation on Superconducting NISQ Processors*
- **Subject Category:** Quantum Information & Computation, Quantum Error Mitigation, Superconducting Qubit Hardware

```text
Dear Editor and Editorial Board of Quantum Science and Technology,

Please find enclosed our manuscript entitled "When Harmonic ZNE Fails: A Comparative Benchmark of Error Mitigation on Superconducting NISQ Processors", submitted for publication in Quantum Science and Technology.

Quantum Error Mitigation (QEM) is vital for achieving quantum utility on Noisy Intermediate-Scale Quantum (NISQ) hardware prior to fault-tolerant quantum error correction. Zero-Noise Extrapolation (ZNE) via unitary pulse stretching or digital gate folding is widely employed. Recently, harmonic and spectral extrapolation models have been proposed to capture coherent oscillatory error phases that escape standard polynomial or exponential fits.

In this work, we conduct an extensive, reproducible benchmark comparing Harmonic ZNE (utilizing Generalized Lomb-Scargle spectral decoupling) against standard Polynomial/Exponential ZNE and Randomized Compiling (Pauli Twirling) across 1 to 4 superconducting transmon qubits using calibrated heavy-hex noise models and Qiskit pulse stretching emulations.

To rigorously isolate algorithmic failure modes from time-dependent hardware calibration drift (such as transient $T_1/T_2$ fluctuations and readout instability), our benchmark employs controlled, high-fidelity Qiskit 2.x (`AerSimulator`) emulations parameterized by realistic superconducting heavy-hex transmon noise models under a strict shot budget ($N_{\mathrm{total}} = 24,000$). This controlled ablation architecture allows us to identify the exact multi-qubit spectator crosstalk threshold at which spectral/harmonic ZNE breaks down when Pauli Twirling is omitted.

Our findings reveal critical operational boundaries for quantum practitioners:
1. On a 1-qubit coherent Ramsey echo sequence probed across deep noise scales ($\lambda \le 17$), Harmonic ZNE outperforms standard polynomial extrapolation, reducing Mean Absolute Error (MAE) by 85.4%.
2. Crucially, in entangled 4-qubit TFIM Trotter circuits, non-commuting coherent $ZZ$ spectator crosstalk and multi-mode interference cause harmonic ZNE to fail catastrophically (MAE surges to 2.28 at $\epsilon = 0.04$ rad vs. 0.148 unmitigated), performing significantly worse than unmitigated observables.
3. In contrast, Randomized Compiling (Pauli Twirling) converts coherent crosstalk into stochastic Pauli channels, enabling standard linear and exponential ZNE to achieve robust error reductions of 80.8%–81.0% under identical shot budgets.

We provide a diagnostic decision tree and open-source Qiskit-compatible modules allowing researchers to determine a priori whether their circuit-noise topology qualifies for harmonic ZNE.

Given QST's focus on quantum computing engineering and benchmark methodologies, this work directly addresses key open questions in practical NISQ error mitigation. The manuscript is original and not under review elsewhere.

Suggested Reviewers:
- Dr. Ryan LaRose (Michigan State University / Mitiq Lead) - Co-author of Mitiq and specialist in Zero-Noise Extrapolation protocols.
- Dr. Vincent Russo (IBM Quantum) - Expert in quantum error mitigation, randomized compiling, and superconducting circuit benchmarking.
- Prof. Simon Benjamin (University of Oxford) - Pioneer in quantum error mitigation theory and practical hardware verification.

Sincerely,

Bruno Luçardo Olivaes
Independent Researcher, Brazil
Email: brunoolivaes@gmail.com
ORCID: 0009-0003-5351-446X
Repository: https://github.com/bruno-olivaes/qiskit-lombscargle-zne
Zenodo DOI: 10.5281/zenodo.24121693
```

---

## 4. Paper 7: Physical Review D (PRD)

- **Target Journal:** *Physical Review D* (Particles, Fields, Gravitation, and Cosmology - American Physical Society)
- **Manuscript Title:** *Breaking the Binning Attenuation Barrier: Unbinned Composite Quadrature Likelihood and Neural Simulation-Based Inference for Certified DSI Searches at the LHC*
- **Subject Category:** Particle Physics, High-Energy Experiment and Phenomenological Analysis, Machine Learning in HEP

```text
Dear Editors of Physical Review D,

We submit our manuscript entitled "Breaking the Binning Attenuation Barrier: Unbinned Composite Quadrature Likelihood and Neural Simulation-Based Inference for Certified DSI Searches at the LHC" for consideration as a regular research article in Physical Review D.

Searches for physics beyond the Standard Model at sub-femtometer scales are increasingly limited not by collision luminosity, but by systematic statistical dilution in histogram-level analyses. When searching for subtle, continuous high-frequency spectral phenomena—such as log-periodic Discrete Scale Invariance (DSI) predicted by conformal hidden sectors or quantum gravity limit cycles—traditional binned analyses discretize continuous invariant mass coordinates, destroying phase coherence via intra-bin $\mathrm{sinc}(\omega \Delta u / 2\pi)$ destructive interference ($\omega^2 \Delta u^2 / 12$ Fisher information loss) as $\omega \Delta u$ approaches Nyquist zeros.

In this paper, we demonstrate that unbinned continuous profile likelihood inference breaks this binning attenuation barrier. Crucially, rather than relying on an opaque black-box classifier, our architecture formulates an explicit Unbinned Continuous Profile Likelihood normalized at every parameter step via composite $4\times 64$-node Gauss-Legendre numerical quadrature ($256$ nodes) over all $N = 17,458$ clean Drell-Yan opposite-sign dimuon events ($m \in [11, 75]$ GeV, isolated from 62,214 total CMS Run 2010B dimuons), cross-validated by a zero-anchored PyTorch Fourier-conditioned Neural Simulation-Based Inference ratio estimator (`ConditionalDensityMLP`). Explicitly accounting for the empirical CMS barrel mass resolution measured directly from the $J/\psi$ resonance ($\sigma_u^{\mathrm{barrel}} = 0.0120$, $73.1\%$ signal survival at $\lambda = 1.10$):
1. We separate the slow-modulation equivalence regime ($\lambda \ge 1.50$, where unbinned and 40–60-bin Poisson likelihoods match within $1\text{--}5\%$) from the high-frequency binning collapse regime ($\lambda \in [1.05, 1.25]$, $\omega \in [28.16, 128.78]$ rad).
2. At $\lambda = 1.10$ ($\omega = 65.92$ rad), the unbinned Composite-GL likelihood achieves a 95% CL upper limit of $\varepsilon_{95} = 0.0337$ ($\varepsilon_{95}^{\mathrm{neural}} = 0.0324$), outperforming 20-bin ($0.9800$, $29.1\times$ loss), 40-bin ($0.1924$, $5.7\times$ loss), and 60-bin ($0.0512$, $1.52\times$ loss) Poisson searches documented relative to our companion baseline study (Zenodo DOI: 10.5281/zenodo.24149840).
3. Integrated into our audited five-gate certification engine, the unbinned likelihood yields a decisive Bayesian Information Criterion penalty ($\Delta\mathrm{BIC} = -18.15$, $p_{\mathrm{corrected}} = 0.4500$ at $\lambda = 1.10$), preventing false-positive discoveries across all tested scales.

This work bridges advanced continuous likelihood estimation with rigorous experimental metrology in collider physics. Because PRD is the premier venue for high-energy physics phenomenology, collider search methodology, and statistical methods in HEP, we believe this manuscript will be of broad interest to your readership.

The manuscript has not been published previously and is not under consideration elsewhere.

Suggested Reviewers:
- Prof. Kyle Cranmer (Data Science Institute / University of Wisconsin-Madison) - Pioneer of Simulation-Based Inference and machine learning in LHC particle physics.
- Prof. Jesse Thaler (MIT / IAIFI) - Specialist in collider phenomenology, jet substructure, and foundational machine learning methods in particle physics.
- Dr. Johann Brehmer (Qualcomm AI Research / formerly NYU/CERN) - Leading researcher in neural likelihood ratio estimation and EFT bounds at the LHC.

Sincerely,

Bruno Luçardo Olivaes
Independent Researcher, Brazil
Email: brunoolivaes@gmail.com
ORCID: 0009-0003-5351-446X
Repository: https://github.com/bruno-olivaes/lhc-nsbi-dsi
Zenodo DOI: 10.5281/zenodo.24149842
```

