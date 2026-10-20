
import random

class Inimigo:
    def __init__(self, nome, vida, ataque):
        self.nome = nome
        self.vida = vida
        self.ataque = ataque

    def mostrar_status(self):
        print("\n======================")
        print(f"Inimigo: {self.nome}")
        print(f"Vida: {self.vida} HP")
        print(f"Ataque: {self.ataque}")
        print("======================")

    def receber_dano(self, dano):
        self.vida -= dano

        if self.vida < 0:
            self.vida = 0

        print(f"\n{self.nome} recebeu {dano} de dano!")

    def atacar(self):
        print(f"\n{self.nome} atacou você!")
        return self.ataque

    def esta_vivo(self):
        return self.vida > 0


def gerar_inimigo():
    inimigos = [
        Inimigo("Froggit", 20, 5),
        Inimigo("Whimsun", 15, 3),
        Inimigo("Moldsmal", 25, 4),
        Inimigo("Loox", 30, 7),
        Inimigo("Vegetoid", 35, 6)
    ]

    return random.choice(inimigos)
