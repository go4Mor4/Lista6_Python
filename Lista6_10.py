dezena_unidade = ['um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze', 'treze', 'quatorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove'], \
                 ['vinte', 'trinta', 'quarenta', 'cinquenta', 'sessenta', 'setenta', 'oitenta', 'noventa']
numero = int(input("Digite um número: "))
while numero < 0 or numero > 99:
    print("[o numero tem que estar entre 1 e 99]")
    numero = int(input("Digite um número: "))
if numero < 20:
    print(dezena_unidade[0][numero - 1])
else:
    numero = str(numero)
    if numero[1] == '0':
        numero = int(numero[0])
        print(dezena_unidade[1][numero -2])
    else:
        numero_d = int(numero[0])
        print(dezena_unidade[1][numero_d - 2], end=" e ")
        numero_u = int(numero[1])
        print(dezena_unidade[0][numero_u - 1])