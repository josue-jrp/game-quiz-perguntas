import os
db_users = os.getcwd() + r"\data-base\jogadores\usuarios.txt"

def create(username, passwd):
    with open(db_users, "r", encoding="utf-8")as file:
        conteudo = file.readlines()

        # abaixo serve para detectar se exite um usuário utilizando o mesmo username
        chaveamento = f"[#{username}##@"

        for item in conteudo:
            if chaveamento in item:
                return False
        else:

            with open(db_users, "a", encoding="utf-8")as arquivo:
                chaveamento = "\n" + chaveamento + f"{passwd}@@*0**]"
                arquivo.write(chaveamento)

                return True