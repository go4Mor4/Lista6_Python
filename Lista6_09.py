cpf = str(input("DIgite o CPF no seguinte formato: [xxx.xxx.xxx-xx]: "))
while cpf[3] != '.' or cpf[7] != '.' or cpf[11] != '-':
    print("CPF digitado incorretamente.")
    cpf = str(input("DIgite o CPF no seguinte formato: [xxx.xxx.xxx-xx]"))
print("CPF digitado corretamente.")
