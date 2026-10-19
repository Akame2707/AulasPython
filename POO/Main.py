class Pet:
    def __init__(self, nome):
        self.nome = nome

    def fazer_som(self):
        pass


class Cachorro(Pet):
    def fazer_som(self):
        print("Au au!")


class Gato(Pet):
    def fazer_som(self):
        print("Miau!")


nome = input("Digite o nome do animal: ")
tipo = input("Digite o tipo (cachorro ou gato): ").lower()

if tipo == "cachorro":
    pet = Cachorro(nome)

elif tipo == "gato":
    pet = Gato(nome)

else:
    print("Tipo de animal inválido!")
    exit()

print(f"\nNome do animal: {pet.nome}")
pet.fazer_som()