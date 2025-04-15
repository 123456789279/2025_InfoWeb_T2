print("Digite uma frase:")
frase = input()
ultima_frase = frase[ frase.rindex(" ") + 1: ]
print(ultima_frase)