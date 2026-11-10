# dsi-cosmo-search

Busca pré-registrada por Invariância Discreta de Escala (DSI)
em espectros de potência cosmológicos.

## Rodar

    pip install numpy scipy astropy dynesty matplotlib pytest
    pytest tests/ -v
    python scripts/run_sanity.py --stage ac

## Etapas

1. Sanity check (a e c) — valida o núcleo em dados sintéticos
2. Sanity check (b) — valida o nulo no Planck real (após baixar dados)
3. Pré-registro no OSF (congela o protocolo)
4. Stage B: `python scripts/run_planck.py --seed <int>`
5. Replicação: `python scripts/run_desi.py --seed <int>`

## Licença
MIT.

