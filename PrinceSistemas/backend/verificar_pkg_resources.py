import os
import sys

def check_venv_for_pkg_resources():
    site_packages = [p for p in sys.path if p.endswith('site-packages')][0]
    pacotes = set()
    
    for root, dirs, files in os.walk(site_packages):
        for file in files:
            if file.endswith('.py'):
                try:
                    path = os.path.join(root, file)
                    with open(path, 'r', encoding='utf-8', errors='ignore') as f:
                        content = f.read()
                        if 'pkg_resources' in content:
                            # Extrair nome do pacote a partir do caminho
                            rel_path = os.path.relpath(path, site_packages)
                            package = rel_path.split(os.sep)[0]
                            pacotes.add(package)
                except Exception as e:
                    pass
    
    with open('pacotes_com_pkg_resources.txt', 'w') as f:
        for package in sorted(pacotes):
            f.write(f"{package}\n")
    
    print(f"Encontrados {len(pacotes)} pacotes usando pkg_resources.")
    print(f"Resultados salvos em: {os.path.abspath('pacotes_com_pkg_resources.txt')}")

if __name__ == "__main__":
    check_venv_for_pkg_resources()
