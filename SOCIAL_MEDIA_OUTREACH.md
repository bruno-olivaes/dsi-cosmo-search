# 📢 SOCIAL MEDIA OUTREACH: Kit de Divulgação para Redes Sociais

Modelos de posts prontos para **LinkedIn** e **X (Twitter)** cobrindo todos os 8 trabalhos do portfólio científico (7 artigos + monografia master). Todos os links apontam para os DOIs oficiais permanentes do CERN/Zenodo e repositórios abertos.

---

## 🌟 Paper 7: Verossimilhança Não-Binada & NSBI no LHC (DESTAQUE MÁXIMO)

### 🐦 X (Twitter) [260 caracteres]
🚀 Até 29.1x mais sensibilidade no LHC vs. 20 bins (5.7x vs. 40 bins) em λ=1.10 sem aceleradores novos!
Aplicamos Verossimilhança Não-Binada (4×64 GL) + NSBI PyTorch nos Drell-Yan do CMS/CERN (ε₉₅ = 0.0337; ΔBIC = -18.15).
DOI: https://doi.org/10.5281/zenodo.24149842
#MachineLearning #Physics #LHC #CERN

### 💼 LinkedIn
🚀 **Quebrando a Barreira do Binning no LHC: Até 29,1x Mais Sensibilidade com Verossimilhança Não-Binada e NSBI**

Quando buscamos modulações log-periódicas finas em espectros do LHC, agrupar colisões em histogramas impõe atenuação analítica $\mathrm{sinc}(\omega \Delta u / 2\pi)$ — destruindo a coerência próxima aos zeros de Nyquist.

No Paper 7, combinamos uma **Verossimilhança de Perfil Contínua Não-Binada** (quadratura composta $4\times 64$ nós de Gauss-Legendre) com um estimador amortizado de **NSBI em PyTorch (`ConditionalDensityMLP`)**, aplicados sobre todos os $N = 17.458$ eventos limpos de Drell-Yan do CMS Run 2010B incorporando a resolução empírica do barril ($\sigma_u = 0,0120$; $73,1\%$ de sobrevivência em $\lambda = 1,10$):
🔹 **Ganho em Alta Frequência:** O limite a 95% CL atingiu $\varepsilon_{95} = 0,0337$ ($\varepsilon_{95}^{\text{neural}} = 0,0324$) em $\lambda = 1,10$, superando em **29,1x** a busca Poisson com 20 bins ($0,9800$) e em **5,7x** com 40 bins ($0,1924$).
🔹 **Metrologia Blindada:** O protocolo de 5 portões confirmou o resultado nulo ($p_{\text{corrigido}} = 0,4500$; $\Delta\text{BIC} = -18,15$), provando imunidade total contra falsos alarmes.

Tudo 100% aberto e reprodutível:
📄 DOI Paper 7: https://doi.org/10.5281/zenodo.24149842
💻 Artigo e Código: https://github.com/bruno-olivaes/lhc-nsbi-dsi
🏛️ Monografia Unificada: https://doi.org/10.5281/zenodo.24124702

#MachineLearning #HighEnergyPhysics #CERN #DeepLearning #OpenScience #DataScience #Physics

---

## 🌌 Paper 1: Cosmologia Observacional (Planck 2018 DSI)

### 🐦 X (Twitter) [264 caracteres]
Testamos a Invariância Discreta de Escala (DSI) na CMB do satélite Planck 2018 com protocolo pré-registrado (v2.1.2) e 5 portões de integridade. Resultado nulo certificado: p = 0.998, ΔBIC = -49.80 e ε < 0.05.
Paper & DOI: https://doi.org/10.5281/zenodo.24121677
#Cosmology #Physics #OpenScience #Planck

### 💼 LinkedIn
🌌 **Invariância Discreta de Escala na Radiação Cósmica de Fundo: Um Teste Certificado no Planck 2018**

Assinaturas log-periódicas no início do universo são previstas por modelos de inflação não-padrão. Mas como evitar o viés de garimpo de ruído (*look-elsewhere effect*)?

No Paper 1, desenvolvemos um protocolo pré-registrado no Git (tag `v2.1.2`) de 3 estágios com 5 portões matemáticos de integridade aplicado aos resíduos sobre o espectro oficial `BestFit` $\Lambda$CDM do Planck 2018 PR3 ($N=83$ multipolos, SHA-256 verificado):
✅ 1.000 simulações bootstrap com fase embaralhada.
✅ Candidato residual principal ($\hat{\lambda} = 1,2938 \pm 0,0072$) com $p_{\text{corrigido}} = 0,998$ e $\Delta\text{BIC} = -49,80$ (resultado nulo robusto).
✅ Limite superior primordial certificado: $\varepsilon_{95\%} < 0,05$ em $\lambda \in [1,1; 148]$.

A ciência avança quando eliminamos falsos positivos com rigor metrológico.

📄 DOI Zenodo: https://doi.org/10.5281/zenodo.24121677
💻 GitHub: https://github.com/bruno-olivaes/dsi-cosmo-search

#Cosmology #Astrophysics #Planck2018 #OpenScience #DataAnalysis #Physics

---

## 🔬 Paper 2: Efeito Casimir & Metrologia AFM

### 🐦 X (Twitter) [264 caracteres]
Cuidado com splines e polinômios em forças de superfície! Mostramos como o Fenômeno de Runge gera falsos periódicos na força de Casimir (583.5 nm) e propomos base física {1, z⁻⁴, z⁻⁵} + GLS direto.
DOI: https://doi.org/10.5281/zenodo.24121687
#Nanotechnology #Metrology #Physics #AFM

### 💼 LinkedIn
🔬 **Armadilhas Estatísticas na Espectroscopia de Força de Casimir: Eliminando Falsos Positivos em AFM**

Em medidas de força de Casimir e gravidade em escala sub-micrométrica, oscilações residuais têm sido frequentemente interpretadas como física exótica.

No Paper 2, analisamos $N = 497$ resíduos de pressão dinâmica e $N = 288$ resíduos de força estática extraídos vetorialmente sem perdas de Decca et al. (PRL 2003), além de mapas KPFM 2D de de Jong et al. (Nat. Phys. 2025). Demonstramos que oscilações aparentes ($\lambda = 583,5\text{ nm}$, $\text{FAP} = 1,49\times 10^{-45}$) decorrem do **Fenômeno de Runge** em polinômios cúbicos sobre caudas $z^{-4}$, enquanto a reamostragem por splines atenua $22,6\%$ da variância em $\lambda = 7,5\text{ nm}$ (degradando $\text{MDL}_{90}$ em $2,27\times$).

Ao adotar a base física $\{1, z^{-4}, z^{-5}\}$ — que absorve analiticamente desvios lineares de ponto de contato ($-4 C_4 \delta z_0 z^{-5}$) — e periodogramas Generalized Lomb-Scargle diretos, $\chi^2/\text{dof}$ cai para $1,14$ ($\text{FAP} = 0,163$), restaurando o ruído branco instrumental.

📄 DOI Zenodo: https://doi.org/10.5281/zenodo.24121687
💻 Repositório: https://github.com/bruno-olivaes/casimir-afm-spectroscopy

#Nanotechnology #Metrology #CasimirEffect #QuantumPhysics #Instrumentation

---

## 🔭 Paper 3: Energia Escura Oscilatória & ESA Euclid

### 🐦 X (Twitter) [267 caracteres]
Onde o ESA Euclid quebra a degenerescência da Energia Escura oscilatória? Resolvemos a continuidade exata e calculamos a matriz de Fisher Stage-IV sobre Pantheon+ full-cov + DESI + Planck CMB.
DOI: https://doi.org/10.5281/zenodo.24121691
#Cosmology #DarkEnergy #Euclid #ESA

### 💼 LinkedIn
🔭 **Prevendo Energia Escura Log-Oscilatória com o Telescópio Espacial ESA Euclid**

A tensão de Hubble ($H_0$) e anomalias cosmológicas motivam modelos de Energia Escura dinâmica além da constante cosmológica $\Lambda$.

No Paper 3 ($w(a) = -1 + A \sin((2\pi/\lambda)\ln a + \phi_0)$):
🔹 Obtemos a solução analítica exata de $\rho_{\mathrm{DE}}(z)$ com a matriz de covariância completa $1580\times 1580$ do Pantheon+ + DESI BAO + Planck CMB ($\Delta\chi^2 = -3,90$, $\Delta\text{BIC} = +18,22$).
🔹 Quantificamos via matriz de Fisher Stage-IV ($\sigma_H/H = 1,3\%$) que $H(z)$ isolado do Euclid separa os melhores ajustes atuais em apenas $0,103\%$ ($0,18\sigma$), porém com prior $\sigma_{\Omega_m} = 0,007$ atinge sensibilidade $3\sigma$ de $A_{3\sigma} \approx 0,15\text{--}0,29$ para $\lambda \in [1,5; 10]$ — motivando sinergia multi-sonda (lenteamento fraco, $D_M$ e Ly-$\alpha$ BAO).

📄 DOI Zenodo: https://doi.org/10.5281/zenodo.24121691
💻 Repositório: https://github.com/bruno-olivaes/oscillatory-dark-energy-euclid

#Cosmology #DarkEnergy #EuclidMission #Astrophysics #TheoreticalPhysics

---

## ⚛️ Paper 4: Computação Quântica & Mitigação de Ruído (ZNE)

### 🐦 X (Twitter) [264 caracteres]
Quando a extrapolação harmônica falha em qubits NISQ? Benchmark via emulação Qiskit 2.x AerSimulator (ruído heavy-hex, 24k tiros): 85.4% em 1Q, falha em 4Q (MAE=2.28) vs. 80.8–81.0% com Pauli Twirling.
DOI: https://doi.org/10.5281/zenodo.24121693
#QuantumComputing #Qiskit #NISQ #QEM

### 💼 LinkedIn
⚛️ **Quando o ZNE Harmônico Falha: Benchmarking de Mitigação de Erros sob Modelos Transmon Heavy-Hex**

A mitigação de erros quânticos (Zero-Noise Extrapolation - ZNE) é essencial na era NISQ. Mas será que extrapolações espectrais harmônicas sempre funcionam?

No Paper 4, realizamos um benchmark pré-registrado via emulações de alta fidelidade no Qiskit 2.x (`AerSimulator`) calibradas com modelos de ruído *heavy-hex* de transmons supercondutores ($24.000$ tiros/semente):
🔹 Em 1 qubit (Ramsey echo coerente, $\lambda \le 17$), o ZNE Harmônico via Lomb-Scargle reduz o MAE em **85,4%**.
🔹 Em 4 qubits (Trotter TFIM), crosstalk não-comutativo $ZZ$ e interferência multimodal causam falha catastrófica do HZNE ($\text{MAE} = 2,28$ em $\epsilon = 0,04\text{ rad}$ vs. $0,148$ sem mitigação).
🔹 O **Pauli Twirling** (Randomized Compiling) converte crosstalk coerente em canais estocásticos, permitindo reduções de erro de **80,8%–81,0%** com ZNE linear e exponencial.

Fornecemos uma árvore de decisão diagnóstica para desenvolvedores quânticos.

📄 DOI Zenodo: https://doi.org/10.5281/zenodo.24121693
💻 Código aberto: https://github.com/bruno-olivaes/qiskit-lombscargle-zne

#QuantumComputing #Qiskit #IBMQuantum #QuantumErrorMitigation #NISQ #OpenSource

---

## 🔐 Paper 5: Criptografia Pós-Quântica no TLS 1.3 (NIST FIPS 203)

### 🐦 X (Twitter) [265 caracteres]
Qual o custo real de migrar para a criptografia pós-quântica na internet? Auditamos a fragmentação TCP do NIST ML-KEM-768 no handshake do TLS 1.3.
DOI: https://doi.org/10.5281/zenodo.24121695
#Cybersecurity #PostQuantum #Cryptography #Networking #InfoSec

### 💼 LinkedIn
🔐 **O Custo de Rede da Criptografia Pós-Quântica: Fragmentação TCP no TLS 1.3 (NIST FIPS 203)**

A migração para a criptografia resistente a computadores quânticos é urgente, mas quais são os gargalos de infraestrutura?

No Paper 5, realizamos uma auditoria determinística de transporte de socket e modelagem exata da fronteira MTU de 1.500 B (MSS 1.460 B) comparando o padrão NIST FIPS 203 (ML-KEM / Kyber-768) e KEMs híbridos contra RSA-3072 e ECDH X25519:
⚠️ Chaves públicas maiores (1.184 bytes) e cifras (1.088 bytes) forçam o `ClientHello` híbrido (`1.518 B`) além do MSS de 1.460 B (MTU de 1.500 bytes), gerando fragmentação em 2 segmentos TCP.
⚠️ A fragmentação TCP eleva a latência em conexões de alta perda de pacotes e redes móveis.
✅ Apresentamos estratégias de cripto-agilidade para mitigar esse impacto sem comprometer a segurança.

📄 DOI Zenodo: https://doi.org/10.5281/zenodo.24121695
💻 Repositório: https://github.com/bruno-olivaes/pqc-crypto-agility-benchmark

#Cybersecurity #PostQuantumCryptography #NIST #TLS13 #NetworkSecurity #InfoSec

---

## 💥 Paper 6: Busca de DSI em Dados Abertos do LHC (CMS)

### 🐦 X (Twitter) [268 caracteres]
Aplicamos o protocolo de 5 portões a 62.214 colisões dimuon do CMS no LHC (CERN Open Data). Resultado nulo certificado (p = 0.3240 na janela limpa; ΔBIC = +238.8) e sem universalidade com o Planck.
DOI: https://doi.org/10.5281/zenodo.24149840
#ParticlePhysics #LHC #CERN #DataScience

### 💼 LinkedIn
💥 **Busca Certificada de Invariância de Escala Discreta em Espectros Dimuon do LHC**

Existe uma constante de escala geométrica universal que conecta colisores de partículas e o cosmos primordial?

No Paper 6, adaptamos o protocolo de metrologia de 3 estágios para analisar 62.214 eventos físicos de dimuons ($\mu^+\mu^-$) do experimento CMS ($\sqrt{s} = 7\,\text{TeV}$, CERN Open Data):
❌ No contínuo limpo Drell-Yan ($11\text{--}75\,\text{GeV}$, $N = 17.458$), o candidato em $\hat{\lambda} = 2.902 \pm 0.075$ falha nos portões de amplitude ($A = 2.15 < 2.87$) e bootstrap ($p = 0.3240$; $\Delta\text{BIC} = +238.82$).
❌ No espectro amplo ($2\text{--}110\,\text{GeV}$), ressonâncias conhecidas ($J/\psi, \Upsilon, Z$) também falham no Portão 2 de amplitude ($A = 7.83 < 13.49$) e não formam uma escada geométrica contínua.
❌ Zero correlação com o candidato cosmológico do Planck ($\lambda = 1.2938 \pm 0.0072$).

Eliminamos especulações com metrologia reprodutível.

📄 DOI Zenodo: https://doi.org/10.5281/zenodo.24149840
💻 Repositório & Artigo: https://github.com/bruno-olivaes/lhc-dsi-search
🏛️ Monografia: https://doi.org/10.5281/zenodo.24124702

#ParticlePhysics #HighEnergyPhysics #CERN #CMSExperiment #LHC #OpenData

---

## 🏛️ Monografia Master Unificada (*The Matrioska Protocol*)

### 🐦 X (Twitter) [267 caracteres]
Da cosmologia primordial à criptografia pós-quântica: publiquei a monografia master unificada de 45 páginas (7 capítulos) integrando 7 artigos científicos sob um único protocolo metrológico.
DOI CERN/Zenodo: https://doi.org/10.5281/zenodo.24124702
#Physics #OpenScience #Quantum

### 💼 LinkedIn
🏛️ **The Matrioska Protocol: Da Invariância de Escala Primordial à Criptografia Pós-Quântica**

Tenho a satisfação de disponibilizar a **Monografia Master Unificada** (45 páginas, 7 capítulos), sintetizando um programa de pesquisa interdisciplinar que conecta física fundamental, inteligência artificial e segurança computacional:

Consolidando 7 artigos de pesquisa:
1️⃣ Cosmologia Observacional (Planck 2018 CMB)
2️⃣ Espectroscopia de Força de Casimir & Metrologia AFM
3️⃣ Energia Escura Oscilatória & ESA Euclid
4️⃣ Mitigação de Erro Quântico (ZNE) via Emulação Qiskit 2.x *Heavy-Hex*
5️⃣ Criptografia Pós-Quântica no TLS 1.3 (NIST FIPS 203 & Fronteira MTU 1.500 B)
6️⃣ Busca de DSI em Espectros de Massa do LHC (CMS Open Data)
7️⃣ Verossimilhança Não-Binada ($4\times 64$ GL) & NSBI com ganho de até 29,1x vs. 20 bins no LHC

Organizado formalmente sob a Classificação Decimal de Dewey (CDD 500 $\to$ 530 $\to$ 006) e arquivado permanentemente no CERN / Zenodo:

🏛️ **DOI Master Oficial:** https://doi.org/10.5281/zenodo.24124702
📖 Perfil Academia.edu: https://independent.academia.edu/BrunoOlivaes

Agradeço à comunidade científica e aos entusiastas de ciência aberta pelo diálogo e suporte!

#OpenScience #TheoreticalPhysics #Cosmology #QuantumComputing #MachineLearning #Cybersecurity #CERN #Zenodo

