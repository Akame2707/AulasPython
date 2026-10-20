
import random
from Jogador import Jogador, agir, fugir, flertar
from Inimigo import gerar_inimigo


def main():
    print("=== UNDERTALE PYTHON ===")

    nome = input("Digite o nome do humano: ")

    jogador = Jogador(vidaP=50, LVP=1, energiaP=30)

    print(f"\nOlá, {nome}!")
    print("Você caiu no Subterrâneo...")

    inimigo = gerar_inimigo()

    print(f"\nUm {inimigo.nome} apareceu!")

    while jogador.vidaP > 0 and inimigo.esta_vivo():

        print("\n===== MENU DE BATALHA =====")
        print(f" Sua vida: {jogador.vidaP}")
        print(f"Sua energia: {jogador.energiaP}")
        print(f"Vida do inimigo: {inimigo.vida}")
        print("\n1 - Lutar")
        print("2 - Agir")
        print("3 - Fugir")
        print("4 - Flertar")

        opcao = input("\nEscolha uma opção: ")

        if opcao == "1":
            if jogador.energiaP > 10:
                jogador.lutar()

                dano = random.randint(5, 12)
                inimigo.receber_dano(dano)

                jogador.energiaP -= 10
            else:
                jogador.lutar()

        elif opcao == "2":
            agir()

        elif opcao == "3":
            fugir()
            print("Você escapou da batalha!")
            return

        elif opcao == "4":
            flertar()

        else:
            print("Opção inválida!")
            continue

        if inimigo.esta_vivo():
            dano_inimigo = inimigo.atacar()
            jogador.vidaP -= dano_inimigo

            if jogador.vidaP < 0:
                jogador.vidaP = 0

            print(f"Você recebeu {dano_inimigo} de dano!")

    if jogador.vidaP <= 0:
        print("\nGAME OVER...")
    else:
        print(f"\nVocê derrotou {inimigo.nome}!")


if __name__ == "__main__":
    main()
