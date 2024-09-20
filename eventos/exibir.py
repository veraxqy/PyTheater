# EXIBIR EVENTO
def exibir_evento():
    import os
    from validar import validar_matricula
    import eventos.db_eventos as db_eventos
    from relatorios.eventos import listar_eventos
    executar_linha = False
    eventos = db_eventos.carregar_eventos()
    os.system('clear')
    print()
    print("_____----------------------------------------_____")
    print("|   |            Dados do Evento             |   |")
    print("--------------_____________________---------------")
    print()
    matricula = validar_matricula()

    if matricula in eventos:
        listar_eventos(matricula, executar_linha)
    else:
        print("*! Evento não encontrado. !*")

    print()
    input("Tecle <ENTER> para continuar...")