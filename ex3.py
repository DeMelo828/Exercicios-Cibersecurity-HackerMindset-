import os
path = r"C:\Users\labsfiap\Desktop\ex3\senhas"

directory = os.path.dirname(path)
if not os.path.exists(directory):
    os.makedirs(directory)
try:
    with open(path, "r") as senhas:
        linhas = senhas.readlines()
        if linhas:
            for i, linha in enumerate(linhas):
                if i < 10:
                    print(linha.strip())
                else:
                    break
        else:
            print("O arquivo está vazio.")
except FileNotFoundError:
    with open(path, "w") as senhas:
        print(f"O arquivo '{path}' não foi encontrado. Um novo arquivo foi criado.")

    
