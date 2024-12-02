with open ("texto,txt", "r") as senhas:
    import ipdb;ipdb.set_trace()
    for i, linha in enumerate(senhas):
        if i < 10:
            print(linha.strip())
        else:
            break
    
