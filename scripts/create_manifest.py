import hashlib, json, os, sys

def sha256(path):
    h = hashlib.sha256()
    with open(path, 'rb') as f:
        for chunk in iter(lambda: f.read(8192), b''):
            h.update(chunk)
    return h.hexdigest()

def main():
    files = [
        'COM_PowerSpect_CMB-TT-binned_R3.01.txt'
    ]
    manifest = {}
    for fname in files:
        path = os.path.join('data', 'planck', fname)
        if not os.path.exists(path):
            print(f"ERRO: Arquivo não encontrado: {path}")
            print("Por favor, baixe os dados do Planck 2018 (PLA) e coloque-os em data/planck/")
            print("Links:")
            print("1. https://pla.esac.esa.int/")
            print("2. Navegue até: Cosmology -> CMB power spectra -> PR3 (2018)")
            print("3. Baixe: COM_PowerSpect_CMB-TT-binned_R3.01.txt")
            sys.exit(1)
        manifest[fname] = sha256(path)
        print(f"Hash de {fname}: {manifest[fname]}")
    
    with open('data_manifest.json', 'w') as f:
        json.dump(manifest, f, indent=2)
    print("\nManifesto gerado com sucesso em data_manifest.json")

if __name__ == '__main__':
    main()
