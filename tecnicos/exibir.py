# EXIBIR TÉCNICO
def exibir_tecnico():
    import os
    from validar import validar_matricula
    import tecnicos.db_tecnicos as db_tecnicos
    from relatorios.tecnicos import listar_tecnicos
    executar_linha = False
    tecnicos = db_tecnicos.carregar_tecnicos()
    os.system('clear')
    print()
    print("_____-----------------------------------------_____")
    print("|   |            Dados do Técnico             |   |")
    print("--------------______________________---------------")
    print()
    matricula = validar_matricula()

    if matricula in tecnicos:
        listar_tecnicos(matricula, executar_linha)
    else:
        print("*! Técnico não encontrado. !*")

    print()
    input("Tecle <ENTER> para continuar...")