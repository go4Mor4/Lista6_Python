string1 = str(input("Digite a primeira string: "))
string2 = str(input("Digite a segunda string: "))
print("\n")
print("String 1: ", string1)
print("String 2: ", string2)
print("\n")
print("Tamanho de ", string1, ": ", len(string1))
print("Tamanho de ", string2, ": ", len(string2))
print("\n")
if string1 == string2:
    print("As frases são identicas.")
else:
    print("As frases são diferentes.")
if len(string1) == len(string2):
    print("As frases tem o mesmo tamanho.")
else:
    print("As frases tem tamanhos diferentes.")