import os

# MENUS
import menus

# PRODUTORES
import produtores.cadastrar as cadastrar_prod
import produtores.exibir as exibir_prod
import produtores.alterar as alterar_prod
import produtores.excluir as excluir_prod

# TÉCNICOS
import tecnicos.cadastrar as cadastrar_tec
import tecnicos.exibir as exibir_tec
import tecnicos.alterar as alterar_tec
import tecnicos.excluir as excluir_tec

# EVENTOS
import eventos.cadastrar as cadastrar_evnt
import eventos.exibir as exibir_evnt
import eventos.alterar as alterar_evnt
import eventos.excluir as excluir_evnt

# RELATÓRIOS
import relatorios.produtores as listar_prod
import relatorios.tecnicos as listar_tec
import relatorios.eventos as listar_evnt

#####################################
######## PyTheater - Versão 6 #######
#####################################

# PROGRAMA PRINCIPAL
resp = ''
while resp != '0':
    executar_linha = True
    resp = menus.menu_principal()

    if resp == '1':
        opc_prod = ''
        while opc_prod != '0':
            opc_prod = menus.menu_produtor()
            print()
            if opc_prod == '1':
                cadastrar_prod.cadastrar_produtor()
            elif opc_prod == '2':
                exibir_prod.exibir_produtor()
            elif opc_prod == '3':
                alterar_prod.alterar_produtor()
            elif opc_prod == '4':
                excluir_prod.excluir_produtor()

    elif resp == '2':
        opc_tecnico = ''
        while opc_tecnico != '0':
            opc_tecnico = menus.menu_tecnico()
            print()
            if opc_tecnico == '1':
                cadastrar_tec.cadastrar_tecnico()
            elif opc_tecnico == '2':
                exibir_tec.exibir_tecnico()
            elif opc_tecnico == '3':
                alterar_tec.alterar_tecnico()
            elif opc_tecnico == '4':
                excluir_tec.excluir_tecnico()

    elif resp == '3':
        opc_evnt = ''
        while opc_evnt != '0':
            opc_evnt = menus.menu_evento()
            print()
            if opc_evnt == '1':
                cadastrar_evnt.cadastrar_evento()
            elif opc_evnt == '2':
                exibir_evnt.exibir_evento()
            elif opc_evnt == '3':
                alterar_evnt.alterar_evento()
            elif opc_evnt == '4':
                excluir_evnt.excluir_evento()

    elif resp == '4':
        opc_relt = ''
        while opc_relt != '0':
            opc_relt = menus.menu_relatorio()
            print()
            if opc_relt == '1':
                listar_prod.listar_produtores('', executar_linha)
            elif opc_relt == '2':
                listar_tec.listar_tecnicos('', executar_linha)
            elif opc_relt == '3':
                listar_evnt.listar_eventos('', executar_linha)

    elif resp == '5':
        menus.menu_informacoes()

os.system('clear')
print("#####################################")
print("##    Você encerrou o programa!    ##")
print("#######        Até logo!        #####")