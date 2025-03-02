from tkinter import *

def botao_confirma(alternativas):
    for chave, valor in alternativas.items():

        if valor:
            print("alternativa marcada: ", chave.cget("text"))
            return True, chave.cget("text").strip()

    else:
        print("\n\nnenhum item foi marcado!")
        return False, " "
    

#def botao_pular_questao():

def verificar(palpite, rc):
    if palpite.strip() == rc:
        return True
    else:
        return False