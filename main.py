def area_do_aluno():
    while True:
        print("--area do aluno--")
        print("A- fazer cadastro")
        print("B- lista de alunos")
        print("C- dados dos alunos")

        input("escolha um opção: ")

def area_do_professor():
    while True:
        print("--area do professor--")
        print("D- fazer cadastro")
        print("E- lista de professores")
        print("F- dados dos professores")

        input("escolha um opção: ")

def exercicios():
    while True:
        print("--exercicios--")
        print("G- lista de exercicios")
        print("H- enviar exercicios")

        input("escolha um opção: ")

def relatorios():
    while True:
        print("--relatorios--")
        print("I- relatorio de alunos")
        print("J- relatorio de professores")

        input("escolha um opção: ")


def menu():
    while True:
        print("menu")
        print("1- area do aluno")
        print("2- area do professor")
        print("3- exercicios")
        print("4- relatorios")
        print("0- sair")

        opção = input("escolha uma opção: ")