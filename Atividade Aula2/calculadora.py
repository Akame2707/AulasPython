print("===== MENU =====")
print("1 - Somar")
print("2 - Subtrair")
print("3 - Multiplicar")
print("4 - Dividir")
print("5 - Sair")
print("================")

opcao = int(input("Digite a opção desejada: "))

match opcao:
    case 1:
        a = float(input("Digite o primeiro número: "))
        b = float(input("Digite o segundo número: "))
        print(f"Resultado da soma: {a + b}")
    
    case 2:
        a = float(input("Digite o primeiro número: "))
        b = float(input("Digite o segundo número: "))
        print(f"Resultado da subtração: {a - b}")
    
    case 3:
        a = float(input("Digite o primeiro número: "))
        b = float(input("Digite o segundo número: "))
        print(f"Resultado da multiplicação: {a * b}")
    
    case 4:
        a = float(input("Digite o primeiro número: "))
        b = float(input("Digite o segundo número: "))
        if b != 0:
            print(f"Resultado da divisão: {a / b}")
        else:
            print("Erro: divisão por zero!")
    
    case 5:
        print("Saindo do programa...")
    
    case _:
        print("Opção inválida!")