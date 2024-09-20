# EXCLUIR TÉCNICO
def excluir_tecnico():
    import os
    from validar import validar_matricula
    import tecnicos.db_tecnicos as db_tecnicos
    from relatorios.tecnicos import listar_tecnicos
    import eventos.db_eventos as db_eventos
    executar_linha = False
    tecnicos = db_tecnicos.carregar_tecnicos()
    eventos = db_eventos.carregar_eventos()
    os.system('clear')
    print()
    print("_____------------------------------------------_____")
    print("|   |             Excluir Técnico              |   |")
    print("--------------______________________----------------")
    print()
    matricula = validar_matricula()
    
    if matricula in tecnicos:
        listar_tecnicos(matricula, executar_linha)
        for key, value in eventos.items():
            if value[3] == str(matricula):
                print()
                print("*! Técnico não pode ser excluído, pois está vinculado a um evento. !*")
            else:
                print()
                exc_tecnico = input("[] -> Deseja excluir este Técnico? [S/N]: ")
                if exc_tecnico == 's' or exc_tecnico == 'S':
                    del tecnicos[matricula]
                    print("| Técnico Excluído com Sucesso! |")
                    db_tecnicos.salvar_tecnicos(tecnicos)
                else:
                    print("*! Exclusão não realizada. !*")
    else:
        print("*! Técnico não encontrado. !*")
    print()
    input("Tecle <ENTER> para continuar...")