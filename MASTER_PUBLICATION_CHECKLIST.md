# 🧭 MASTER PUBLICATION CHECKLIST: O Portfólio dos 5 Artigos Científicos

Guia central de submissão e publicação para o autor (**Bruno L. Olivaes**). Contém todos os caminhos locais dos pacotes compactados, repositórios GitHub, metadados exatos para o **arXiv**, instruções de emissão de DOI no **Zenodo**, e protocolo de pré-registro no **OSF**.

---

## 📊 1. Tabela Resumo do Portfólio

| # | Artigo | Repositório GitHub | Pacote ZIP para o arXiv | Categoria arXiv | Cross-List | Status Zenodo / Release |
| :-: | :--- | :--- | :--- | :---: | :---: | :---: |
| **1** | **Planck DSI** | [`bruno-olivaes/dsi-cosmo-search`](https://github.com/bruno-olivaes/dsi-cosmo-search) | [`arxiv_submission.zip`](file:///C:/Users/bruno/projects/dsi-cosmo-search/arxiv_submission.zip) | `astro-ph.CO` | `gr-qc`, `stat.AP` | Release `v2.1.1` criada |
| **2** | **Casimir AFM** | [`bruno-olivaes/casimir-afm-spectroscopy`](https://github.com/bruno-olivaes/casimir-afm-spectroscopy) | [`arxiv_submission_casimir.zip`](file:///C:/Users/bruno/casimir-afm-spectroscopy/arxiv_submission_casimir.zip) | `physics.ins-det` | `quant-ph`, `physics.data-an` | Toggle pronto p/ `v1.0.0` |
| **3** | **Euclid DE** | [`bruno-olivaes/oscillatory-dark-energy-euclid`](https://github.com/bruno-olivaes/oscillatory-dark-energy-euclid) | [`arxiv_submission_euclid.zip`](file:///C:/Users/bruno/projects/oscillatory-dark-energy-euclid/arxiv_submission_euclid.zip) | `astro-ph.CO` | `gr-qc` | Toggle pronto p/ `v1.0.0` |
| **4** | **Qiskit ZNE** | [`bruno-olivaes/qiskit-lombscargle-zne`](https://github.com/bruno-olivaes/qiskit-lombscargle-zne) | [`arxiv_submission_qiskit.zip`](file:///C:/Users/bruno/projects/qiskit-lombscargle-zne/arxiv_submission_qiskit.zip) | `quant-ph` | `physics.comp-ph` | Toggle pronto p/ `v2.0.0` |
| **5** | **PQC Wire** | [`bruno-olivaes/pqc-crypto-agility-benchmark`](https://github.com/bruno-olivaes/pqc-crypto-agility-benchmark) | [`arxiv_submission_pqc.zip`](file:///C:/Users/bruno/projects/pqc-crypto-agility-benchmark/arxiv_submission_pqc.zip) | `cs.CR` | `cs.NI` | Toggle pronto p/ `v1.0.0` |

---

## 🏛️ 2. Passo a Passo Zenodo (Ativação dos DOIs)

Para cada um dos 5 repositórios, faça o onboarding no Zenodo para emissão automática do DOI de citação de software científico:

1. Acesse: **[https://zenodo.org/account/settings/github/](https://zenodo.org/account/settings/github/)**
2. Faça login com sua conta do GitHub (`bruno-olivaes`).
3. Clique no botão **"Sync now"** no canto superior direito.
4. Na lista de repositórios, mude a chavinha de **OFF** para **ON** (Verde) para os 5 projetos:
   - [ ] `bruno-olivaes/dsi-cosmo-search`
   - [ ] `bruno-olivaes/casimir-afm-spectroscopy`
   - [ ] `bruno-olivaes/oscillatory-dark-energy-euclid`
   - [ ] `bruno-olivaes/qiskit-lombscargle-zne`
   - [ ] `bruno-olivaes/pqc-crypto-agility-benchmark`
5. Dispare as releases oficiais via terminal (caso ainda não criadas) para gerar os DOIs:
   ```bash
   # Paper 1 (já possui v2.1.1, se necessário sincronizar crie v2.1.2)
   cd C:\Users\bruno\projects\dsi-cosmo-search && gh release create v2.1.2 --title "v2.1.2 - Zenodo Archive Sync" --notes "Automated Zenodo release"

   # Paper 2
   cd C:\Users\bruno\casimir-afm-spectroscopy && gh release create v1.0.0 --title "v1.0.0 - Artifact-Resistant Spectral Analysis in Dynamic AFM Casimir Force Measurements" --notes "First official release"

   # Paper 3
   cd C:\Users\bruno\projects\oscillatory-dark-energy-euclid && gh release create v1.0.0 --title "v1.0.0 - Forecasting Log-Oscillatory Dark Energy with ESA Euclid" --notes "First official release"

   # Paper 4
   cd C:\Users\bruno\projects\qiskit-lombscargle-zne && gh release create v2.0.0 --title "v2.0.0 - When Harmonic ZNE Fails: Comparative Benchmark on NISQ Devices" --notes "First official release"

   # Paper 5
   cd C:\Users\bruno\projects\pqc-crypto-agility-benchmark && gh release create v1.0.0 --title "v1.0.0 - Post-Quantum Cryptography Wire Overhead and TCP Fragmentation in TLS 1.3" --notes "First official release"
   ```

---

## 📑 3. Passo a Passo OSF (Open Science Framework - Pré-Registro)

*Exclusivo para o **Paper 1 (DSI)**, certificando o resultado nulo blindado contra viés de publicação.*

1. Acesse: **[https://osf.io/](https://osf.io/)** e faça login.
2. Clique em **"Create new project"** com o título: `dsi-cosmo-search`.
3. No painel do projeto, clique na aba **"Registrations"** $\to$ **"New registration"**.
4. Selecione o tipo de formulário: **"Open-Ended Registration"**.
5. Abra o arquivo local:
   [`C:\Users\bruno\projects\dsi-cosmo-search\preregistration_OSF_v2.1.1.md`](file:///C:/Users/bruno/projects/dsi-cosmo-search/preregistration_OSF_v2.1.1.md)
6. Copie os blocos correspondentes (Hipótese, Five Mandatory Integrity Gates, Métricas de Certificação $p_{\mathrm{corrected}} = 0.975$, $\Delta\mathrm{BIC} = \mathrm{NaN}$, e Reprodutibilidade) e cole no formulário.
7. Finalize e torne o registro **Público Imediatamente** (sem embargo). Guarde o DOI do OSF.

---

## 📬 4. Passo a Passo arXiv (Upload dos 5 Pacotes)

Acesse **[https://arxiv.org/submit](https://arxiv.org/submit)** e faça o envio de cada um dos 5 artigos:

### 📄 Paper 1: Cosmologia Observacional (Planck 2018 DSI)
- **Arquivo ZIP para upload:** [`C:\Users\bruno\projects\dsi-cosmo-search\arxiv_submission.zip`](file:///C:/Users/bruno/projects/dsi-cosmo-search/arxiv_submission.zip)
- **Metadados:** [`C:\Users\bruno\projects\dsi-cosmo-search\ARXIV_METADATA.txt`](file:///C:/Users/bruno/projects/dsi-cosmo-search/ARXIV_METADATA.txt)
- **Title:** Constraints on Primordial Discrete Scale Invariance from the Planck 2018 Temperature Power Spectrum
- **Authors:** Bruno L. Olivaes
- **Primary Category:** `astro-ph.CO` (Cosmology and Nongalactic Astrophysics)
- **Cross-list Categories:** `gr-qc`, `stat.AP`
- **Comments:** 4 pages, 1 table. Code and data provenance available at https://github.com/bruno-olivaes/dsi-cosmo-search

---

### 📄 Paper 2: Metrologia Experimental (Espectroscopia AFM Casimir)
- **Arquivo ZIP para upload:** [`C:\Users\bruno\casimir-afm-spectroscopy\arxiv_submission_casimir.zip`](file:///C:/Users/bruno/casimir-afm-spectroscopy/arxiv_submission_casimir.zip)
- **Metadados:** [`C:\Users\bruno\casimir-afm-spectroscopy\ARXIV_METADATA_CASIMIR.txt`](file:///C:/Users/bruno/casimir-afm-spectroscopy/ARXIV_METADATA_CASIMIR.txt)
- **Title:** Artifact-Resistant Spectral Analysis in Dynamic AFM Casimir Force Measurements
- **Authors:** Bruno L. Olivaes
- **Primary Category:** `physics.ins-det` (Instrumentation and Detectors)
- **Cross-list Categories:** `quant-ph`, `physics.data-an`
- **Comments:** 3 pages, 3 figures, 1 table. Code and reproducible dataset available at https://github.com/bruno-olivaes/casimir-afm-spectroscopy

---

### 📄 Paper 3: Energia Escura Dinâmica (Previsão ESA Euclid)
- **Arquivo ZIP para upload:** [`C:\Users\bruno\projects\oscillatory-dark-energy-euclid\arxiv_submission_euclid.zip`](file:///C:/Users/bruno/projects/oscillatory-dark-energy-euclid/arxiv_submission_euclid.zip)
- **Metadados:** [`C:\Users\bruno\projects\oscillatory-dark-energy-euclid\ARXIV_METADATA_EUCLID.txt`](file:///C:/Users/bruno/projects/oscillatory-dark-energy-euclid/ARXIV_METADATA_EUCLID.txt)
- **Title:** Forecasting Log-Oscillatory Dark Energy with ESA Euclid: Breaking the Degeneracy
- **Authors:** Bruno L. Olivaes
- **Primary Category:** `astro-ph.CO` (Cosmology and Nongalactic Astrophysics)
- **Cross-list Categories:** `gr-qc`
- **Comments:** 4 pages, 1 figure, 1 table. Code and data available at https://github.com/bruno-olivaes/oscillatory-dark-energy-euclid

---

### 📄 Paper 4: Computação Quântica NISQ (ZNE Harmônico vs Pauli Twirling)
- **Arquivo ZIP para upload:** [`C:\Users\bruno\projects\qiskit-lombscargle-zne\arxiv_submission_qiskit.zip`](file:///C:/Users/bruno/projects/qiskit-lombscargle-zne/arxiv_submission_qiskit.zip)
- **Metadados:** [`C:\Users\bruno\projects\qiskit-lombscargle-zne\ARXIV_METADATA_QISKIT.txt`](file:///C:/Users/bruno/projects/qiskit-lombscargle-zne/ARXIV_METADATA_QISKIT.txt)
- **Title:** When Harmonic ZNE Fails: A Comparative Benchmark of Error Mitigation on NISQ Devices
- **Authors:** Bruno L. Olivaes
- **Primary Category:** `quant-ph` (Quantum Physics)
- **Cross-list Categories:** `physics.comp-ph`
- **Comments:** 4 pages, 1 figure, 1 table. Code and data available at https://github.com/bruno-olivaes/qiskit-lombscargle-zne

---

### 📄 Paper 5: Criptografia Pós-Quântica (Overhead de Rede e TCP no TLS 1.3)
- **Arquivo ZIP para upload:** [`C:\Users\bruno\projects\pqc-crypto-agility-benchmark\arxiv_submission_pqc.zip`](file:///C:/Users/bruno/projects/pqc-crypto-agility-benchmark/arxiv_submission_pqc.zip)
- **Metadados:** [`C:\Users\bruno\projects\pqc-crypto-agility-benchmark\ARXIV_METADATA_PQC.txt`](file:///C:/Users/bruno/projects/pqc-crypto-agility-benchmark/ARXIV_METADATA_PQC.txt)
- **Title:** The Network Cost of Post-Quantum Cryptography: TCP Fragmentation in TLS 1.3 Handshakes
- **Authors:** Bruno L. Olivaes
- **Primary Category:** `cs.CR` (Cryptography and Security)
- **Cross-list Categories:** `cs.NI` (Networking and Internet Architecture)
- **Comments:** 3 pages, 1 figure, 1 table. Code available at https://github.com/bruno-olivaes/pqc-crypto-agility-benchmark
