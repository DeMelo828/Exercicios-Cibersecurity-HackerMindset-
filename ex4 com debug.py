import requests

url_base = "youtube.com"  

def fetch_data(request_url):
    import ipdb;ipdb.set_trace()
    try:
        response = requests.get(request_url)
        if response.status_code == 200:
            print(f"Status code 200 for {request_url}")
            return response.text  # Retornar o conteúdo da resposta
        else:
            print(f'Erro: {response.status_code} para {request_url}')
            return None
    except requests.exceptions.RequestException as e:
        print(f'Ocorreu um erro: {e} para {request_url}')
        return None

# Abrir e ler o arquivo 'test2.txt'
with open("test2.txt", "r") as arquivo:
    for i, linha in enumerate(arquivo):
        if i < 20:
            linha = linha.strip()
            print(f"Lendo URL base: {linha}")
            full_url = f"https://{linha}.{url_base}"
            data = fetch_data(full_url)
            if data:
                print(data)
        else:
            break



