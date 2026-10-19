class Pet:
    def __init__(self, energia, fome, nome):
        self.energia = energia
        self.fome = fome
        self.nome = nome

    def alimentar(self):
        print("Você alimentou seu Pet!")
        self.fome -= 5

    def brincar(self):
        print("Você brincou com seu Pet!")
        self.energia -= 5

    def dormir(self):
        print("O seu Pet dormiu!")
        self.energia += 5

    def mostrarStatus(self):
        print("=== PET VIRTUAL ===")
        print("Nome:", self.nome)
        print("Energia:", self.energia)
        print("Fome:", self.fome)
