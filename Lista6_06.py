chave_DMA = [['', 'um', 'dois', 'três', 'quatro', 'cinco',
              'seis', 'sete', 'oito', 'nove', 'dez',
              'onze', 'doze', 'treze', 'quatorze', 'quinze',
              'dezesseis', 'dezessete', 'dezoito', 'dezenove',],
             ['', 'vinte', 'trinta'], ['janeiro', 'fevereiro',
            'março', 'abril', 'maio', 'junho', 'julho',
            'agosto', 'setembro', 'outubro', 'novembro',
            'dezembro']]
data_numeros = input("Digite uma data no seguinte formato: [DD/MM/AA]: ")
while data_numeros[2] != '/' and data_numeros[5] != '/' and len(data_numeros) != 10:
    print("[digitação incorreta]")
    data_numeros = str(input("Digite uma data no seguinte formato: [DD/MM/AA]: "))
lista_inteiros = list(map(int, data_numeros.split('/')))
def transformador(dma, lista_data):
    if lista_data[0] < 20:
        print(dma[0][lista_data[0]], end=' de ')
    else:
        dezena = str(lista_data[0])
        dezena = int(dezena[0])
        print(dma[1][dezena-1], end='')
        unidade = str(lista_data[0])
        unidade = int(unidade[1])
        if unidade == 0:
            print(end=' de ')
        else:
            print(" e", dma[0][unidade], end=' de ')
    mes = str(lista_data[1])
    if mes[0] == '1':
        mes = int(mes[0] + mes[1])
        print(dma[2][mes - 1], end=' de ')
    else:
        mes = int(mes[0])
        print(dma[2][mes - 1], end=' de ')
    print(lista_data[2])
transformador(chave_DMA, lista_inteiros)