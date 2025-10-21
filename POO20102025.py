# Questão 1

lista_numeros = list((1, 2, 3, 4, 5))
for numero in lista_numeros:
    print (numero)

# Questão 2

print(lista_numeros[0],lista_numeros[len(lista_numeros)-1], lista_numeros[3])

# Questão 3

lista_numeros[2]= "uva"
print(lista_numeros)

# Questão 4

usuario=int(input('Digite um número: '))
lista_numeros.append(usuario)
print(lista_numeros)

# Questão 5

lista_numeros.remove(1)
print(lista_numeros)