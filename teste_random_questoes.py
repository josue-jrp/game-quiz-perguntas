import os
from random import randint, shuffle

arquivo = os.getcwd() + r"\data-base\banco-questoes\com-alternativas\conhecimentos-gerais.txt"

def pegar_questao():
    with open(arquivo, "r", encoding="utf-8")as file:
        conteudo = file.read()
        questoes = conteudo.split("-\n")
        indice_escolhido = randint(0, len(questoes) - 1)
        questao_escolhida = questoes[indice_escolhido]

        return questao_escolhida
    
def separar_alternativas(questao):
    final_ask = questao.find("al->")
    pergunta = questao[:final_ask]
    alternativas = [item.replace("\n", "").strip() for item in questao[final_ask + 4:].split(",")]
    correta = ""
    
    for indice, item in enumerate(alternativas):
        if "*" in item:
            correta = item.replace("*","")
            alternativas[indice] = item.replace("*", "")

    shuffle(alternativas) # serve para embaralhar a lista de alternativas

    print(pergunta)
    for i in alternativas:
        print(f"X) {i}")
    
    print(f"\nresposta correta: {correta}\n\n")

    return pergunta, alternativas, correta

# pergunta sendo 'str' e alternativas é uma lista com 4 valores


