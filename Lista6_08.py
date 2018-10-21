mensagem = str(input("Digite a sua mensagem: ")).lower()
mensagem = mensagem.replace(' ', '')
mensagem_invertida = mensagem[:: -1]
if mensagem == mensagem_invertida:
    print("Palindromo!")
else:
    print("Não é um Palindromo!")