# LISTAR TÉCNICOS
def listar_tecnicos(matricula, executar_linha):
    import os
    import tecnicos.db_tecnicos as db_tecnicos
    tecnicos = db_tecnicos.carregar_tecnicos()
    if executar_linha:
        os.system('clear')
        print()
        print("____--------------------------------------------------------------------------____")
        print("|  |                   Lista Geral de Técnicos Cadastrados                    |  |")
    print("|  |--------------------------------------------------------------------------|  |")
    print("|-----------|-----------------------------|--------------------|-----------------|")
    print("| Matrícula |            Nome             |       E-mail       |     Telefone    |")
    print("|-----------|-----------------------------|--------------------|-----------------|")
    if executar_linha:
        for matricula in tecnicos:
            print("| %-9s "%(matricula), end='')
            print("| %-27s "%(tecnicos[matricula][0]), end='')
            print("| %-18s "%(tecnicos[matricula][1]), end='')
            print("| %-15s |"%(tecnicos[matricula][2]))
    else:
        print("| %-9s "%(matricula), end='')
        print("| %-27s "%(tecnicos[matricula][0]), end='')
        print("| %-18s "%(tecnicos[matricula][1]), end='')
        print("| %-15s |"%(tecnicos[matricula][2]))
    print("|-----------|-----------------------------|--------------------|-----------------|")
    print()
    if executar_linha:
        input("Tecle <ENTER> para continuar...")