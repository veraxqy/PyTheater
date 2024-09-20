# EXIBIR PRODUTOR
def exibir_produtor():
    import os
    from validar import validar_matricula
    import produtores.db_produtores as db_produtores
    from relatorios.produtores import listar_produtores
    executar_linha = False
    produtores = db_produtores.carregar_produtores()
    os.system('clear')
    print()
    print("_____-------------------------------------------_____")
    print("|   |            Dados do Produtor              |   |")
    print("--------------_______________________---------------")
    print()
    matricula = validar_matricula()

    if matricula in produtores:
        listar_produtores(matricula, executar_linha)
    else:
        print("*! Produtor não encontrado. !*")
    print()
    input("Tecle <ENTER> para continuar...")