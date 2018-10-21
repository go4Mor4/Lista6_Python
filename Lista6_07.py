frase = str(input("Digite uma frase: ")).lower()
espacos = frase.count(' ')
vogais = []
for i in range(len(frase)):
    if frase[i] in ['a', 'e', 'i', 'o', 'u']:
        vogais.append(frase[i])
    else:
        continue
print("\nExistem ", espacos, "espaços na frase.")
print("A: ", vogais.count('a'), "\nE: ", vogais.count('e'), "\nI: ", vogais.count('i'), "\nO: ", vogais.count('o'), "\nU: ", vogais.count('u'))

