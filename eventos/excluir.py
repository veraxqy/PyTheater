# EXCLUIR EVENTO
def excluir_evento():
    import os
    from validar import validar_matricula
    import eventos.db_eventos as db_eventos
    from relatorios.eventos import listar_eventos
    executar_linha = False
    eventos = db_eventos.carregar_eventos()
    os.system('clear')
    print()
    print("_____-----------------------------------------_____")
    print("|   |             Excluir Evento              |   |")
    print("--------------______________________---------------")
    print()
    matricula = validar_matricula()
    
    if matricula in eventos:
        listar_eventos(matricula, executar_linha)
        print()
        exc_evento = input("[] -> Deseja excluir este Evento? [S/N]: ")
        if exc_evento == 's' or exc_evento == 'S':
            del eventos[matricula]
            db_eventos.salvar_eventos(eventos)
            print("| Evento Excluído com Sucesso! |")
        else:
            print("*! Exclusão não realizada. !*")
    else:
        print("*! Evento não encontrado !*")
    input("Tecle <ENTER> para continuar...")