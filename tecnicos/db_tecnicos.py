import os
import pickle

tecnicos = {}

def carregar_tecnicos():
    if os.path.exists("tecnicos/tecnicos.pkl"):
        with open("tecnicos/tecnicos.pkl", "rb") as file:
            return pickle.load(file)
    else:
        return []

def salvar_tecnicos(tecnicos):
    with open("tecnicos/tecnicos.pkl", "wb") as file:
        pickle.dump(tecnicos, file)

# - TRECHO DE CÓDIGO BASEADO EM: https://replit.com/@PVeeeeeee/PyShoes