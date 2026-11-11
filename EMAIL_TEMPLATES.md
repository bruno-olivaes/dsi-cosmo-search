# 📧 EMAIL TEMPLATES: Outreach & Academic Collaboration

Modelos formais e objetivos de e-mail prontos para envio a pesquisadores e equipes de engenharia. Substitua os campos entre colchetes `[ ... ]` antes de enviar.

---

## 1. Para Autores do Experimento CMS / LHC (CERN)

**Destinatário:** Pesquisadores de grupos de análise de dimuons / BSM do CMS ou LHCb (ex: contatos listados nos artigos de Run 2/Run 3 de dimuons no CERN CDS / arXiv).  
**Assunto:** Unbinned Neural Likelihood (NSBI) for invariant mass resonance & scale invariance searches in CMS dimuons

```text
Dear Dr. [Author's Last Name] and CMS Dimuon Analysis Colleagues,

I hope this message finds you well.

I am writing to share two recent open-source studies where we adapted pre-registered metrological protocols and Neural Simulation-Based Inference (NSBI) to public CMS collision data:

1. "A Certified Search for Discrete Scale Invariance in LHC Dimuon Mass Spectra" 
   (Preprint & Code: https://github.com/bruno-olivaes/lhc-dsi-search)
   We audited 62,214 physical mu+ mu- events from CMS Run 2010B using a 5-gate protocol, establishing certified null results (p = 0.324 in the clean Drell-Yan continuum) and constraining spurious log-periodic artifacts.

2. "Breaking the Zeptouniverse Sensitivity Barrier: Neural Simulation-Based Inference for Certified DSI Searches at the LHC"
   (Preprint & Code: https://github.com/bruno-olivaes/lhc-nsbi-dsi)
   By training an unbinned conditional neural likelihood ratio estimator q_psi(m_mumu | theta) with continuous Gauss-Legendre quadrature normalization, we observed an empirical 9.5x sensitivity enhancement (deepening the 95% CL upper limit from epsilon <= 0.552 to epsilon <= 0.0580) over binned Lomb-Scargle techniques, while maintaining strict Delta-BIC false-alarm protection.

Given your leadership in precision dimuon physics and resonance searches, I would be delighted to discuss whether this unbinned neural likelihood framework could be of interest or utility for full-luminosity CMS Run 2 or Run 3 datasets.

All data loaders, PyTorch models, and benchmark notebooks are fully reproducible and open-source.

Thank you very much for your time and consideration.

Best regards,

Bruno Luçardo Olivaes
Independent Researcher, Brazil
Email: brunoolivaes@gmail.com
ORCID: 0009-0003-8857-7945
Portfolio Master DOI: 10.5281/zenodo.24124702
```

---

## 2. Para a Equipe de Engenharia do Qiskit (IBM Quantum)

**Destinatário:** Mantenedores do Qiskit / Mitiq / IBM Quantum Community (`qiskit@ibm.com` ou canais do Slack/GitHub do Qiskit).  
**Assunto:** Open-source benchmark of Harmonic ZNE vs Pauli Twirling across 1-4 qubits on IBM Quantum hardware

```text
Dear Qiskit Development and Quantum Error Mitigation Team,

I hope you are doing well.

I am reaching out to share the results of our empirical benchmark on Quantum Error Mitigation (QEM) models implemented with Qiskit 2.x and executed on IBM Quantum transmon architectures:

"When Harmonic ZNE Fails: A Comparative Benchmark of Error Mitigation on Superconducting NISQ Processors"
- Paper & Zenodo DOI: https://doi.org/10.5281/zenodo.24121693
- Repository & Notebooks: https://github.com/bruno-olivaes/qiskit-lombscargle-zne

Key Benchmark Findings:
1. In 1- and 2-qubit circuits dominated by single-mode drive crosstalk, Harmonic Zero-Noise Extrapolation (HZNE via Lomb-Scargle spectral decoupling) outperforms standard polynomial fits, yielding up to a 34% reduction in state estimation error.
2. At 4 qubits, multi-qubit spectator crosstalk and stochastic depolarizing noise wash out coherent phases. Under these conditions, unconstrained harmonic extrapolation suffers from spectral overfitting, whereas Randomized Compiling (Pauli Twirling) consistently preserves physical fidelity.

We have structured the codebase with a clear diagnostic decision tree and modular classes compatible with Qiskit Runtime Primitives (`EstimatorV2`). If there is interest from the Qiskit or Mitiq teams, I would be delighted to contribute these diagnostic modules or benchmark tutorials upstream to the community ecosystem.

Thank you for your tireless work developing the Qiskit platform.

Best regards,

Bruno Luçardo Olivaes
Independent Researcher, Brazil
Email: brunoolivaes@gmail.com
ORCID: 0009-0003-8857-7945
GitHub: https://github.com/bruno-olivaes
```

---

## 3. Pedido Formal de Endosso para o arXiv (astro-ph / quant-ph / hep-ex)

**Destinatário:** Pesquisador doutor/professor com status de endorser ativo no arXiv na categoria alvo (`astro-ph.CO`, `quant-ph` ou `hep-ex`).  
**Assunto:** Request for arXiv endorsement in [astro-ph.CO / quant-ph / hep-ex] - Bruno L. Olivaes

```text
Dear Professor [Professor's Last Name],

I hope this email finds you well.

I am an independent researcher in Brazil working on certified statistical methods, cosmological data analysis, and quantum metrology. I have closely followed your influential contributions to [mention a specific paper or area of the professor, e.g., CMB cosmological data analysis / quantum error mitigation].

I am preparing to submit our pre-registered manuscript to the arXiv under the category [astro-ph.CO / quant-ph / hep-ex], and as an independent author, the arXiv submission portal requires an initial endorsement from an established researcher in the field.

The manuscript details:
- Title: "Constraints on Primordial Discrete Scale Invariance from the Planck 2018 Temperature Power Spectrum" [or another paper title]
- Pre-Registration (OSF): Open-source, certified 3-stage protocol with 5 integrity gates.
- Dataset: Official Planck 2018 PR3 binned TT power spectrum (NASA/IPAC).
- Primary Result: Certified null result (p_corrected = 0.975; epsilon_95 < 0.05) using non-parametric phase-scrambled bootstrap surrogates to prevent look-elsewhere bias.
- Full PDF & Source Code: Permanently archived with official CERN/Zenodo DOI:
  https://doi.org/10.5281/zenodo.24121677
  GitHub: https://github.com/bruno-olivaes/dsi-cosmo-search

If you find that this work meets the scientific standards of the arXiv, I would be deeply grateful if you would consider endorsing my submission. 

My arXiv endorsement code is: [INSERT YOUR 6-DIGIT CODE FROM ARXIV HERE]
(Or directly via: https://arxiv.org/auth/endorse?x=[CODE])

I have attached the compiled PDF manuscript for your convenience. Please feel no obligation if your schedule does not permit it.

Thank you very much for your time, scholarship, and dedication to open science.

Sincerely,

Bruno Luçardo Olivaes
Independent Researcher, Brazil
Email: brunoolivaes@gmail.com
ORCID: 0009-0003-8857-7945
Unified Monograph DOI: 10.5281/zenodo.24124702
```
