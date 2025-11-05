def ler_usuario():
    while True:
        nome = input("Digite seu nome:")
        if not nome.strip():
            print("Seu nome tem que ser preenchido.")
        elif any(char.isdigit() for char in nome):
            print("Seu nome não pode conter número.")
        else:
            return nome
   

def ler_idade():
    while True:
        try:
            idade = int(input("Digite sua idade:"))
            return idade
        except ValueError:
            print("Deve conter só números.")

nome = ler_usuario()
idade = ler_idade()

print(f"Nome: {nome}")
print(f"Idade: {idade}")