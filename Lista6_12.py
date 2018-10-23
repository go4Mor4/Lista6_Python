n_telefone = str(input("Digite o n° do telefone: "))
while len(n_telefone) != 8 or n_telefone != 7:
    print("O número precisa ter 8 ou 7 digitos")
    n_telefone = str(input("Digite o n° do telefone: "))
numero_correto = []
if n_telefone[3] == '-' and len(n_telefone) == 8:
    numero_correto = ['3']
    numero_correto.append(n_telefone)
    numero_final = numero_correto[0] + numero_correto[1]
    print(numero_final)
elif '-' not in n_telefone and len(n_telefone) == 8:
    n1 = n_telefone[0:4]
    n2 = n_telefone[4:8]
    print(n1 + '-' + n2)
elif '-' not in n_telefone and len(n_telefone) == 7:
    numero_correto = ['3']
    numero_correto.append(n_telefone)
    numero_final = numero_correto[0] + numero_correto[1]
    n1 = numero_final[0:4]
    n2 = numero_final[4:8]
    print(n1 + '-' + n2)
else:
    print(n_telefone)