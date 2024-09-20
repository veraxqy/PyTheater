# CADASTRAR PRODUTOR
def cadastrar_produtor():
    import os
    from validar import validar_matricula, validar_nome, validar_email, validar_telefone
    import produtores.db_produtores as db_produtores
    from produtores.db_produtores import produtores
    from relatorios.produtores import listar_produtores
    produtores = db_produtores.carregar_produtores()
    executar_linha = False
    os.system('clear')
    print()
    print("_____------------------------------------------_____")
    print("|   |            Cadastrar Produtor            |   |")
    print("-------------__________________________-------------")
    print()
    nome = validar_nome()
    print()
    while True:
        matricula = validar_matricula()
        if matricula in produtores:
            print("*! Matrícula já cadastrada! Tente novamente. !*")
        else:
            break
    print()
    email = validar_email()
    print()
    telefone = validar_telefone()
    print()
    produtores[matricula] = [nome, email, telefone]
    print()
    db_produtores.salvar_produtores(produtores)
    listar_produtores(matricula, executar_linha)
    print()
    print("| Produtor Cadastrado com Sucesso! |")
    print()
    input("Tecle <ENTER> para continuar...")