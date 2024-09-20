import os

# MENU PRINCIPAL
def menu_principal():
  os.system('clear')
  print("- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - ")
  print("""       ____       _____ _                _            
      |  _ \ _   __   _| |__   ___  __ _| |_ ___ _ __ 
      | |_) | | | || | | '_ \ / _ \/ _` | __/ _ \ '__|
      |  __/| |_| || | | | | |  __/ (_| | |_  __/ |   
      |_|    \__, ||_| |_| |_|\___|\__,_|\__\___|_|   
             |___/                                     """)
  print("_____ - - - - - - - - - - - - - - - - - - - - - - - - -_____")
  print("|   |--------------------------------------------------|   |")
  print("|   |      PyTheater: Sistema de Gestão para Teatro    |   |")
  print("|   |--------------------------------------------------|   |")
  print("|   |              1 - Módulo Produtor                 |   |")
  print("|   |              2 - Módulo Técnico                  |   |")
  print("|   |              3 - Módulo Evento                   |   |")
  print("|   |              4 - Módulo Relatório                |   |")
  print("|   |              5 - Módulo Informações              |   |")
  print("|   |              0 - Sair                            |   |")
  print("------------------------------------------------------------")
  print()
  resp = input("-> Escolha sua opção: ")
  return resp

#MENU PRODUTOR
def menu_produtor():
  os.system('clear')
  print("")
  print("_____ - - - - - - - - - - - - - - - - - - - -_____")
  print("|   |----------------------------------------|   |")
  print("|   |            Módulo Produtor             |   |")
  print("|   |----------------------------------------|   |")
  print("|   |     1 - Cadastrar Produtor             |   |")
  print("|   |     2 - Exibir Dados do Produtor       |   |")
  print("|   |     3 - Alterar Dados do Produtor      |   |")
  print("|   |     4 - Excluir Produtor               |   |")
  print("|   |     0 - Retornar ao Menu Principal     |   |")
  print("--------------------------------------------------")
  print()
  opc_prod = input("-> Escolha sua opção: ")
  return opc_prod

# MENU TÉCNICO
def menu_tecnico():
  os.system('clear')
  print("")
  print("_____ - - - - - - - - - - - - - - - - - - - -_____")
  print("|   |----------------------------------------|   |")
  print("|   |             Módulo Técnico             |   |")
  print("|   |----------------------------------------|   |")
  print("|   |     1 - Cadastrar Técnico              |   |")
  print("|   |     2 - Exibir Dados do Técnico        |   |")
  print("|   |     3 - Alterar Dados do Técnico       |   |")
  print("|   |     4 - Excluir Técnico                |   |")
  print("|   |     0 - Retornar ao Menu Principal     |   |")
  print("--------------------------------------------------")
  print()
  opc_tec = input("-> Escolha sua opção: ")
  return opc_tec

# MENU EVENTO
def menu_evento():
  os.system('clear')
  print("")
  print("_____ - - - - - - - - - - - - - - - - - - - -_____")
  print("|   |----------------------------------------|   |")
  print("|   |             Módulo Evento              |   |")
  print("|   |----------------------------------------|   |")
  print("|   |     1 - Cadastrar Evento               |   |")
  print("|   |     2 - Exibir Dados do Evento         |   |")
  print("|   |     3 - Alterar Dados do Evento        |   |")
  print("|   |     4 - Excluir Evento                 |   |")
  print("|   |     0 - Retornar ao Menu Principal     |   |")
  print("--------------------------------------------------")
  print()
  opc_evnt = input("-> Escolha sua opção: ")
  return opc_evnt

# MENU RELATÓRIO
def menu_relatorio():
  os.system('clear')
  print("")
  print("_____ - - - - - - - - - - - - - - - - - - - -_____")
  print("|   |----------------------------------------|   |")
  print("|   |            Módulo Relatório            |   |")
  print("|   |----------------------------------------|   |")
  print("|   |     1 - Lista Geral de Produtores      |   |")
  print("|   |     2 - Lista Geral de Técnicos        |   |")
  print("|   |     3 - Lista Geral de Eventos         |   |")
  print("|   |     0 - Retornar ao Menu Principal     |   |")
  print("--------------------------------------------------")
  print()
  opc_relt = input("-> Escolha sua opção: ")
  return opc_relt
  
# MENU INFORMAÇÕES
def menu_informacoes():
  os.system('clear')
  print()
  print("_____ - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - _____")
  print("|   |-------------------------------------------------------------------|   |")
  print("|   |                            INFORMAÇÕES                            |   |")
  print("|   |-------------------------------------------------------------------|   |")
  print("|   |       Esse projeto é um sistema de gerenciamento de teatro,       |   |")
  print("|   |       desenvolvido pensando no papel do gestor geral, pos-        |   |")
  print("|   |       sibilitando-o cadastrar as equipes que integram a           |   |")
  print("|   |       organização e os eventos que podem vir a acontecer          |   |")
  print("|   |       no local.                                                   |   |")
  print("|   |-------------------------------------------------------------------|   |")
  print("-----------------------------------------------------------------------------")
  print("|   |     Desenvolvedor:           |   |")
  print("|   |     Elder Bruno @veraxqy.ui  |   |")
  print("----------------------------------------")
  print()
  input("Tecle <ENTER> para continuar...")