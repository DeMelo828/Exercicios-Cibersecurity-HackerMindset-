import requests
import os

def check_subdomains(domain, wordlist):
    if not os.path.exists(wordlist):
        print(f"O arquivo '{wordlist}' não foi encontrado.")
        return

    with open(wordlist, "r") as arquivo:
        subdominios = [linha.strip() for linha in arquivo if linha.strip()]

    session = requests.Session()

    for subdominio in subdominios:
        full_url = f"http://{subdominio}.{domain}"
        try:
            response = session.get(full_url, timeout=5)
            if response.status_code // 100 == 2:
                print(f"Subdomínio encontrado: {full_url} - Status Code: {response.status_code}")
        except requests.RequestException as e:
            print(f"Erro ao tentar acessar {full_url}: {e}")

    session.close()

def check_paths(domain, wordlist):
    if not os.path.exists(wordlist):
        print(f"O arquivo '{wordlist}' não foi encontrado.")
        return

    with open(wordlist, "r") as arquivo:
        paths = [linha.strip() for linha in arquivo if linha.strip()]

    session = requests.Session()
    base_url = f"http://{domain}"

    for path in paths:
        # URL encoding for the path to handle special characters
        encoded_path = requests.utils.quote(path)
        full_url = f"{base_url}/{encoded_path}"
        try:
            response = session.get(full_url, timeout=5)
            if response.status_code // 100 == 2:
                print(f"Path encontrado: {full_url} - Status Code: {response.status_code}")
        except requests.RequestException as e:
            print(f"Erro ao tentar acessar {full_url}: {e}")

    session.close()

def main():
    print("----------------------------------")
    print("1tdcr Vitor de Melo")
    print("Alvo:")
    domain = input("Digite o domínio (exemplo: example.com): ").strip()
    
    subdomains_wordlist = "subdomains-top1million-5000.txt"
    paths_wordlist = "subdomains-top1million-5000.txt"  # Use a wordlist específica para paths e arquivos

    print("\nVerificando subdomínios...")
    check_subdomains(domain, subdomains_wordlist)

    print("\nVerificando paths e arquivos...")
    check_paths(domain, paths_wordlist)

if __name__ == "__main__":
    main()
