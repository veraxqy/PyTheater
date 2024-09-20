# LISTAR PRODUTORES
def listar_produtores(matricula, executar_linha):
    import os
    import produtores.db_produtores as db_produtores
    produtores = db_produtores.carregar_produtores()
    if executar_linha:
        os.system('clear')
        print()
        print("____--------------------------------------------------------------------------____")
        print("|  |                  Lista Geral de Produtores Cadastrados                   |  |")
    print("|  |--------------------------------------------------------------------------|  |")
    print("|-----------|-----------------------------|--------------------|-----------------|")
    print("| Matrícula |            Nome             |       E-mail       |     Telefone    |")
    print("|-----------|-----------------------------|--------------------|-----------------|")
    if executar_linha:
        for matricula in produtores:
            print("| %-9s "%(matricula), end='')
            print("| %-27s "%(produtores[matricula][0]), end='')
            print("| %-18s "%(produtores[matricula][1]), end='')
            print("| %-15s |"%(produtores[matricula][2]))
    else:
        print("| %-9s "%(matricula), end='')
        print("| %-27s "%(produtores[matricula][0]), end='')
        print("| %-18s "%(produtores[matricula][1]), end='')
        print("| %-15s |"%(produtores[matricula][2]))
    print("|-----------|-----------------------------|--------------------|-----------------|")
    print()
    if executar_linha:
        input("Tecle <ENTER> para continuar...")