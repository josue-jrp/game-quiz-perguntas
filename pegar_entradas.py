import login
import create_user

def pegar(entrada_username, entrada_passwd, re_entrada_username=None):

    valor_username = entrada_username.get()
    valor_passwd = entrada_passwd.get()

    valor_username.strip()

    # verificação de campos vazios
    if valor_username == " " or len(valor_username) == 0 or valor_passwd == " " or len(valor_passwd) == 0:
        print()
        return "por favor, preencha os campos corretamente!", False
    
    else:
        if re_entrada_username == None:
            print("efetuando tentativa de login...")
            retorno, status = login.logar(valor_username, valor_passwd)

            if status:
                print(retorno["resposta_sys"])
                return retorno, status

            else:
                print(retorno)
                return retorno, status

        else:
            # se cair nesse else significa que essa função foi chamada com o parâmetro 're_entrada_username' diferente de None (ou seja, é para criar um usuário)
            valor_re_passwd = re_entrada_username.get()

            print("efetuando tentativa de criação de usuário...")
            if valor_passwd != valor_re_passwd:
                print("as senhas informadas apresentam divergências!")
                return "as senhas informadas apresentam divergências!", False
            
            else:
                status = create_user.create(valor_username, valor_passwd)

                if status:
                    return "parabéns, sua conta foi registrada com sucesso!", True
                else:
                    return "username já está cadastrado no sistema!", False
            
    
            