# CADASTRAR TÉCNICO
def cadastrar_tecnico():
    import os
    from validar import validar_matricula, validar_nome, validar_email, validar_telefone
    import tecnicos.db_tecnicos as db_tecnicos
    from tecnicos.db_tecnicos import tecnicos
    from relatorios.tecnicos import listar_tecnicos
    tecnicos = db_tecnicos.carregar_tecnicos()
    executar_linha = False
    os.system('clear')
    print()
    print("_____------------------------------------------_____")
    print("|   |            Cadastrar Técnico             |   |")
    print("-------------__________________________-------------")
    print()
    nome = validar_nome()
    print()
    while True:
        matricula = validar_matricula()
        if matricula in tecnicos:
            print("*! Matrícula já cadastrada! Tente novamente. !*")
        else:
            break
    print()
    email = validar_email()
    print()
    telefone = validar_telefone()
    print()
    tecnicos[matricula] = [nome, email, telefone]
    print()
    db_tecnicos.salvar_tecnicos(tecnicos)
    listar_tecnicos(matricula, executar_linha)
    print()
    print("| Técnico Cadastrado com Sucesso! |")
    print()
    input("Tecle <ENTER> para continuar...")