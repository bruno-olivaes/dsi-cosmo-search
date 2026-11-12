# 📬 JOURNAL SUBMISSION KIT: Professional Cover Letters

This document provides ready-to-submit, formal cover letters for the four high-impact papers in the portfolio, tailored to their respective target peer-reviewed journals.

Author: **Bruno Luçardo Olivaes**  
Affiliation: **Independent Researcher, Brazil**  
Email: **brunoolivaes@gmail.com**  
ORCID: **[0009-0003-8857-7945](https://orcid.org/0009-0003-8857-7945)**  

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
3. The most prominent spectral candidate (hat{lambda} = 4.12 +/- 0.31) fails the amplitude and look-elsewhere gates, yielding a post-trial significance of p_corrected = 0.975, consistent with Gaussian cosmic variance.
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
ORCID: 0009-0003-8857-7945
Repository: https://github.com/bruno-olivaes/dsi-cosmo-search
Zenodo DOI: 10.5281/zenodo.24121677
```

---

## 2. Paper 2: Review of Scientific Instruments (RSI)

- **Target Journal:** *Review of Scientific Instruments* (AIP Publishing)
- **Manuscript Title:** *Statistical Pitfalls in Casimir Force Spectroscopy: Eliminating False-Positive Periodic Signals in Sub-Micron AFM Metrology*
- **Subject Category:** Nanotechnology, Precision Metrology, Surface Force Instrumentation, Statistical Signal Processing

```text
Dear Editor of Review of Scientific Instruments,

We submit for your consideration the manuscript entitled "Statistical Pitfalls in Casimir Force Spectroscopy: Eliminating False-Positive Periodic Signals in Sub-Micron AFM Metrology" as an original research article in Review of Scientific Instruments.

Precision measurements of quantum vacuum phenomena—such as the Casimir effect, Casimir-Polder interactions, and non-Newtonian gravity searches—rely on atomic force microscopy (AFM) and Kelvin probe force microscopy (KPFM) operating at separation distances below 1 micrometer. In recent literature, several experimental groups have reported anomalous oscillatory residuals in force-distance curves, attributing them to exotic quantum corrections or discrete scale invariance.

In this paper, we conduct a systematic metrological audit demonstrating that such oscillatory residuals can be purely instrumental and mathematical artifacts induced by:
1. High-order polynomial detrending suffering from the Runge phenomenon near boundary domains.
2. Natural cubic spline interpolations producing synthetic log-periodic phase undulations under non-uniform spatial sampling.
3. Uncompensated electrostatic patch potentials in Kelvin probe measurements.

We establish a rigorous, gate-certified data-processing protocol that replaces unconstrained spline and polynomial subtractions with adaptive low-order Chebyshev baselines and Generalized Lomb-Scargle periodograms coupled to Fisher-information matrices. Beyond demonstrating how polynomial detrending induces Runge boundary oscillations against $z^{-4}$ tails and how cubic splines attenuate sub-micron signals by 57%, we provide an explicit first-order Taylor expansion proof showing that experimental contact-point calibration offsets ($\delta z_0$) generate a spurious $-4 C_4 \delta z_0 z^{-5}$ term that is analytically absorbed by our physically motivated $\{1, z^{-4}, z^{-5}\}$ baseline. We submit this manuscript under the standard subscription track (zero APC).

We benchmark this protocol on synthetic and experimental AFM force curves, demonstrating 100% rejection of spurious periodicities while preserving genuine sub-picoNewton physical modulations.

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
ORCID: 0009-0003-8857-7945
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
1. On 1- and 2-qubit circuits dominated by single-mode drive crosstalk, Harmonic ZNE outperforms standard polynomial extrapolation, reducing state estimation error by up to 34%.
2. Crucially, as circuit depth and entangling layers scale to 4 qubits, multi-qubit spectator crosstalk and stochastic depolarizing noise severely wash out coherent error phases. Under these conditions, unconstrained harmonic extrapolation undergoes spectral overfitting, leading to worse ground-state fidelity estimates than unmitigated observables.
3. In contrast, Randomized Compiling (Pauli Twirling) successfully diagonalizes the noise channel into a stochastic Pauli channel, consistently outperforming harmonic extrapolation in multi-qubit regimes.

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
ORCID: 0009-0003-8857-7945
Repository: https://github.com/bruno-olivaes/qiskit-lombscargle-zne
Zenodo DOI: 10.5281/zenodo.24121693
```

---

## 4. Paper 7: Physical Review D (PRD)

- **Target Journal:** *Physical Review D* (Particles, Fields, Gravitation, and Cosmology - American Physical Society)
- **Manuscript Title:** *Breaking the Zeptouniverse Sensitivity Barrier: Neural Simulation-Based Inference for Certified Discrete Scale Invariance Searches at the LHC*
- **Subject Category:** Particle Physics, High-Energy Experiment and Phenomenological Analysis, Machine Learning in HEP

```text
Dear Editors of Physical Review D,

We submit our manuscript entitled "Breaking the Zeptouniverse Sensitivity Barrier: Neural Simulation-Based Inference for Certified Discrete Scale Invariance Searches at the LHC" for consideration as a regular research article in Physical Review D.

Searches for physics beyond the Standard Model at distance scales below 10^-18 m (the zeptouniverse) are increasingly limited not by collision luminosity, but by systematic statistical dilution in histogram-level analyses. When searching for subtle, continuous spectral phenomena—such as log-periodic Discrete Scale Invariance (DSI) predicted by conformal hidden sectors or quantum gravity limit cycles—traditional binned Generalized Lomb-Scargle periodograms discretize continuous invariant mass coordinates, destroying phase coherence and diluting the Fisher information metric. Consequently, classical binned searches can only constrain modulations with large signal amplitudes (epsilon > 0.30 - 0.50).

In this paper, we demonstrate that unbinned continuous profile likelihood inference breaks this sensitivity barrier. Crucially, rather than relying on an opaque black-box classifier, our architecture formulates an explicit Unbinned Continuous Profile Likelihood normalized at every parameter step via 64-node Gauss-Legendre numerical quadrature over 62,214 CMS dimuon events. By eliminating the $\Delta u^2 / 12$ intra-bin Fisher information dilution inherent to binned Lomb-Scargle periodograms (documented in our companion baseline study, Zenodo DOI: 10.5281/zenodo.24149840), the method achieves a $9.5\times$ empirical improvement in 95% CL upper-limit sensitivity ($\varepsilon_{95} \le 0.0580$ vs. $0.5520$) while strictly preserving false-positive immunity:
1. We construct a continuous likelihood ratio estimator p(m_mumu | theta_DSI, theta_SM) calibrated on CERN Open Data dimuon events from CMS Run 2010B.
2. The continuous likelihood leverages exact numerical quadrature partition functions to enable unbinned profile likelihood evaluations q(epsilon) = -2 Delta ln L without histogram binning loss.
3. In a head-to-head benchmark on identical Drell-Yan continuum collisions (m in [11, 75] GeV), the unbinned approach improves the 95% CL upper limit from epsilon_95^trad <= 0.5520 down to epsilon_95^unbinned <= 0.0580—achieving a certified 9.5x sensitivity enhancement without requiring additional beam time.
4. Integrated into our audited five-gate certification engine, the unbinned likelihood yields a decisive Bayesian Information Criterion penalty (Delta-BIC = -23.21), preventing false-positive discoveries.

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
ORCID: 0009-0003-8857-7945
Repository: https://github.com/bruno-olivaes/lhc-nsbi-dsi
Zenodo DOI: 10.5281/zenodo.24149842
```

