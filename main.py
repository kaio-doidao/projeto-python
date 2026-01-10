def area_do_aluno():
    while True:
        print("\n--area do aluno--")
        print("A- fazer cadastro")
        print("B- lista de alunos")
        print("C- dados dos alunos")
        print("0- voltar")

        opcao = input("escolha uma opcao: ").upper()

        if opcao == "A":
            print("Cadastro de aluno")
        elif opcao == "B":
            print("Lista de alunos")
        elif opcao == "C":
            print("Dados dos alunos")
        elif opcao == "0":
            break
        else:
            print("Opção inválida")


        

def area_do_professor():
    while True:
        print("--area do professor--")
        print("D- fazer cadastro")
        print("E- lista de professores")
        print("F- dados dos professores")
        print("0 - voltar")

        opcao = input("escolha um opcao: ").upper()

        if opcao == "D":
            print("Cadastro de professor")
        elif opcao == "E":
            print("Lista de professores")
        elif opcao == "F":
            print("Dados dos professores")
        elif opcao == "0":
            break
        else:
            print("Opção inválida")



def exercicios():
    while True:
        print("--exercicios--")
        print("G- lista de exercicios")
        print("H- enviar exercicios")
        print ("0 - voltar")

        opcao = input("escolha um opcao: ").upper()

        if opcao == "G":
            print("Lista de exercícios")
        elif opcao == "H":
            print("Enviar exercícios")
        elif opcao == "0":
            break
        else:
            print("Opção inválida")



def relatorios():
    while True:
        print("--relatorios--")
        print("I- relatorio de alunos")
        print("J- relatorio de professores")
        print("0 - voltar")

        opcao = input("escolha um opcao: ").upper()

        if opcao == "I":
            print("Relatório de alunos")
        elif opcao == "J":
            print("Relatório de professores")
        elif opcao == "0":
            break
        else:
            print("Opção inválida")


def menu():
    while True:
        print("\n==== menu==")
        print("1- area do aluno")
        print("2- area do professor")
        print("3- exercicios")
        print("4- relatorios")
        print("0- sair")

        opcao = input("escolha uma opcao: ")

        if opcao == "1":
            area_do_aluno()
        elif opcao == "2":
            area_do_professor()
        elif opcao == "3":
            exercicios()
        elif opcao == "4":
            relatorios()
        elif opcao == "0":
            print("Saindo do sistema...")
            break
        else:
            print("Opção inválida")

# executar o programa
menu()
    