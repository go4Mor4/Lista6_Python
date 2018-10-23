import random
biblioteca = ['chupeta', 'pessoa', 'hamburguer', 'astronauta']
vidas_usuario = 7
palavra_aleatoria = random.choice(biblioteca)
palavra_embaralhada = ''.join(random.sample(palavra_aleatoria, len(palavra_aleatoria)))
while vidas_usuario != 0:
    print("quantidade de vidas: ", vidas_usuario)
    print(palavra_embaralhada)
    resposta_usuario = input("Que palavra é essa? : ")
    if resposta_usuario == palavra_aleatoria:
        print("Você acertou, a palavra era: ", palavra_embaralhada)
        break
    else:
        vidas_usuario -= 1