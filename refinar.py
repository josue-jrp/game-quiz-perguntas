def refinar_conteudo(conteudo_bruto):
    encontrando__q__ = conteudo_bruto.find("#") + 2
    encontrando_fim_questao = conteudo_bruto.find('##') -1
    corpo_questao = conteudo_bruto[encontrando__q__:encontrando_fim_questao]
    alternativas = conteudo_bruto[conteudo_bruto.find("[")+1:conteudo_bruto.find("]")]
    alternativas = [item.strip().strip("'") for item in alternativas.replace("'", "").split(",")]
    al_correta = conteudo_bruto[conteudo_bruto.find("'rc':") + 6: -1].strip("'")
    return corpo_questao, alternativas, al_correta
