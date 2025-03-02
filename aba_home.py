from tkinter import *
from aba_main import Principal
import pegar_entradas
import time
import main
import os

class Home(Principal):
    def __init__(self):
        super().__init__()

        cinza = '#202020'
        escuro = '#101010'

        def retornar_pag_anterior(widget_atual, pag_anterior, botao=0):
            # o parametro dessa função conterá o widget que deverá ser destruído para que o usuário consiga voltar a home
            widget_atual.destroy()
            pag_anterior.pack(pady=40)
            if botao != 0:
                botao.destroy()
        
        def opcao_escolhida(opcao):

            self.frame_container_opcoes.pack_forget()
            frame_container_definicoes_de_opcao = Frame(self.frame_container_questao1, width=800, height=590, bg=cinza)
            frame_container_definicoes_de_opcao.pack(pady=40)
            frame_container_definicoes_de_opcao.propagate(False)
            botao_retornar_home = Button(frame_container_definicoes_de_opcao, width=5, text="voltar", bg="red", font=("Verdana bold", 18),fg=escuro, command=lambda:retornar_pag_anterior( frame_container_definicoes_de_opcao, self.frame_container_opcoes))
            botao_retornar_home.place(x=10, y=10)

            if opcao == "iniciar game":
                
                print("usuário iniciou um game.")
                frame_interno = Frame(frame_container_definicoes_de_opcao, width=400, height=400, bg=escuro)
                frame_interno.pack(pady=60)
                frame_interno.propagate(False) 

                def criar_conta():
                    frame_interno.pack_forget()
                    frame_container_credenciais = Frame(frame_container_definicoes_de_opcao, width=600, height=500, bg=escuro)
                    frame_container_credenciais.pack(pady=5)
                    frame_container_credenciais.propagate(False)

                    frame_titulo_criar_conta = Frame(frame_container_credenciais, width=570, height=30)
                    frame_titulo_criar_conta.pack(pady=20)
                    frame_titulo_criar_conta.propagate(False)

                    texto_titulo_criar_conta = Label(frame_titulo_criar_conta, font=("Verdana bold",20), text="Criar conta", fg="white", bg=escuro, width=100, height=30)
                    texto_titulo_criar_conta.pack()

                    # frame para organizar entrada e texto de 'username'
                    frame_username = Frame(frame_container_credenciais, width=570, height=70, bg=escuro)
                    frame_username.pack(pady=20)
                    frame_username.propagate(False)
                    texto_entrada_username = Label(frame_username, text="username:", font=("Verdana bold", 12), fg="white", bg=escuro)
                    texto_entrada_username.place(x=160)
                    entrada_username = Entry(frame_username, bg=cinza, font=("Verdana bold", 16), fg="white", background=escuro, insertbackground="white")
                    entrada_username.place(x=160, y=30)

                    # frame serve para organizar texto e entrada de password do usuário
                    frame_passwd = Frame(frame_container_credenciais, width=570, height=70, bg=escuro, background=escuro)
                    frame_passwd.pack()
                    frame_passwd.propagate(False)
                    texto_entrada_passwd = Label(frame_passwd, text="password", font=("Verdana bold", 12), fg="white", bg=escuro)
                    texto_entrada_passwd.place(x=160)
                    entrada_passwd = Entry(frame_passwd, bg=cinza, font=("Verdana bold", 16), fg="white", background=escuro, show="*", insertbackground="white")
                    entrada_passwd.place(x=160, y=30)
                    ver_ocultar_senha = Button(frame_passwd, text="ver", bg=escuro, fg="white", command= lambda: (entrada_passwd.configure(show=""), ver_ocultar_senha.configure(text="ocultar")) if entrada_passwd.cget("show") == "*" else (entrada_passwd.configure(show="*"), ver_ocultar_senha.configure(text="ver")))

                    ver_ocultar_senha.place(x=410, y=31)

                    re_frame_passwd = Frame(frame_container_credenciais, width=570, height=70, bg=escuro)
                    re_frame_passwd.pack(pady=5)
                    re_frame_passwd.propagate(False)

                    re_texto_entrada_passwd = Label(re_frame_passwd, text="re password", font=("Verdana bold", 12), fg="white", bg=escuro)
                    re_texto_entrada_passwd.place(x=160)

                    re_entrada_passwd = Entry(re_frame_passwd, bg=cinza, font=("Verdana bold", 16), fg="white", background=escuro, show="*", insertbackground="white")
                    re_entrada_passwd.place(x=160, y=30)

                    re_ver_ocultar_senha = Button(re_frame_passwd, text="ver", bg=escuro, fg="white", command= lambda: (re_entrada_passwd.configure(show=""), re_ver_ocultar_senha.configure(text="ocultar")) if re_entrada_passwd.cget("show") == "*" else (re_entrada_passwd.configure(show="*"), re_ver_ocultar_senha.configure(text="ver")))

                    re_ver_ocultar_senha.place(x=410, y=31)

                    # frame responsável por organizar o botao de 'fazer login'

                    def verificar():
                        retorno, status = pegar_entradas.pegar(entrada_username, entrada_passwd, re_entrada_passwd)

                        if status:
                            destruir = frame_container_credenciais.winfo_children()
                            for item in destruir:
                                item.destroy()

                            time.sleep(1)
                            frame_container_credenciais.configure(bg=cinza, height=300)
                            frame_container_credenciais.pack(pady=150)
                            texto_retorno_sucesso = Label(frame_container_credenciais, text=retorno, font=("Verdana bold", 20), fg="lightgreen", bg=cinza)
                            texto_retorno_sucesso.pack(pady=80)

                        else:
                            
                            # essa config serve para impedir que o widget de mensagem de erro de login se multiplique para o usuário
                            filhos_frame_container = frame_container_credenciais.winfo_children()   
                            if len(filhos_frame_container) > 5:
                                filhos_frame_container[-1].destroy()  
                                print("widget destruído!")
                        
                            print()

                            frame_container_credenciais.configure(height=550)
                            texto_retorno_insucesso = Label(frame_container_credenciais, text=retorno, fg="red", font=("Verdana bold", 16), bg=cinza)
                            texto_retorno_insucesso.pack()

                    frame_botao_criar = Frame(frame_container_credenciais, width=570, height=70, bg=escuro)
                    frame_botao_criar.pack(pady=10)
                    frame_botao_criar.propagate(False)

                    # a função associada a este botão está a algumas linhas acima...
                    botao_criar = Button(frame_botao_criar, text="criar", width=10 ,bg="green", fg="white", font=("Verdana bold",16), command=verificar)
                    botao_criar.pack(pady=15)

                    # caso esse botao seja apertado significa que o uusário quer retornar a página anterior
                    botao_retornar_frame_interno = Button(frame_container_definicoes_de_opcao, width=5, bg="red",font=("Verdana bold", 18), text="voltar", command=lambda:retornar_pag_anterior(frame_container_credenciais, frame_interno, botao_retornar_frame_interno))
                    botao_retornar_frame_interno.place(x=10, y=10)

                def fazer_login():
                    frame_interno.pack_forget()
                    frame_container_credenciais_login = Frame(frame_container_definicoes_de_opcao, width=600, height=380, bg=escuro)
                    frame_container_credenciais_login.pack(pady=65)
                    frame_container_credenciais_login.propagate(False)

                    frame_titulo_login = Frame(frame_container_credenciais_login, width=570, height=30)
                    frame_titulo_login.pack(pady=20)
                    frame_titulo_login.propagate(False)

                    texto_titulo_login = Label(frame_titulo_login, font=("Verdana bold",20), text="Login", fg="white", bg=escuro, width=100, height=30)
                    texto_titulo_login.pack()

                    # frame para organizar entrada e texto de 'username'
                    frame_username = Frame(frame_container_credenciais_login, width=570, height=70, bg=escuro)
                    frame_username.pack(pady=20)
                    frame_username.propagate(False)
                    texto_entrada_username = Label(frame_username, text="username:", font=("Verdana bold", 12), fg="white", bg=escuro)
                    texto_entrada_username.place(x=160)
                    entrada_username = Entry(frame_username, bg=cinza, font=("Verdana bold", 16), fg="white", background=escuro, insertbackground="white")
                    entrada_username.place(x=160, y=30)

                    # frame serve para organizar texto e entrada de password do usuário
                    frame_passwd = Frame(frame_container_credenciais_login, width=570, height=70, bg=escuro)
                    frame_passwd.pack()
                    frame_passwd.propagate(False)
                    texto_entrada_passwd = Label(frame_passwd, text="password", font=("Verdana bold", 12), fg="white", bg=escuro)
                    texto_entrada_passwd.place(x=160)
                    entrada_passwd = Entry(frame_passwd, bg=cinza, font=("Verdana bold", 16), fg="white", background=escuro, show="*", insertbackground="white")
                    entrada_passwd.place(x=160, y=30)
                    ver_ocultar_senha = Button(frame_passwd, text="ver", bg=escuro, fg="white", command= lambda: (entrada_passwd.configure(show=""), ver_ocultar_senha.configure(text="ocultar")) if entrada_passwd.cget("show") == "*" else (entrada_passwd.configure(show="*"), ver_ocultar_senha.configure(text="ver")))

                    ver_ocultar_senha.place(x=410, y=31)

                    # frame responsável por organizar o botao de 'fazer login'

                    def antes_pegar_entradas():
                        retorno, status = pegar_entradas.pegar(entrada_username, entrada_passwd)

                        if status:
                            destruir = frame_container_credenciais_login.winfo_children()
                            for item in destruir:
                                item.destroy()

                            frame_container_credenciais_login.configure(bg=cinza) # esse container será enviado para a função 'explicação' no outro modulo
                            texto_retorno_sucesso = Label(frame_container_credenciais_login, text=f"login efetuado com sucesso!\n", font=("Verdana bold", 12), fg="lightgreen", bg=cinza)
                            texto_retorno_sucesso.pack(pady=10)

                            frame_escolha_tema_pergunta = Frame(frame_container_credenciais_login, width=400, height=200, bg=cinza)
                            frame_escolha_tema_pergunta.pack(pady=20)
                            frame_escolha_tema_pergunta.propagate(False)

                            texto_escolha_o_tema = Label(frame_escolha_tema_pergunta, text="escolha o tema das perguntas", font=("Verdana", 19), fg="white", bg=cinza)
                            texto_escolha_o_tema.pack()

                            tema_escolhido = ""

                            def escolher_tema(tema):
                                global tema_escolhido
                                tema_escolhido = tema
                                print(f'\n\ninformações que serão passadas para a outra janela:\nnome jogador: {retorno["info_user"]["nome"]} \nrecorde do jogador: {retorno["info_user"]["recorde"]}\ntema escolhido: {tema_escolhido}')
                                #
                                resposta = main.aba_explicacao(self, frame_container_credenciais_login, retorno["info_user"]["nome"], retorno["info_user"]["recorde"], tema_escolhido)


                            botao_escolha_1 = Button(frame_escolha_tema_pergunta, bg=escuro, text="conhecimentos gerais", command= lambda: escolher_tema("CG"), fg="white", font=("Verdana", 14))
                            
                            botao_escolha_1.pack(side=LEFT)

                            botao_escolha_2 = Button(frame_escolha_tema_pergunta, bg=escuro, text="raciocinio lógico", command= lambda: escolher_tema("RL"), fg="white", font=("Verdana", 14))
                            botao_escolha_2.pack(side=RIGHT)


                            # abaixo, será feito uma chamada para outro mudulo que dará acesso ao usuário para a outra página... a página do jogo realmente. Essa chamada "enviará" os parametros contendo nome e pontuação recorde do usuário:
                            
                            # o primeiro parâmetro que vai ser passado é o desta janela atual ok
                            # o segundo parâmetro é o nome do jogador ok
                            # o terceiro é a maior pontuação do jogador ok
                            # o quarto é o tema da pergunta 

                            

                            #...

                        else:
                            
                            # essa config serve para impedir que o widget de mensagem de erro de login se multiplique para o usuário
                            filhos_frame_container = frame_container_credenciais_login.winfo_children()   
                            if len(filhos_frame_container) > 4:
                                filhos_frame_container[-1].destroy()  
                                print("widget destruído!")
                        
                            print()

                            frame_container_credenciais_login.configure(height=420)
                            texto_retorno_insucesso = Label(frame_container_credenciais_login, text=retorno, fg="red", font=("Verdana bold", 16), bg=cinza)
                            texto_retorno_insucesso.pack()

                    frame_botao_logar = Frame(frame_container_credenciais_login, width=570, height=70, bg=escuro)
                    frame_botao_logar.pack(pady=10)
                    frame_botao_logar.propagate(False)

                    # a função associada a este botão está a algumas linhas acima...
                    botao_logar = Button(frame_botao_logar, text="fazer login", bg="green", fg="white", font=("Verdana bold",16), command=antes_pegar_entradas)
                    botao_logar.pack(pady=15)

                    # caso esse botao seja apertado significa que o uusário quer retornar a página anterior
                    botao_retornar_frame_interno = Button(frame_container_definicoes_de_opcao, width=5, bg="red",font=("Verdana bold", 18), text="voltar", command=lambda:retornar_pag_anterior(frame_container_credenciais_login, frame_interno, botao_retornar_frame_interno))
                    botao_retornar_frame_interno.place(x=10, y=10)
                    
                botao_logar = Button(frame_interno, width=400, height=5, bg=cinza, fg="white", font=("Verdana bold", 19), text="Fazer login", command=fazer_login)
                botao_logar.pack(pady=19)

                botao_criar_perfil = Button(frame_interno, width=400, height=5, bg=cinza, fg="white", font=("Verdana bold", 19), text="Criar conta", command=criar_conta)
                botao_criar_perfil.pack()
                
            elif opcao == "adicionar questão":
                print("usuário quer adicionar uma questão")

            elif opcao == "visualizar recordes":
                print("usuário quer visualizar recordes")

        # esse Gui está sendo reaproveitado, por isso varios frames estão sendo destruidos    
        self.frame_interno_superior0.destroy()
        self.frame_interno_superior1.destroy()
        self.frame_indicativo_instrucoes_sistema.destroy()
        self.frame_indicativo_rodada.destroy()

        self.frame_conteiner_alternativas0.destroy()
        self.frame_conteiner_alternativas1.destroy()

        self.frame_externo1.configure(width=1060, height=750)
        self.frame_externo1.place(x=0, y=0)

        self.frame_corpo_questao.destroy()
        self.frame_indicativo_tema_pergunta.destroy()
        self.frame_indicativo_numero_pergunta.destroy()

        self.frame_container_questao0.configure(height=590)
        self.frame_container_questao1.configure(height=585)

        self.frame_interno_inferior0.configure(height=700)
        self.frame_interno_inferior1.configure(height=694)

        self.frame_container_bem_vindo0 = Frame(self.frame_indicativo_sistema1, width=500, height=50, bg=cinza)
        self.frame_container_bem_vindo0.pack(pady=10)
        self.frame_container_bem_vindo0.propagate(False)

        self.frame_container_bem_vindo1 = Frame(self.frame_container_bem_vindo0, width=496, height=42, bg=escuro)
        self.frame_container_bem_vindo1.place(x=2, y=2)
        self.frame_container_bem_vindo1.propagate(False)

        self.texto_bem_vindo = Label(self.frame_container_bem_vindo1, text="seja muito bem vindo ao quiz de perguntas e respostas", bg=escuro, fg="red", font=("Verdana bold", 15))
        self.texto_bem_vindo.pack(pady=10)

        self.frame_container_opcoes = Frame(self.frame_container_questao1, width=500, height=500, bg=cinza)
        self.frame_container_opcoes.pack(pady=40)
        self.frame_container_opcoes.propagate(False)

        self.frame_opcao_iniciar_game = Frame(self.frame_container_opcoes, width=480, height=70, bg=escuro)
        self.frame_opcao_iniciar_game.pack(pady=8)
        self.frame_opcao_iniciar_game.propagate(False)

        self.botao_opcao_iniciar_game = Button(self.frame_opcao_iniciar_game, width=480, height=70, fg="white", bg=escuro, text="iniciar game", font=("Verdana bold",19), command=lambda:opcao_escolhida(self.botao_opcao_iniciar_game.cget("text")))
        self.botao_opcao_iniciar_game.pack()

        self.frame_opcao_adicionar_questao = Frame(self.frame_container_opcoes, width=480, height=70, bg=escuro )
        self.frame_opcao_adicionar_questao.pack()
        self.frame_opcao_adicionar_questao.propagate(False)

        self.botao_adicionar_questao = Button(self.frame_opcao_adicionar_questao, width=480, height=70, fg="white", bg=escuro, text="adicionar questão", font=("Verdana bold", 19), command=lambda:opcao_escolhida(self.botao_adicionar_questao.cget("text")))
        self.botao_adicionar_questao.pack()

        self.frame_opcao_visualizar_recordes = Frame(self.frame_container_opcoes, width=480, height=70, bg=escuro)
        self.frame_opcao_visualizar_recordes.pack(pady=8)
        self.frame_opcao_visualizar_recordes.propagate(False)

        self.botao_opcao_visualizar_recordes = Button(self.frame_opcao_visualizar_recordes, width=480, height=70, fg="white", bg=escuro, text="visualizar recordes", font=("Verdana bold", 19), command=lambda:opcao_escolhida(self.botao_opcao_visualizar_recordes.cget("text")))
        self.botao_opcao_visualizar_recordes.pack()      

home = Home()

home.mainloop()