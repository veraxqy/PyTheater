# LISTAR EVENTOS
def listar_eventos(matricula, executar_linha):
    import os
    import eventos.db_eventos as db_eventos
    import produtores.db_produtores as db_produtores
    import tecnicos.db_tecnicos as db_tecnicos
    eventos = db_eventos.carregar_eventos()
    produtores = db_produtores.carregar_produtores()
    tecnicos = db_tecnicos.carregar_tecnicos()
    if executar_linha:
        os.system('clear')
        print()
        print("______---------------------------------------------------------------------------------------------------------------------------------------------______")
        print("|    |                                                    Lista Geral de Eventos Cadastrados                                                       |    |")
    print("|    |---------------------------------------------------------------------------------------------------------------------------------------------|    |")
    print("|------------|------------------------------------------|-----------------|----------------------|----------------------|---------------|---------------|")
    print("| Matrícula  |              Nome do Evento              |    Categoria    |       Produtor(a)    |        Técnico       |  Data Início  |    Data Fim   |")
    print("|------------|------------------------------------------|-----------------|----------------------|----------------------|---------------|---------------|")
    if executar_linha:
        
        for matricula in eventos:
            print("| %-10s "%(matricula), end='')
            print("| %-40s "%(eventos[matricula][0]), end='')
            print("| %-15s "%(eventos[matricula][1]), end='')
            matricula_produtor = int(eventos[matricula][2])
            matricula_tecnico = int(eventos[matricula][3])
            print("| %s - %-16s "%(matricula_produtor, produtores[matricula_produtor][0]), end='')
            print("| %s - %-16s "%(matricula_tecnico, tecnicos[matricula_tecnico][0]), end='')
            print("| %-13s "%(eventos[matricula][4]), end='')
            print("| %-13s |"%(eventos[matricula][5]))
    else:
        print("| %-10s "%(matricula), end='')
        print("| %-40s "%(eventos[matricula][0]), end='')
        print("| %-15s "%(eventos[matricula][1]), end='')
        matricula_produtor = int(eventos[matricula][2])
        matricula_tecnico = int(eventos[matricula][3])
        print("| %s - %-16s "%(matricula_produtor, produtores[matricula_produtor][0]), end='')
        print("| %s - %-16s "%(matricula_tecnico, tecnicos[matricula_tecnico][0]), end='')
        print("| %-13s "%(eventos[matricula][4]), end='')
        print("| %-13s |"%(eventos[matricula][5]))
    print("|------------|------------------------------------------|-----------------|----------------------|----------------------|---------------|---------------|")
    print()
    if executar_linha:
        input("Tecle <ENTER> para continuar...")