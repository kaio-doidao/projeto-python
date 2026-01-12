import json
import os

ARQ_ALUNOS = "alunos.json"
ARQ_PROFESSORES = "professores.json"
ARQ_EXERCICIOS = "exercicios.json"

DIAS = ["segunda", "terca", "quarta", "quinta", "sexta"]


# ================= ARQUIVOS =================

def carregar(arq):
    if os.path.exists(arq):
        with open(arq, "r", encoding="utf-8") as f:
            return json.load(f)
    return []

def salvar(arq, dados):
    with open(arq, "w", encoding="utf-8") as f:
        json.dump(dados, f, indent=4, ensure_ascii=False)


alunos = carregar(ARQ_ALUNOS)
professores = carregar(ARQ_PROFESSORES)
exercicios = carregar(ARQ_EXERCICIOS)


# ================= UTIL =================

def escolher_dia():
    for i, d in enumerate(DIAS, 1):
        print(f"{i} - {d.capitalize()}")
    return DIAS[int(input("Dia: ")) - 1]

def escolher_aluno():
    for i, a in enumerate(alunos, 1):
        print(f"{i} - {a['nome']}")
    return alunos[int(input("Aluno: ")) - 1]


# ================= EXERCÍCIOS (CRUD) =================

def cadastrar_exercicio():
    exercicios.append({
        "nome": input("Nome do exercício: "),
        "grupo": input("Grupo muscular: ")
    })
    salvar(ARQ_EXERCICIOS, exercicios)

def listar_exercicios():
    for i, e in enumerate(exercicios, 1):
        print(f"{i} - {e['nome']} ({e['grupo']})")

def dados_exercicios():
    for e in exercicios:
        print(e)

def excluir_exercicio():
    listar_exercicios()
    exercicios.pop(int(input("Excluir exercício: ")) - 1)
    salvar(ARQ_EXERCICIOS, exercicios)


def area_exercicios():
    while True:
        print("\n-- EXERCÍCIOS --")
        print("A - Cadastrar")
        print("B - Listar")
        print("C - Dados")
        print("D - Excluir")
        print("0 - Voltar")
        op = input("Opção: ").upper()

        if op == "A": cadastrar_exercicio()
        elif op == "B": listar_exercicios()
        elif op == "C": dados_exercicios()
        elif op == "D": excluir_exercicio()
        elif op == "0": break


# ================= ALUNOS =================

def cadastrar_aluno():
    alunos.append({
        "nome": input("Nome: "),
        "idade": int(input("Idade: ")),
        "peso": float(input("Peso: ")),
        "planos": {},
        "frequencia": {}
    })
    salvar(ARQ_ALUNOS, alunos)

def listar_alunos():
    print(f"Total: {len(alunos)}")
    for a in alunos:
        print("-", a["nome"])

def dados_alunos():
    for a in alunos:
        print(a)

def excluir_aluno():
    a = escolher_aluno()
    alunos.remove(a)
    salvar(ARQ_ALUNOS, alunos)


def area_aluno():
    while True:
        print("\n-- ÁREA DO ALUNO --")
        print("A - Cadastrar")
        print("B - Listar")
        print("C - Dados")
        print("D - Excluir")
        print("0 - Voltar")
        op = input("Opção: ").upper()

        if op == "A": cadastrar_aluno()
        elif op == "B": listar_alunos()
        elif op == "C": dados_alunos()
        elif op == "D": excluir_aluno()
        elif op == "0": break


# ================= PROFESSORES =================

def cadastrar_professor():
    professores.append({
        "nome": input("Nome: "),
        "area": input("Área: ")
    })
    salvar(ARQ_PROFESSORES, professores)

def listar_professores():
    print(f"Total: {len(professores)}")
    for p in professores:
        print("-", p["nome"])

def dados_professores():
    for p in professores:
        print(p)

def excluir_professor():
    for i, p in enumerate(professores, 1):
        print(i, p["nome"])
    professores.pop(int(input("Excluir: ")) - 1)
    salvar(ARQ_PROFESSORES, professores)


def area_professor():
    while True:
        print("\n-- ÁREA DO PROFESSOR --")
        print("A - Cadastrar")
        print("B - Listar")
        print("C - Dados")
        print("D - Excluir")
        print("0 - Voltar")
        op = input("Opção: ").upper()

        if op == "A": cadastrar_professor()
        elif op == "B": listar_professores()
        elif op == "C": dados_professores()
        elif op == "D": excluir_professor()
        elif op == "0": break


# ================= PLANO DE EXERCÍCIOS =================

def cadastrar_plano():
    aluno = escolher_aluno()
    dia = escolher_dia()
    grupo = input("Grupo muscular: ")

    lista = []
    listar_exercicios()
    while True:
        op = input("Número do exercício (enter p/ sair): ")
        if not op:
            break
        lista.append(exercicios[int(op) - 1]["nome"])

    aluno["planos"][dia] = {
        "grupo": grupo,
        "exercicios": lista
    }
    salvar(ARQ_ALUNOS, alunos)


# ================= FREQUÊNCIA =================

def registrar_frequencia():
    aluno = escolher_aluno()
    dia = escolher_dia()

    resp = input("Presente? (s/n): ").lower()
    presente = resp in ["s", "sim"]

    feitos = int(input("Exercícios feitos: ")) if presente else 0

    aluno["frequencia"][dia] = {
        "presente": presente,
        "feitos": feitos
    }
    salvar(ARQ_ALUNOS, alunos)


# ================= RELATÓRIOS =================

def relatorios():
    print("\n=== ALUNOS ===")
    listar_alunos()

    print("\n=== PROFESSORES ===")
    listar_professores()

    print("\n=== EXERCÍCIOS DOS ALUNOS ===")
    for a in alunos:
        print(a["nome"], a["planos"])

    print("\n=== FREQUÊNCIA ===")
    for a in alunos:
        print(a["nome"], a["frequencia"])


# ================= MENU =================

def menu():
    while True:
        print("""
1 - Área do aluno
2 - Área do professor
3 - Exercícios
4 - Plano de exercícios
5 - Frequência
6 - Relatórios
0 - Sair
""")
        op = input("Opção: ")

        if op == "1": area_aluno()
        elif op == "2": area_professor()
        elif op == "3": area_exercicios()
        elif op == "4": cadastrar_plano()
        elif op == "5": registrar_frequencia()
        elif op == "6": relatorios()
        elif op == "0": break


menu()


