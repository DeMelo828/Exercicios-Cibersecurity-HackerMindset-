import requests
import os

def check_subdomains(url_base):
    file_path = "ex4/subdomains-top1million-5000.txt"
    if not os.path.exists(file_path):
        print(f"O arquivo '{file_path}' não foi encontrado.")
        return
    with open(file_path, "r") as arquivo:
        subdominios = [linha.strip() for linha in arquivo.readlines()[:20]]
    for subdominio in subdominios:
        full_url = f"https://{subdominio}.{url_base}"
        try:
            response = requests.get(full_url)
            print(f"URL: {full_url} - Status Code: {response.status_code}")
        except requests.exceptions.RequestException as e:
            print(f"Erro ao acessar {full_url}: {e}")
check_subdomains("youtube.com")




