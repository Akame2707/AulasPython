class Jogador:
    def __init__(self, vidaP, LVP, energiaP):
        self.vidaP = vidaP
        self.energiaP = energiaP
        self.LVP = LVP

    def lutar(self):
        if self.energiaP > 10:
            print("Você luta contra seus inimigos!")
        else:
            print("Você está cansado demais para lutar!")


def agir():
    print("\n=== AGIR ===")
    print("1 - Conversar")
    print("2 - Elogiar")
    print("3 - Fazer carinho")
    print("4 - Voltar")

    opcao = input("Escolha uma ação: ")

    if opcao == "1":
        conversar()
    elif opcao == "2":
        elogiar()
    elif opcao == "3":
        carinho()
    elif opcao == "4":
        print("Você voltou ao menu principal.")
    else:
        print("Opção inválida!")
        agir()


def conversar():
    print("Você tentou conversar com o inimigo.")


def elogiar():
    print("Você elogiou o inimigo.")


def carinho():
    print("Você fez carinho no inimigo.")

def fugir():
    print("Você sai correndo da luta, bem, isso funciona também!")
    
def flertar():
    print("Você...flerta com o monstro?")