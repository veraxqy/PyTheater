# ALTERAR TÉCNICO
def alterar_tecnico():
    import os
    from validar import validar_matricula
    import tecnicos.db_tecnicos as db_tecnicos
    from relatorios.tecnicos import listar_tecnicos
    tecnicos = db_tecnicos.carregar_tecnicos()
    executar_linha = False
    os.system('clear')
    print()
    print("_____--------------------------------------------------_____")
    print("|   |            Alterar Dados do Técnico              |   |")
    print("--------------______________________________----------------")
    print()
    matricula = validar_matricula()

    if matricula in tecnicos:
        os.system('clear')
        print("_____ - - - - - - - - - - - - - - - - - - - -_____")
        print("|   |----------------------------------------|   |")
        print("|   |     Qual dado você deseja alterar?     |   |")
        print("|   |----------------------------------------|   |")
        print("|   |  1 - Nome   2 - E-mail   3 - Telefone  |   |")
        print("|   |                0 - Sair                |   |")
        print("--------------------------------------------------")
        print()
        alterar = input("-> Escolha sua opção: ")

        if alterar == '1':
            nome = input("[] -> Novo Nome do Técnico: ")
            tecnicos[matricula][0] = nome
        elif alterar == '2':
            email = input("[] -> Novo E-mail do Técnico: ")
            tecnicos[matricula][1] = email
        elif alterar == '3':
            telefone = input("[] -> Novo Telefone do Técnico: ")
            tecnicos[matricula][2] = telefone
        elif alterar == '0':
            print("[] Retornando ao Menu Principal...")
            return
        else:
            print("*! Opção Inválida !*")
        db_tecnicos.salvar_tecnicos(tecnicos)
        listar_tecnicos(matricula, executar_linha)
        print("| Dados Alterados com Sucesso! |")
    else:
        print("*! Técnico não encontrado !*")
    print()
    input("Tecle <ENTER> para continuar...")