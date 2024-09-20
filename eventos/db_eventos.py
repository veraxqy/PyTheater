import os
import pickle

eventos = {}

def carregar_eventos():
    if os.path.exists("eventos/eventos.pkl"):
        with open("eventos/eventos.pkl", "rb") as file:
            return pickle.load(file)
    else:
        return []

def salvar_eventos(eventos):
    with open("eventos/eventos.pkl", "wb") as file:
        pickle.dump(eventos, file)

# - TRECHO DE CÓDIGO BASEADO EM: https://replit.com/@PVeeeeeee/PyShoes