
# 1 Questão

lista_de_notas = []

while True:
    notas = float(input("Informe a nota : (Digite -1 para encerrar:)"))
    if notas == (-1):
        break
    else:
        lista_de_notas.append(notas)

print(lista_de_notas)

# Letra A

print(f"A LISTA POSSUI {len(lista_de_notas)} NOTAS.")

# Letra B

print(lista_de_notas)

# Letra C

for notas in reversed (lista_de_notas):
    print(notas)

# Letra D

print(sum(lista_de_notas))

#Letra E

print(sum(lista_de_notas) / len(lista_de_notas))

# Letra F
qtd = 0
for notas in lista_de_notas:
    if notas > (sum(lista_de_notas) / len(lista_de_notas)):
        qtd += 1
print(f"A quantidade de notas acima da média: {qtd}")

# Letra G

qtd = 0
for notas in lista_de_notas:
    if notas < 7:
        qtd += 1
print(f"A quantidade de notas abaixo de 7: {qtd}")

# Letra H

print("Parabéns")





