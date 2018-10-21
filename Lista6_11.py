import random
import test
import time


def forca(chances):
    if chances == 7:
        print("------------")
        print("|          |")
        print("|          ")
        print("|          ")
        print("|          ")
        print("|          ")
        print("|          ")
        print("|")

    elif chances == 6:
        print("------------")
        print("|          |")
        print("|          0")
        print("|          ")
        print("|          ")
        print("|          ")
        print("|          ")
        print("|")

    elif chances == 5:
        print("------------")
        print("|          |")
        print("|          0")
        print("|          |")
        print("|          ")
        print("|          ")
        print("|          ")
        print("|")

    elif chances == 4:
        print("------------")
        print("|          |")
        print("|          0")
        print("|         -|")
        print("|          ")
        print("|          ")
        print("|          ")
        print("|")

    elif chances == 3:
        print("------------    ")
        print("|          |    ")
        print("|          0    ")
        print("|         -|-   ")
        print("|               ")
        print("|               ")
        print("|               ")
        print("|")

    elif chances == 2:
        print("------------    ")
        print("|          |    ")
        print("|          0    ")
        print("|         -|-   ")
        print("|         /      ")
        print("|               ")
        print("|               ")
        print("|")

    elif chances == 1:
        print("------------    ")
        print("|          |    ")
        print("|          0    ")
        print("|         -|-   ")
        print("|         / \   ")
        print("|               ")
        print("|               ")
        print("|")


dicionario = [
    'melancia', 'tangerina', 'carro', 'dia', 'universo', 'galaxia', 'amor',
    'filosofia', 'antagonista', 'castigo', 'morte'
]


while True:
    letras_achadas = []
    chances = 7
    letras_erradas = []
    palavra = random.choice(dicionario)
    print("a palavra tem ", len(palavra), " letras ")
    letras_organizadas = sorted(palavra)

    while len(letras_achadas) != len(palavra) and chances > 0:
        print("\n" * 10)
        print("chances restantes: ", chances)
        forca(chances)
        for letra_posicao in palavra:
            if letras_achadas.count(letra_posicao) > 0:
                print(letra_posicao, end=" ")
            else:
                print("_ ", end="")

        letra = input("\nDigite uma letra: ")
        quant_letras = palavra.count(letra)
        if len(letra) != 1:
            print("Digite apenas uma letra.")

        else:
            if letra in palavra and letra not in letras_achadas:
                print("acertou", letra)
                if quant_letras > 1:
                    for quant_letras in range(quant_letras):
                        letras_achadas.append(letra)
                else:
                    letras_achadas.append(letra)
            elif letra in letras_erradas or letra in letras_achadas:
                print("você ja digitou esta letra")
            elif letra not in palavra:
                print("essa letra não está na palavra")
                letras_erradas.append(letra)
                chances = chances - 1
                print("chances restantes: ", chances)

            for letra_posicao in palavra:
                if letras_achadas.count(letra_posicao) > 0:
                    print(letra_posicao, end="")
                else:
                    print("_ ", end="")

    if chances == 0:
        print("\n" * 15)
        print("você perdeu, a palavra era: ", palavra)
    else:
        print("\n" * 15)
        print("você venceu, a palavra era: ", palavra)
    dicionario.remove(palavra)
    print("Reiniciando o jogo em 3 segundos...")
    time.sleep(3)