
from PetVirtual import Pet

nome = input("Digite o nome do animal: ")
pet = Pet(50, 50, nome)

resposta = 1

while resposta > 0:
    pet.mostrarStatus()

    print("\n1 - Alimentar")
    print("2 - Brincar")
    print("3 - Dormir")
    print("0 - Sair")
    
    
    
    resposta = int(input("O que deseja fazer? "))
    
    match resposta:
        case 1:
            pet.alimentar()
        case 2:
            pet.brincar()
        case 3:
            pet.dormir()
        case 0:
            print("Até logo!")
        case _:
            print("Opção inválida!")
