# ALTERAR PRODUTOR
def alterar_produtor():
    import os
    from validar import validar_matricula
    import produtores.db_produtores as db_produtores
    from relatorios.produtores import listar_produtores
    produtores = db_produtores.carregar_produtores()
    executar_linha = False
    os.system('clear')
    print()
    print("_____--------------------------------------------------_____")
    print("|   |            Alterar Dados do Produtor             |   |")
    print("--------------______________________________----------------")
    print()
    matricula = validar_matricula()
    
    if matricula in produtores:
        os.system('clear')
        listar_produtores(matricula, executar_linha)
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
            nome = input("[] -> Novo Nome do Produtor: ")
            produtores[matricula][0] = nome
        elif alterar == '2':
            email = input("[] -> Novo E-mail do Produtor: ")
            produtores[matricula][1] = email
        elif alterar == '3':
            telefone = input("[] -> Novo Telefone do Produtor: ")
            produtores[matricula][2] = telefone
        elif alterar == '0':
            print("[] Retornando ao Menu Principal...")
            return
        else:
            print("*! Opção Inválida !*")
        db_produtores.salvar_produtores(produtores)
        listar_produtores(matricula, executar_linha)
        print("| Dados Alterados com Sucesso! |")
    else:
        print("*! Produtor não encontrado !*")
    print()
    input("Tecle <ENTER> para continuar...")