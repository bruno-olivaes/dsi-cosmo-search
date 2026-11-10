# 📌 Instruções Passo a Passo: Ativação do Repositório no Zenodo

Como o repositório `dsi-cosmo-search` no GitHub foi criado recentemente, o Zenodo precisa da sua autorização para conectar o webhook que emite o DOI de citação de software científico.

---

### Passo 1: Acesse as Configurações do GitHub no Zenodo
1. Acesse: **[https://zenodo.org/account/settings/github/](https://zenodo.org/account/settings/github/)**
2. Se não estiver conectado, faça login com a sua conta do GitHub (`bruno-olivaes`).

---

### Passo 2: Sincronizar e Ativar o Repositório
1. Na lista de repositórios, clique no botão **"Sync now"** no canto superior direito para o Zenodo carregar seus novos repositórios do GitHub.
2. Localize na lista o repositório:
   ```
   bruno-olivaes/dsi-cosmo-search
   ```
3. Clique no botão de toggle ao lado do repositório para mudá-lo de **OFF** para **ON** (Verde).

---

### Passo 3: Emitir o DOI do Zenodo
Como a release `v2.1.1` já existe no GitHub, assim que você ligar o toggle:
- Se o Zenodo capturar a release automaticamente:
  Ele gerará um DOI no formato `10.5281/zenodo.XXXXXXX`.
- Se o Zenodo só escutar novas releases após a ativação:
  Basta criar a tag `v2.1.2` no terminal com um único comando:
  ```bash
  cd C:\Users\bruno\projects\dsi-cosmo-search
  gh release create v2.1.2 --title "v2.1.2 - Zenodo Archive Sync" --notes "Release to trigger automated Zenodo archiving."
  ```

---

### Passo 4: Adicionar o Badge ao README.md
Assim que o DOI for emitido (exemplo: `10.5281/zenodo.14889921`), adicione a seguinte linha no topo do `README.md`:
```markdown
[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.XXXXXXX.svg)](https://doi.org/10.5281/zenodo.XXXXXXX)
```

