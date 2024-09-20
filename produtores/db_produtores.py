import os
import pickle

produtores = {}

def carregar_produtores():
    if os.path.exists("produtores/produtores.pkl"):
        with open("produtores/produtores.pkl", "rb") as file:
            return pickle.load(file)
    else:
        return []

def salvar_produtores(produtores):
    with open("produtores/produtores.pkl", "wb") as file:
        pickle.dump(produtores, file)

# - TRECHO DE CÓDIGO BASEADO EM: https://replit.com/@PVeeeeeee/PyShoes