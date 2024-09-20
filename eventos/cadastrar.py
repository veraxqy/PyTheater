# CADASTRAR EVENTO
def cadastrar_evento():
    import os
    from validar import validar_matricula, validar_data, comparar_data
    import eventos.db_eventos as db_eventos
    import produtores.db_produtores as db_produtores
    import tecnicos.db_tecnicos as db_tecnicos
    from relatorios.eventos import listar_eventos
    from relatorios.produtores import listar_produtores
    from relatorios.tecnicos import listar_tecnicos
    from eventos.db_eventos import eventos
    eventos = db_eventos.carregar_eventos()
    produtores = db_produtores.carregar_produtores()
    tecnicos = db_tecnicos.carregar_tecnicos()
    executar_linha = True
    os.system('clear')
    print()
    print("_____------------------------------------------_____")
    print("|   |            Cadastrar Evento              |   |")
    print("-------------__________________________-------------")
    print()
    nome = input("[] -> Nome do Evento: ")
    print()
    categoria = input("[] -> Categoria: ")
    print()
    while True:
        matricula = validar_matricula()
        if matricula in eventos:
            print("*! Matrícula já cadastrada! Tente novamente. !*")
        else:
            break
    print()
    listar_produtores('', executar_linha)
    while True:
        matricula_produtor = validar_matricula()
        if matricula_produtor not in produtores:
            print("*! Produtor não encontrado! Por favor tente novamente. !*")
        else:
            break
    print()
    listar_tecnicos('', executar_linha)
    while True:
        matricula_tecnico = validar_matricula()
        if matricula_tecnico not in tecnicos:
            print("*! Técnico não encontrado! Por favor tente novamente. !*")
        else:
            break
    print()

    while True:
        os.system('clear')
        print("_____------------------------------------------_____")
        print("|   |            Cadastrar Evento              |   |")
        print("-------------__________________________-------------")
        print("[] Nome: %s    [] Categoria: %s"%(nome, categoria))
        print("[] Matrícula do Evento: %s"%(matricula))
        print("[] Produtor: %s    [] Técnico: %s"%(produtores[matricula_produtor][0],     tecnicos[matricula_tecnico][0]))
        print("---------------------------------------------------")
        print("[] -> Data do Início do Evento: ")
        data_inicio = validar_data()
        print()
        print("___________________________________________________")
        print("[] -> Data do Fim do Evento: ")
        data_fim = validar_data()
        print()

        if comparar_data(data_inicio, data_fim):
            break
        else:
            print("*! Data do Fim do Evento deve ser maior que ou igual a Data do Início do Evento. !*")
            print()
            input("Tecle <ENTER> para Tentar Novamente...")

    print()
    eventos[matricula] = [nome, categoria, str(matricula_produtor), str(matricula_tecnico), str(data_inicio),     str(data_fim)]
    print()
    db_eventos.salvar_eventos(eventos)
    listar_eventos(matricula, executar_linha)
    print()
    print("| Evento Cadastrado com Sucesso! |")
    print()
    input("Tecle <ENTER> para continuar...")