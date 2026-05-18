import math
from colorama import Fore, Style, init
init()

print(Fore.BLUE + "\n--RESOLUÇÃO DE CONTAS MATEMÁTICAS--\n" + Style.RESET_ALL)

while True:
    print(Fore.GREEN + "\n============= MENU =============")
    print("0  - Sair do menu")
    print("1 - Soma")
    print("2 - Subtração")
    print("3 - Multiplicação")
    print("4 - Divisão")
    print("5 - Cálculo de Média")
    print("6 - Equação de Segundo Grau")
    print("7 - Fatorial")
    print("8 - Conversão de Unidades")
    print("9 - Tabuada Completa")
    print("10 - Fibonacci")
    print("=================================\n")
    print(Style.RESET_ALL)

    opcao = input("- ESCOLHA A OPÇÃO DESEJADA DO MENU: ")
    print("\n")

    # Switch/Case (match/case), ao invés de if/elif, para questão de legibilidade.
    match opcao:
        case "1":
            print(Fore.GREEN + "|| Você escolheu realizar um cálculo de Soma ||" + Style.RESET_ALL)
            a = float(input("Digite o valor de A: "))
            b = float(input("Digite o valor de B: "))
            conta = a + b
            print(f"\nO Resultado da soma é: {conta:.2f}")

        case "2":
            print(Fore.GREEN + "|| Você escolheu realizar um cálculo de Subtração ||" + Style.RESET_ALL)
            a = float(input("Digite o valor de A: "))
            b = float(input("Digite o valor de B: "))
            conta = a - b
            print(f"\nO Resultado da subtração é: {conta:.2f}")

        case "3":
            print(Fore.GREEN + "|| Você escolheu realizar um cálculo de Multiplicação ||" + Style.RESET_ALL)
            a = float(input("Digite o valor de A: "))
            b = float(input("Digite o valor de B: "))
            conta = a * b
            print(f"\nO Resultado da multiplicação é: {conta:.2f}")

        case "4":
            print(Fore.GREEN + "|| Você escolheu realizar um cálculo de Divisão ||" + Style.RESET_ALL)
            a = float(input("Digite o valor de A: "))
            b = float(input("Digite o valor de B: "))
            if b != 0:
                conta = a / b
                print(f"\nO resultado da divisão é: {conta:.2f}")
            else:
                print("\nNão é possível dividir por zero !!!")

        case "5":
            print(Fore.GREEN + "|| Você escolheu realizar um cálculo de Média ||" + Style.RESET_ALL)
            quantidade = int(input("Digite quantos números deseja inserir no cálculo --> "))
            soma = 0 
            for i in range(quantidade):
                numero = float(input(f"Digite o número {i+1}: ")) 
                soma = (soma + numero)
            media = soma / quantidade
            print(f"\nO resultado do cálculo da média é: {media:.2f}")

        case "6":
            print(Fore.GREEN + "|| Você escolheu realizar um cálculo de Equação de Segundo Grau ||" + Style.RESET_ALL)
            a = float(input("Digite o valor de a: "))
            b = float(input("Digite o valor de b: "))
            c = float(input("Digite o valor de c: "))
            delta = ((b**2) - (4*a*c))

            if a == 0:
                print("\nNão é equação do segundo grau!!!\n")
            elif delta < 0:
                print("\nNão há raízes reais!!!\n")
            elif delta == 0:
                x = -b / (2*a)
                print(f"\nRaiz única: x = {x:.2f}\n")
            else:
                x1 = (-b + math.sqrt(delta)) / (2*a)
                x2 = (-b - math.sqrt(delta)) / (2*a)
                print(f"\nx1 = {x1:.2f}")
                print(f"x2 = {x2:.2f}\n")

        case "7":
            print(Fore.GREEN + "|| Você escolheu realizar um cálculo Fatorial ||" + Style.RESET_ALL)
            num = int(input("Digite um número: "))
            fatorial = 1
            for i in range(1, num + 1):
                fatorial = fatorial * i
            print(f"\nO resultado da fatoração é: {fatorial:.2f}")

        case "8":
            print(Fore.GREEN + "|| Você escolheu realizar um cálculo para Conversão de Unidades ||" + Style.RESET_ALL)
            while True:
                print(Fore.MAGENTA + "\n========== MENU DE CONVERSÃO ===========")
                print("0 - Sair do Sub-menu")
                print("1 - Conversão de Km/h para M/s")
                print("2 - Conversão de Horas para Minutos")
                print("3 - Conversão de Kg para g")
                print("4 - Conversão de Celsius para Fahrenheit")
                print("====================================\n")
                print(Style.RESET_ALL)

                escolha = input("- ESCOLHA A OPÇÃO DESEJADA DO MENU: ")
                print("\n")

                match escolha:
                    case "1":
                        print(Fore.MAGENTA + "|| Você escolheu realizar uma Conversão de Km/h para M/s ||" + Style.RESET_ALL)
                        kmh = float(input("Digite a velocidade (Km/h): "))
                        ms = kmh / 3.6
                        print(f"\nA conversão de {kmh:.2f} Quilômetros por hora é {ms:.2f} Metros por segundo")
                    case "2":
                        print(Fore.MAGENTA + "|| Você escolheu realizar uma Conversão de Horas para Minutos ||" + Style.RESET_ALL)
                        horas = float(input("Digite as horas desejadas: "))
                        min = horas * 60
                        print(f"\nA conversão de {horas:.2f} Horas é {min:.2f} Minutos")
                    case "3":
                        print(Fore.MAGENTA + "|| Você escolheu realizar uma Conversão de Kg para g ||" + Style.RESET_ALL)
                        kg = float(input("Digite as Quilogramas: "))
                        g = kg * 1000
                        print(f"\nA conversão de {kg:.2f} Quilogramas é {g:.2f} gramas")
                    case "4":
                        print(Fore.MAGENTA + "|| Você escolheu realizar uma Conversão de Celsius para Fahrenheit ||" + Style.RESET_ALL)
                        c = float(input("Digite a Temperatura em Celsius: "))
                        f = (c * 9/5) + 32
                        print(f"\nA conversão de {c:.2f} Graus Celsius é {f:.2f} Fahrenheit")
                    case "0":
                        print(Fore.YELLOW + "|| VOCÊ ESCOLHEU VOLTAR AO MENU PRINCIPAL ||" + Style.RESET_ALL)
                        break
                    case _:  # Equivalente ao 'else', captura qualquer outra coisa
                        print(Fore.RED + "OPÇÃO INVÁLIDA!!" + Style.RESET_ALL)
                        break

        case "9":
            print(Fore.GREEN + "|| Você escolheu realizar uma Tabuada Completa ||" + Style.RESET_ALL)
            num = int(input("Digite o número da tabuada desejada: "))
            print("\n") 
            for i in range(1, 11):
                print(num, "x", i, "=", num * i)

        case "10":
            print(Fore.GREEN + "|| Você escolheu calcular a Sequência de Fibonacci ||" + Style.RESET_ALL)
            x = int(input("Digite quantos termos deseja ver: "))
            a, b = 0, 1
            for i in range(x):
                print(a)
                a, b = b, a + b

        case "0":
            print(Fore.YELLOW + "|| VOCÊ ESCOLHEU FECHAR O MENU ||" + Style.RESET_ALL)
            break

        case _:  # Opção inválida do menu principal
            print(Fore.RED + "OPÇÃO INVÁLIDA!!\n" + Style.RESET_ALL)
            break
