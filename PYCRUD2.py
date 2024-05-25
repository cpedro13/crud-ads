lista_estudantes = []
lista_professores = []
lista_disciplinas = []
lista_turmas = []
lista_matriculas = []

import json


# recuperando dados que foram salvos

def ler_dados_salvos():
    with open("estudantes.json", "r") as arquivo:
        for linha in arquivo:
            dados_json = json.loads(linha)
            lista_estudantes.append(dados_json)
    with open("professor.json", "r") as arquivo:
        for linha in arquivo:
            dados_json = json.loads(linha)
            lista_professores.append(dados_json)
    with open("disciplina.json", "r") as arquivo:
        for linha in arquivo:
            dados_json = json.loads(linha)
            lista_disciplinas.append(dados_json)
    with open("turma.json", "r") as arquivo:
        for linha in arquivo:
            dados_json = json.loads(linha)
            lista_turmas.append(dados_json)
    with open("matricula.json", "r") as arquivo:
        for linha in arquivo:
            dados_json = json.loads(linha)
            lista_matriculas.append(dados_json)


# salvando dados estudantes json
def salvar_estudantes():
    with open("estudantes.json", "w") as arquivo:
        for estudante in lista_estudantes:
            json.dump(estudante, arquivo)
            arquivo.write("\n")


# cadastrando estudantes
def cadastrar_estudante():
    nome = input("Digite o nome do estudante: ")
    codigo = int(input("Digite o código do estudante: "))
    cpf = input("Digite o CPF do estudante: ")
    for estudante in lista_estudantes:
        if estudante['cod_estudante'] == codigo or estudante['cpf_estudante'] == cpf:
            print("Estudante já cadastrado")
            return

    dados_estudante = {
        "nome_estudante": nome,
        "cod_estudante": codigo,
        "cpf_estudante": cpf
    }
    lista_estudantes.append(dados_estudante)
    print("Estudante cadastrado com sucesso!")
    salvar_estudantes()


def listar_estudantes():
    print("Lista de Estudantes:")
    for estudante in lista_estudantes:
        print("Nome:", estudante['nome_estudante'])
        print("Código:", estudante['cod_estudante'])
        print("CPF:", estudante['cpf_estudante'])


def editar_estudante():
    codigo_editar = int(input("Digite o código do estudante que deseja editar: "))
    for estudante in lista_estudantes:
        if estudante["cod_estudante"] == codigo_editar:
            estudante["nome_estudante"] = input("Digite o novo nome: ")
            estudante["cpf_estudante"] = input("Digite o novo CPF: ")
            print(f"Estudante com código {codigo_editar} editado com sucesso!")
            salvar_estudantes()
            return
    print(f"Estudante com código {codigo_editar} não encontrado.")


def excluir_estudante():
    codigo_excluir = int(input("Digite o código do estudante que deseja excluir: "))
    for estudante in lista_estudantes:
        if estudante["cod_estudante"] == codigo_excluir:
            lista_estudantes.remove(estudante)
            print(f"Estudante com código {codigo_excluir} removido com sucesso!")
            return
    print(f"Estudante com código {codigo_excluir} não encontrado.")


def salvar_professores():
    with open("professor.json", "w") as arquivo:
        for professor in lista_professores:
            json.dump(professor, arquivo)
            arquivo.write("\n")


def cadastrar_professor():
    nome_prof = str(input("Digite o nome do professor: "))
    cod_professor = int(input("Insira o código do professor: "))
    cpf_professor = int(input("Insira o CPF: "))
    dados_professor = {
        "nome_professor": nome_prof,
        "cod_professor": cod_professor,
        "cpf_professor": cpf_professor
    }
    lista_professores.append(dados_professor)
    print("Professor cadastrado com sucesso!")
    salvar_professores()


def listar_professor():
    print("Lista de Professores:")
    for professor in lista_professores:
        print("Nome:", professor['nome_professor'])
        print("Código:", professor['cod_professor'])
        print("CPF:", professor['cpf_professor'])


def editar_professor():
    codigo_editar = int(input("Digite o código do professor que deseja editar: "))
    for professor in lista_professores:
        if professor["cod_professor"] == codigo_editar:
            professor["nome_professor"] = input('Digite o novo nome: ')
            professor["cpf_professor"] = int(input('Insira o novo CPF: '))
            print(f"Professor com código {codigo_editar} editado com sucesso!")
            salvar_professores()
            return
    print(f"Professor com código {codigo_editar} não encontrado.")


def excluir_professor():
    codigo_excluir = int(input("Digite o código do professor que deseja excluir: "))
    for professor in lista_professores:
        if professor["cod_professor"] == codigo_excluir:
            lista_professores.remove(professor)
            print(f"Professor com código {codigo_excluir} removido com sucesso!")
            return
    print(f"Professor com código {codigo_excluir} não encontrado.")


def salvar_disciplinas():
    with open("disciplina.json", "w") as arquivo:
        for disciplina in lista_disciplinas:
            json.dump(disciplina, arquivo)
            arquivo.write("\n")


def cadastrar_disciplina():
    disciplina = input("Adicione a disciplina: ")
    disc_codigo = int(input("Digite o código da disciplina: "))

    dados_disciplina = {
        "nome_disciplina": disciplina,
        "disc_codigo": disc_codigo,
    }
    lista_disciplinas.append(dados_disciplina)
    print("Disciplina cadastrada com sucesso!")
    salvar_disciplinas()


def listar_disciplina():
    print("Lista de Disciplinas:")
    for disciplina in lista_disciplinas:
        print("Nome:", disciplina['nome_disciplina'])
        print("Código:", disciplina['disc_codigo'])


def editar_disciplina():
    codigo_editar = int(input("Código para editar: "))
    for disciplina in lista_disciplinas:
        if disciplina["disc_codigo"] == codigo_editar:
            disciplina["nome_disciplina"] = input("Digite o novo nome: ")
            print(f"Disciplina com código {codigo_editar} editado com sucesso!")
            salvar_disciplinas()
            return
    print(f"Disciplina com código {codigo_editar} não encontrado.")


def excluir_disciplina():
    codigo_excluir = int(input("Digite o código da disciplina que deseja excluir: "))
    for disciplina in lista_disciplinas:
        if disciplina["disc_codigo"] == codigo_excluir:
            lista_disciplinas.remove(disciplina)
            print(f"Disciplina com código {codigo_excluir} removido com sucesso!")
            return
    print(f"Disciplina com código {codigo_excluir} não encontrada.")


def salvar_turmas():
    with open("turma.json", "w") as arquivo:
        for turma in lista_turmas:
            json.dump(turma, arquivo)
            arquivo.write("\n")


def cadastrar_turma():
    t_codigo = int(input("Digite o código da turma: "))
    cod_professor = int(input("Digite o código do professor: "))
    dados_turma = {
        "cod_turma": t_codigo
    }
    lista_turmas.append(dados_turma)
    print("Turma cadastrada com sucesso!")
    salvar_turmas()


def listar_turma():
    print("Lista de turmas:")
    for t_codigo in lista_turmas:
        print("Turma:", t_codigo['nome_disciplina'])


def editar_turma():
    codigo_editar = int(input("Digite o código da turma que deseja editar: "))
    for turma in lista_turmas:
        if turma["cod_turma"] == codigo_editar:
            novo_codigo = int(input("Digite o novo código da turma: "))
            turma["cod_turma"] = novo_codigo
            print(f"Turma com código {codigo_editar} editado com sucesso!")
            salvar_turmas()
            return
    print(f"Turma com código {codigo_editar} não encontrado.")


def excluir_turma():
    codigo_excluir = int(input("Digite o código da turma que deseja excluir: "))
    for turma in lista_turmas:
        if turma["cod_turma"] == codigo_excluir:
            lista_turmas.remove(turma)
            print(f"Turma com código {codigo_excluir} removido com sucesso!")
            return
    print(f"Turma com código {codigo_excluir} não encontrado.")


def salvar_matriculas():
    with open("matricula.json", "w") as arquivo:
        for matricula in lista_matriculas:
            json.dump(matricula, arquivo)
            arquivo.write("\n")


def cadastrar_matricula():
    if len(lista_estudantes) == 0:
        print("Ainda não há estudantes cadastrados")
        return
    codigo_estudante = int(input("Digite o código do estudante: "))
    codigo_turma = int(input("Digite o código da turma: "))

    dados_matricula = {
        "cod_estudante": codigo_estudante,
        "cod_turma": codigo_turma
    }
    lista_matriculas.append(dados_matricula)
    print("Matrícula cadastrada com sucesso!")
    salvar_matriculas()


def listar_matriculas():
    print("Lista de Matrículas:")
    for matricula in lista_matriculas:
        print("Código do Estudante:", matricula['cod_estudante'])
        print("Código da Turma:", matricula['cod_turma'])


def editar_matricula():
    if len(lista_estudantes) == 0:
        print("Ainda não há estudantes cadastrados")
        return
    codigo_matricula = int(input("Digite o código do estudante a que deseja editar: "))
    for matricula in lista_matriculas:
        if matricula["cod_estudante"] == codigo_matricula:
            novo_codigo = int(input("Digite o novo código da turma: "))
            matricula["cod_turma"] = novo_codigo
            print(f"Matrícula com código {codigo_matricula} editado com sucesso!")
            salvar_matriculas()
            return

    print(f"Matrícula com código {codigo_matricula} não encontrado.")


def excluir_matricula():
    codigo_excluir = int(input("Digite o código da matrícula que deseja excluir: "))
    for matricula in lista_matriculas:
        if matricula["cod_estudante"] == codigo_excluir:
            lista_matriculas.remove(matricula)
            print(f"Matrícula com código {codigo_excluir} removido com sucesso!")
            return
    print(f"Matrícula com código {codigo_excluir} não encontrado.")


def print_menu_secundario():
    print("[1]. Cadastrar\n[2]. Listar\n[3]. Editar\n[4]. Excluir\n[5]. Retornar ao menu incial")


# ler dados antes de iniciar aplicação
ler_dados_salvos()
while True:

    print("Bem vindo ao Portal do Estudante")
    print("[1]. Estudantes\n[2]. Professores\n[3]. Disciplinas\n[4]. Turmas \n[5]. Matrículas\n[0]. Sair")

    opcao = input("Selecione uma opção válida: ")
    if opcao == "1":
        print("Você escolheu a opção Estudantes")

        while True:
            print_menu_secundario()
            opcao_secundaria = input("Selecione uma opção válida: ")

            if opcao_secundaria == "1":
                cadastrar_estudante()
            elif opcao_secundaria == "2":
                listar_estudantes()
            elif opcao_secundaria == "3":
                editar_estudante()
            elif opcao_secundaria == "4":
                excluir_estudante()
            elif opcao_secundaria == "5":
                print("Você retornou ao MENU INICIAL")
                break
            else:
                print("Opção inválida!")
    elif opcao == "2":
        print("Você escolheu a opção Professores")

        while True:
            print_menu_secundario()
            opcao_secundaria = input("Selecione uma opção válida: ")

            if opcao_secundaria == "1":
                cadastrar_professor()
            elif opcao_secundaria == "2":
                listar_professor()
            elif opcao_secundaria == "3":
                editar_professor()
            elif opcao_secundaria == "4":
                excluir_professor()
            elif opcao_secundaria == "5":
                print("Você retornou ao MENU INICIAL")
                break
            else:
                print("Opção inválida!")
    elif opcao == "3":
        print("Você escolheu a opção Disciplinas")

        while True:
            print_menu_secundario()
            opcao_secundaria = input("Selecione uma opção válida: ")

            if opcao_secundaria == "1":
                cadastrar_disciplina()
            elif opcao_secundaria == "2":
                listar_disciplina()
            elif opcao_secundaria == "3":
                editar_disciplina()
            elif opcao_secundaria == "4":
                excluir_disciplina()
            elif opcao_secundaria == "5":
                print("Você retornou ao MENU INICIAL")
                break
            else:
                print("Opção inválida!")

    elif opcao == "4":
        print("Você escolheu a opção Turmas")

        while True:
            print_menu_secundario()
            opcao_secundaria = input("Selecione uma opção válida: ")

            if opcao_secundaria == "1":
                cadastrar_turma()
            elif opcao_secundaria == "2":
                listar_turma()
            elif opcao_secundaria == "3":
                editar_turma()
            elif opcao_secundaria == "4":
                excluir_turma()
            elif opcao_secundaria == "5":
                print("Você retornou ao MENU INICIAL")
                break
            else:
                print("Opção inválida!")
    elif opcao == "5":
        print("Você escolheu a opção Matrículas")
        while True:
            print_menu_secundario()
            opcao_secundaria = input("Selecione uma opção válida: ")

            if opcao_secundaria == "1":
                cadastrar_matricula()
            elif opcao_secundaria == "2":
                listar_matriculas()
            elif opcao_secundaria == "3":
                editar_matricula()
            elif opcao_secundaria == "4":
                excluir_matricula()
            elif opcao_secundaria == "5":
                print("Você retornou ao MENU INICIAL")
                break
            else:
                print("Opção inválida!")
    elif opcao == "0":
        print("Você escolheu a opção Sair")
        break
    else:
        print("Opção inválida!")
