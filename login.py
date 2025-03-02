import os
arquivo_bd = os.getcwd() + r"\data-base\jogadores\usuarios.txt"


def logar(username, passwd):
    print(username, passwd)

    chaveamento = f"#{username.strip()}##@{passwd.strip()}@@"

    with open(arquivo_bd, "r", encoding="utf-8")as file:
        conteudo = file.readlines()
        print(conteudo)

        for item in conteudo:
            if chaveamento in item:
                print("usuário está cadastrado no sistema!")
                # procurando os pontos no item para pegar o valor
                pontos = item.find("*")
                recorde = item[pontos:].replace("*", "").replace("]", "").replace("\n", "")

                # o retorno será um dicionário e uma boleano
                retorno = {"resposta_sys":"usuário está cadastrado no sistema", "info_user": {"nome":username, "recorde":recorde}}
                return retorno, True
                
        else:
            print("usuário não está cadastrado no sistema!")
            return "não foi possível conectar com as credenciais inseridas!", False



