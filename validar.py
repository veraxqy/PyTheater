import re

# VALIDAR DATA
def validar_data():
    from datetime import datetime
    while True:
        try:
            dia = int(input("[] -> Dia: "))
            mes = int(input("[] -> Mês: "))
            ano = int(input("[] -> Ano: "))
            data = datetime(ano, mes, dia)
            data_atual = datetime.now()
            if ano < data_atual.year:
                print("*! Data Inválida! Por favor tente novamente e digite um ano corretamente. !*")
            else:
                if mes < 1 or mes > 12:
                    print("*! Data Inválida! Por favor tente novamente, digite um mês válido. !*")
                elif mes == 2:
                    if (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0):
                        if 1 <= dia <= 29:
                            return data.date()
                        else:
                            print("*! Data Inválida! Por favor tente novamente, esse mês só possui 29 dias. !*")
                    else:
                        if 1 <= dia <= 28:
                            data = datetime(ano, mes, dia)
                            return data.date()
                        else:
                            print("*! Data Inválida! Por favor tente novamente, esse mês só possui 28 dias. !*")
                elif mes in {4, 6, 9, 11}:
                    if dia < 1 or dia > 30:
                        print("*! Data Inválida! Por favor tente novamente, só há 30 dias no mês. !*")
                    else:
                        return data.date()
                else:
                    if dia < 1 or dia > 31:
                        print("*! Data Inválida! Por favor tente novamente, só há 31 dias no mês. !*")

                    else:
                        return data.date()

        except ValueError:
            print("*! Data Inválida! Por favor tente novamente. !*")

# COMPARAR DATA
def comparar_data(data1, data2):
    return data2 >= data1

# VALIDAR MATRÍCULA
def validar_matricula():
    while True:
        try:
            matricula = int(input("[] -> Matrícula: "))
            break
        except:
            print("*! Matrícula Inválida! Por favor digite apenas números inteiros !*")
    return matricula

def validar_nome():
    while True:
        try:
            nome = input("[] -> Nome: ")
            nome = nome.replace(' ', '')
            if not nome.isalpha():
                print("*! Nome Inválido! Por favor digite apenas letras. !*")
            else:
                return nome
        except:
            return

def validar_email():
    regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b'
    while True:
        try:
            email = input("[] -> E-mail: ")
            if re.fullmatch(regex, email):
                return email
            else:
                print("*! E-mail Inválido! Por favor digite um e-mail válido. !*")
        except:
            return
# - TRECHO DE CÓDIGO BASEADO EM: https://www.usebouncer.com/pt-br/validacao-de-e-mail-em-python/

def validar_telefone():
    regex = '^([14689][0-9]|2[12478]|3([1-5]|[7-8])|5([13-5])|7[193-7])9[0-9]{8}$'
    while True:
        try:
            telefone = input("[] ->] Telefone: ")
            telefone = re.sub('[^0-9]', '', telefone)
            if re.match(regex, telefone):
                return telefone
            else:
                print("*! Telefone Inválido! Por favor digite um telefone válido. !*")
        except:
            return
# - TRECHO DE CÓDIGO BASEADO EM: https://andersonarruda.com.br/article/ValidandocelularbrasileirocomExpressaoRegular/9