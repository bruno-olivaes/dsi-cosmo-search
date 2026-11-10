# 🧭 MASTER PUBLICATION CHECKLIST: Rota Zenodo (DOIs) + Academia.edu (Visibilidade)

Guia central de submissão e publicação para o autor (**Bruno L. Olivaes**).  
Focado na estratégia ágil e independente: **DOIs Oficiais do CERN via Zenodo** + **Vitrine Acadêmica Global via Academia.edu**.

---

## 📊 1. Tabela Resumo do Portfólio dos 5 Artigos

| # | Artigo | Repositório GitHub | Arquivo PDF Compilado | Status Zenodo / Release | Vitrine Academia.edu |
| :-: | :--- | :--- | :--- | :---: | :---: |
| **1** | **Planck DSI** | [`bruno-olivaes/dsi-cosmo-search`](https://github.com/bruno-olivaes/dsi-cosmo-search) | [`manuscript/main.pdf`](file:///C:/Users/bruno/projects/dsi-cosmo-search/manuscript/main.pdf) | Release `v2.1.1` criada | Pronto p/ Upload |
| **2** | **Casimir AFM** | [`bruno-olivaes/casimir-afm-spectroscopy`](https://github.com/bruno-olivaes/casimir-afm-spectroscopy) | [`manuscript/main.pdf`](file:///C:/Users/bruno/casimir-afm-spectroscopy/manuscript/main.pdf) | Toggle pronto p/ `v1.0.0` | Pronto p/ Upload |
| **3** | **Euclid DE** | [`bruno-olivaes/oscillatory-dark-energy-euclid`](https://github.com/bruno-olivaes/oscillatory-dark-energy-euclid) | [`manuscript/main.pdf`](file:///C:/Users/bruno/projects/oscillatory-dark-energy-euclid/manuscript/main.pdf) | Toggle pronto p/ `v1.0.0` | Pronto p/ Upload |
| **4** | **Qiskit ZNE** | [`bruno-olivaes/qiskit-lombscargle-zne`](https://github.com/bruno-olivaes/qiskit-lombscargle-zne) | [`manuscript/main.pdf`](file:///C:/Users/bruno/projects/qiskit-lombscargle-zne/manuscript/main.pdf) | Toggle pronto p/ `v2.0.0` | Pronto p/ Upload |
| **5** | **PQC Wire** | [`bruno-olivaes/pqc-crypto-agility-benchmark`](https://github.com/bruno-olivaes/pqc-crypto-agility-benchmark) | [`manuscript/main.pdf`](file:///C:/Users/bruno/projects/pqc-crypto-agility-benchmark/manuscript/main.pdf) | Toggle pronto p/ `v1.0.0` | Pronto p/ Upload |

---

## 🏛️ 2. Como Obter os DOIs Oficiais no Zenodo (CERN)

O Zenodo (operado pelo CERN e apoiado pela União Europeia) emite DOIs permanentes (`10.5281/zenodo.XXXXXXX`) para softwares e artigos científicos sem exigir afiliação universitária ou cartas de endosso.

### Passo 1: Acesse as Configurações do GitHub no Zenodo
1. Acesse: **[https://zenodo.org/account/settings/github/](https://zenodo.org/account/settings/github/)**
2. Faça login com a sua conta do GitHub (`bruno-olivaes`).

### Passo 2: Sincronizar e Ativar os 5 Repositórios
1. No canto superior direito da página, clique no botão **"Sync now"**. O Zenodo atualizará sua lista de repositórios do GitHub.
2. Localize cada um dos 5 repositórios na lista e mude o botão de toggle de **OFF** para **ON** (Verde):
   - [ ] `bruno-olivaes/dsi-cosmo-search`
   - [ ] `bruno-olivaes/casimir-afm-spectroscopy`
   - [ ] `bruno-olivaes/oscillatory-dark-energy-euclid`
   - [ ] `bruno-olivaes/qiskit-lombscargle-zne`
   - [ ] `bruno-olivaes/pqc-crypto-agility-benchmark`

### Passo 3: Criar uma Release no GitHub para Disparar a Emissão do DOI
Assim que o toggle estiver em **ON**, qualquer release criada no GitHub é automaticamente capturada pelo Zenodo em questão de segundos, gerando o DOI.

Você pode criar as releases via terminal executando os seguintes comandos:
```powershell
# 1. Planck DSI (cria a tag v2.1.2 para sincronização com o Zenodo ativo)
cd C:\Users\bruno\projects\dsi-cosmo-search
gh release create v2.1.2 --title "v2.1.2 - Zenodo Archive Sync" --notes "Release to issue citable Zenodo DOI for Planck DSI pipeline."

# 2. Casimir AFM
cd C:\Users\bruno\casimir-afm-spectroscopy
gh release create v1.0.0 --title "v1.0.0 - Artifact-Resistant Spectral Analysis in Dynamic AFM Casimir Force Measurements" --notes "First official release to issue Zenodo DOI."

# 3. Euclid Forecast
cd C:\Users\bruno\projects\oscillatory-dark-energy-euclid
gh release create v1.0.0 --title "v1.0.0 - Forecasting Log-Oscillatory Dark Energy with ESA Euclid" --notes "First official release to issue Zenodo DOI."

# 4. Qiskit ZNE Benchmark
cd C:\Users\bruno\projects\qiskit-lombscargle-zne
gh release create v2.0.0 --title "v2.0.0 - When Harmonic ZNE Fails: A Comparative Benchmark of Error Mitigation on NISQ Devices" --notes "First official release to issue Zenodo DOI."

# 5. PQC Network Wire
cd C:\Users\bruno\projects\pqc-crypto-agility-benchmark
gh release create v1.0.0 --title "v1.0.0 - The Network Cost of Post-Quantum Cryptography: TCP Fragmentation in TLS 1.3 Handshakes" --notes "First official release to issue Zenodo DOI."
```

### Passo 4: Colar o Badge do DOI no README do GitHub
Assim que o DOI for emitido (aparecerá no painel do Zenodo, ex: `10.5281/zenodo.14889921`), copie o código do badge e cole no topo do `README.md` do repositório:
```markdown
[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.XXXXXXX.svg)](https://doi.org/10.5281/zenodo.XXXXXXX)
```

---

## 🌐 3. Vitrine Social Acadêmica: Publicação no Academia.edu

Com os PDFs compilados e os DOIs em mãos, publique os 5 artigos no **[Academia.edu](https://www.academia.edu/)** para atrair leitores, cientistas e parceiros de pesquisa.

Consulte o manual dedicado:
👉 [`INSTRUCOES_ACADEMIA_EDU.md`](file:///C:/Users/bruno/projects/dsi-cosmo-search/INSTRUCOES_ACADEMIA_EDU.md)

Para cada artigo, o guia fornece:
- O arquivo PDF pronto para upload.
- Título, autores e resumo em texto puro formatado para copiar e colar.
- Tags e áreas de pesquisa recomendadas para maximizar o alcance algorítmico do site.

---

## 📑 4. Passo a Passo OSF (Open Science Framework - Pré-Registro)

*Exclusivo para o **Paper 1 (DSI)**, blindando o resultado nulo contra viés de publicação e garantindo carimbo temporal irrefutável.*

1. Acesse: **[https://osf.io/](https://osf.io/)** e faça login.
2. Clique em **"Create new project"** com o título: `dsi-cosmo-search`.
3. No painel do projeto, clique na aba **"Registrations"** $\to$ **"New registration"**.
4. Selecione o formulário: **"Open-Ended Registration"**.
5. Abra o arquivo local:
   [`C:\Users\bruno\projects\dsi-cosmo-search\preregistration_OSF_v2.1.1.md`](file:///C:/Users/bruno/projects/dsi-cosmo-search/preregistration_OSF_v2.1.1.md)
6. Copie os blocos correspondentes e cole no formulário.
7. Finalize e torne o registro **Público Imediatamente** (sem embargo). Guarde o DOI/link do OSF.

---

## 📦 5. Pacotes Prontos para o Futuro (arXiv)
Caso obtenha no futuro o endosso institucional de um pesquisador da área (`astro-ph`, `quant-ph`, `physics.ins-det`, `cs.CR`), todos os pacotes `.zip` contendo os fontes LaTeX, bibliografias e figuras permanecem arquivados e prontos para submissão imediata:
- Paper 1: `C:\Users\bruno\projects\dsi-cosmo-search\arxiv_submission.zip`
- Paper 2: `C:\Users\bruno\casimir-afm-spectroscopy\arxiv_submission_casimir.zip`
- Paper 3: `C:\Users\bruno\projects\oscillatory-dark-energy-euclid\arxiv_submission_euclid.zip`
- Paper 4: `C:\Users\bruno\projects\qiskit-lombscargle-zne\arxiv_submission_qiskit.zip`
- Paper 5: `C:\Users\bruno\projects\pqc-crypto-agility-benchmark\arxiv_submission_pqc.zip`
