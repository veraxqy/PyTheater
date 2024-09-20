# EXCLUIR PRODUTOR
def excluir_produtor():
    import os
    from validar import validar_matricula
    import produtores.db_produtores as db_produtores
    from relatorios.produtores import listar_produtores
    import eventos.db_eventos as db_eventos
    executar_linha = False
    produtores = db_produtores.carregar_produtores()
    eventos = db_eventos.carregar_eventos()
    os.system('clear')
    print()
    print("_____-------------------------------------------_____")
    print("|   |             Excluir Produtor              |   |")
    print("--------------________________________---------------")
    print()
    matricula = validar_matricula()

    if matricula in produtores:
        listar_produtores(matricula, executar_linha)
        for key, value in eventos.items():
            if value[2] == str(matricula):
                print()
                print("*! Produtor não pode ser excluído, pois está vinculado a um evento. !*")
            else:
                print()
                exc_produtor = input("[] -> Deseja excluir este Produtor? [S/N]: ")
                if exc_produtor == 's' or exc_produtor == 'S':
                    del produtores[matricula]
                    print("| Produtor Excluído com Sucesso! |")
                    db_produtores.salvar_produtores(produtores)
                else:
                    print("*! Exclusão não realizada. !*")
    else:
        print("*! Produtor não encontrado. !*")
    print()
    input("Tecle <ENTER> para continuar...")