nome = input("Informe o nome: ")
vazio1 = ""
vazio2 = ""
for letra in nome:
    vazio1 += letra
for i in range(len(nome)):
    vazio2 = vazio1[0:len(nome) -i:]
    print(vazio2)