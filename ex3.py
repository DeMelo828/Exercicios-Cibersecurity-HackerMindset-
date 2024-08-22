with open ("test.txt", "r") as senhas:
    for i, linha in enumerate(senhas):
        if i < 10:
            print(linha.strip())
        else:
            break
    