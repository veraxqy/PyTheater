# ALTERAR EVENTO
def alterar_evento():
    import os
    from validar import validar_matricula, validar_data, comparar_data
    import eventos.db_eventos as db_eventos
    import produtores.db_produtores as db_produtores
    import tecnicos.db_tecnicos as db_tecnicos
    from relatorios.eventos import listar_eventos
    eventos = db_eventos.carregar_eventos()
    produtores = db_produtores.carregar_produtores()
    tecnicos = db_tecnicos.carregar_tecnicos()
    executar_linha = False
    os.system('clear')
    print()
    print("_____--------------------------------------------------_____")
    print("|   |             Alterar Dados do Evento              |   |")
    print("--------------______________________________----------------")
    print()
    matricula = validar_matricula()

    if matricula in eventos:
        os.system('clear')
        print("_____ - - - - - - - - - - - - - - - - - - - -_____")
        print("|   |----------------------------------------|   |")
        print("|   |     Qual dado você deseja alterar?     |   |")
        print("|   |----------------------------------------|   |")
        print("|   |    1 - Nome         |  4 - Técnico     |   |")
        print("|   |    2 - Categoria    |  5 - Data        |   |")
        print("|   |    3 - Produtor     |  0 - Sair        |   |")
        print("--------------------------------------------------")
        print()
        alterar = input("-> Escolha sua opção: ")

        if alterar == '1':
            nome = input("[] -> Novo Nome do Evento: ")
            eventos[matricula][0] = nome
        elif alterar == '2':
            categoria = input("[] -> Nova Categoria do Evento: ")
            eventos[matricula][1] = categoria
        elif alterar == '3':
            while True:
                matricula_produtor = input("[] -> Nova Matrícula do Produtor: ")
                matricula_produtor = int(matricula_produtor)
                if matricula_produtor in produtores:
                    eventos[matricula][2] = str(matricula_produtor)
                    break
                else:
                    print("*! Produtor não encontrado! Tente novamente. !*")
        elif alterar == '4':
            while True:
                matricula_tecnico = input("[] -> Nova Matrícula do Técnico: ")
                matricula_tecnico = int(matricula_tecnico)
                if matricula_tecnico in tecnicos:
                    eventos[matricula][3] = str(matricula_tecnico)
                    break
                else:
                    print("*! Técnico não encontrado! Tente novamente. !*")
        elif alterar == '5':
            while True:
                print("---------------------------------------------------")
                print("[] -> Data do Início do Evento: ")
                data_inicio = validar_data()
                print()
                print("___________________________________________________")
                print("[] -> Data do Fim do Evento: ")
                data_fim = validar_data()
                print()

                if comparar_data(data_inicio, data_fim):
                    eventos[matricula][4] = str(data_inicio)
                    eventos[matricula][5] = str(data_fim)
                    break
                else:
                    print("*! Data do Fim do Evento deve ser maior que ou igual a Data do Início do Evento. !*")
                    print()
                    input("Tecle <ENTER> para Tentar Novamente...")

        elif alterar == '0':
            print("[] Retornando ao Menu Principal...")
            return
        else:
            print("*! Opção Inválida. !*")
        db_eventos.salvar_eventos(eventos)
        listar_eventos(matricula, executar_linha)
        print("| Dados Alterados com Sucesso! |")
    else:
        print("*! Evento não encontrado. !*")
    print()
    input("Tecle <ENTER> para continuar...")