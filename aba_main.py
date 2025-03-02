from tkinter import *

class Principal(Tk):
    def __init__(self):
        super().__init__()

        #cores em hexadecimal
        cinza = '#202020'
        escuro = '#101010'

        self.geometry("1080x800")
        self.title("quiz perguntas e respostas")
        self.configure(bg="#101010")

        # sempre pegar daqui um frame com 'bordas' finas
        self.frame_externo0 = Frame(self, width=1060, height=750, bg=cinza)
        self.frame_externo0.pack()
        self.frame_externo0.propagate(False)
        self.frame_externo1 = Frame(self.frame_externo0, width=1056, height=746, bg=escuro)
        self.frame_externo1.place(x=2, y=2)
        self.frame_externo1.propagate(False)
        #-----

        # frame principal superior
        self.frame_interno_superior0 = Frame(self.frame_externo1, width=1028, height=176, bg=cinza)
        self.frame_interno_superior0.pack(pady=5)
        self.frame_interno_superior0.propagate(False)
        self.frame_interno_superior1 = Frame(self.frame_interno_superior0, width=1024, height=169, bg=escuro)
        self.frame_interno_superior1.place(x=2, y=4)
        #---

        self.frame_pontuacao0 = Frame(self.frame_interno_superior1, bg=cinza, width=300, height=140)
        self.frame_pontuacao0.place(x=15, y=14)
        self.frame_pontuacao0.propagate(False)

        self.frame_pontuacao1 = Frame(self.frame_pontuacao0, width=296, bg=escuro, height=136)
        self.frame_pontuacao1.place(x=2, y=2)
        self.frame_pontuacao1.propagate(False)

        self.frame_player1 = Frame(self.frame_pontuacao1, width=280, bg=cinza, height=58)
        self.frame_player1.pack(pady=7)
        self.frame_player1.propagate(False)

        self.texto_player1 = Label(self.frame_player1, text="jogador 1 = X", bg=cinza, fg="gray", font=("Verdana bold", 16))
        self.texto_player1.pack(pady=12)

        self.frame_player2 = Frame(self.frame_pontuacao1, width=280, bg=cinza, height=58)
        self.frame_player2.pack()
        self.frame_player2.propagate(False)

        self.texto_player2 = Label(self.frame_player2, text="jogador 2 = X", bg=cinza, fg="gray", font=("Verdana bold", 16))
        self.texto_player2.pack(pady=12)

        self.frame_container_contador0 = Frame(self.frame_interno_superior1, bg=cinza, width=300, height=80)
        self.frame_container_contador0.place(x=710, y=14)
        self.frame_container_contador0.propagate(False)

        self.frame_container_contador1 = Frame(self.frame_container_contador0,  bg=escuro, width=296, height=76)
        self.frame_container_contador1.place(x=2, y=2)
        self.frame_container_contador1.propagate(False)

        self.frame_contador = Frame(self.frame_container_contador1, bg=cinza, width=266, height=50)
        self.frame_contador.pack(pady=14)
        self.frame_contador.propagate(False)

        self.texto_contador = Label(self.frame_contador, text="5:00:00", fg="red", bg=cinza, font=("Verdana bold", 17))
        self.texto_contador.pack(pady=8)

        # frame principal inferior
        self.frame_interno_inferior0 = Frame(self.frame_externo1, width=1028, height=550, bg=cinza)
        self.frame_interno_inferior0.pack(pady=2)
        self.frame_interno_inferior0.propagate(False)
        self.frame_interno_inferior1 = Frame(self.frame_interno_inferior0, width=1024, height=544, bg=escuro)
        self.frame_interno_inferior1.place(x=2, y=3)
        self.frame_interno_inferior1.propagate(False)
        #---

        self.frame_indicativo_sistema0 = Frame(self.frame_interno_inferior1, width=1012, height=70, bg=cinza)
        self.frame_indicativo_sistema0.pack(pady=8)
        self.frame_indicativo_sistema0.propagate(False)

        self.frame_indicativo_sistema1 = Frame(self.frame_indicativo_sistema0, width=1008, height=70, bg=escuro)
        self.frame_indicativo_sistema1.pack(pady=2)
        self.frame_indicativo_sistema1.propagate(False)

        self.frame_indicativo_rodada = Frame(self.frame_indicativo_sistema1, width=250, height=50, bg=cinza)
        self.frame_indicativo_rodada.pack(side=LEFT, padx=10)
        self.frame_indicativo_rodada.propagate(False)

        self.texto_indicativo_rodada = Label(self.frame_indicativo_rodada, bg=cinza, fg="gray", font=("Verdana bold", 20), text="rodada numero X")
        self.texto_indicativo_rodada.pack(pady=5)

        self.frame_indicativo_instrucoes_sistema = Frame(self.frame_indicativo_sistema1, width=730, height=50, bg=cinza)
        self.frame_indicativo_instrucoes_sistema.pack(side=RIGHT, padx=10)
        self.frame_indicativo_instrucoes_sistema.propagate(False)

        self.texto_indicativo_instrucoes_sistema = Label(self.frame_indicativo_instrucoes_sistema, bg=cinza, fg="red", font=("Verdana bold", 14), text="algum texto para instruir o usuário")
        self.texto_indicativo_instrucoes_sistema.pack(side=LEFT, padx=10, pady=8)

        self.frame_container_questao0 = Frame(self.frame_interno_inferior1, width=1012, height=220, bg=cinza)
        self.frame_container_questao0.pack(pady=5)
        self.frame_container_questao0.propagate(False)

        self.frame_container_questao1 = Frame(self.frame_container_questao0, width=1008, height=216, bg=escuro)
        self.frame_container_questao1.pack(pady=2)
        self.frame_container_questao1.propagate(False)

        self.frame_indicativo_tema_pergunta = Frame(self.frame_container_questao1, width=400, height=30, bg=cinza)
        self.frame_indicativo_tema_pergunta.place(x=10, y=10)
        self.frame_indicativo_tema_pergunta.propagate(False)

        self.texto_indicativo_tema_pergunta = Label(self.frame_indicativo_tema_pergunta, text="tema da pergunta é X", font=("Verdana Bold", 14), bg=cinza, fg="gray")
        self.texto_indicativo_tema_pergunta.pack(pady=5)

        self.frame_indicativo_numero_pergunta = Frame(self.frame_container_questao1, width=200, height=30, bg=cinza)
        self.frame_indicativo_numero_pergunta.place(x=790, y=10)
        self.frame_indicativo_numero_pergunta.propagate(False)

        self.texto_indicativo_numero_pergunta = Label(self.frame_indicativo_numero_pergunta, text="pergunta numero X", font=("Verdana Bold", 14), bg=cinza, fg="gray")
        self.texto_indicativo_numero_pergunta.pack(pady=5)

        self.frame_corpo_questao = Frame(self.frame_container_questao1, width=980, height=145, bg=cinza)
        self.frame_corpo_questao.place(x=14, y=55)
        self.frame_corpo_questao.propagate(False)

        texto_teste = "Lorem Ipsum é um texto padrão em latim usado para preencher espaços de texto em publicações, como revistas, jornais e sites. Ele é usado para testar e ajustar aspectos visuais, como a tipografia, a formatação e o layout, antes de utilizar conteúdo real."

        self.texto_corpo_quetao = Label(self.frame_corpo_questao, bg=cinza, fg="gray", font=("Verdana bold", 15), wraplength=960, justify=LEFT, text=texto_teste)
        self.texto_corpo_quetao.place(x=10, y=10)

        self.frame_conteiner_alternativas0 = Frame(self.frame_interno_inferior1, width=1012, height=210, bg=cinza)
        self.frame_conteiner_alternativas0.pack(pady=4)
        self.frame_conteiner_alternativas0.propagate(False)

        self.frame_conteiner_alternativas1 = Frame(self.frame_conteiner_alternativas0, width=1008, height=206, bg=escuro)
        self.frame_conteiner_alternativas1.pack(pady=2)
        self.frame_conteiner_alternativas1.propagate(False)

        self.frame_alternativas = Frame(self.frame_conteiner_alternativas1, width=980, height=185, bg=cinza)
        self.frame_alternativas.place(x=14, y=10)
        self.frame_alternativas.propagate(False)

        self.alternativa_correta = None
        self.resultado_questao = []

        # organizando funcionalidades de Checkbuttons de alternativas
        def selecionar_cb0():
            if self.cb_0.get():
                self.cb_1.set(0)
                self.cb_2.set(0)
                self.cb_3.set(0)

        def selecionar_cb1():
            if self.cb_1.get():
                self.cb_0.set(0)
                self.cb_2.set(0)
                self.cb_3.set(0)

        def selecionar_cb2():
            if self.cb_2.get():
                self.cb_0.set(0)
                self.cb_1.set(0)
                self.cb_3.set(0)

        def selecionar_cb3():
            if self.cb_3.get():
                self.cb_0.set(0)
                self.cb_1.set(0)
                self.cb_2.set(0)

        self.cb_0 = IntVar()
        self.cb_1 = IntVar()
        self.cb_2 = IntVar()
        self.cb_3 = IntVar()

        self.alternativa0 = Checkbutton(self.frame_alternativas, text="opção 1", variable=self.cb_0, command=selecionar_cb0, bg=cinza, font=("Verdana bold", 14), fg="gray")
        self.alternativa0.place(x=10, y=15)

        self.alternativa1 = Checkbutton(self.frame_alternativas, text="opção 2", variable=self.cb_1, command=selecionar_cb1, bg=cinza, font=("Verdana bold", 14), fg="gray")
        self.alternativa1.place(x=10, y=50)

        self.alternativa2 = Checkbutton(self.frame_alternativas, text="opção 3", variable=self.cb_2, command=selecionar_cb2, bg=cinza, font=("Verdana bold", 14), fg="gray")
        self.alternativa2.place(x=10, y=85)

        self.alternativa3 = Checkbutton(self.frame_alternativas, text="opção 4", variable=self.cb_3, command=selecionar_cb3, bg=cinza, font=("Verdana bold", 14), fg="gray")
        self.alternativa3.place(x=10, y=120)

        def mostrar_valor(valor):
            print(valor)
               
        self.botao_confirma = Button(self.frame_alternativas, bg="green", text="confirmar alternativa", fg="white", font=("Verdana bold",14), command=lambda: mostrar_valor([item for item in [self.cb_0.get(), self.cb_1.get(), self.cb_2.get(), self.cb_3.get()]]))
        self.botao_confirma.place(x=780 ,y=15)

        self.botao_pula_questao = Button(self.frame_alternativas, bg="red",width=16, text="pular questão ", fg="white", font=("Verdana bold",14))
        self.botao_pula_questao.place(x=780 ,y=60)

class Match(Toplevel):
    def __init__(self):
        super().__init__()
        #cores em hexadecimal
        cinza = '#202020'
        escuro = '#101010'

        self.geometry("1080x800")
        self.title("quiz perguntas e respostas")
        self.configure(bg="#101010")

        # sempre pegar daqui um frame com 'bordas' finas
        self.frame_externo0 = Frame(self, width=1060, height=750, bg=cinza)
        self.frame_externo0.pack()
        self.frame_externo0.propagate(False)
        self.frame_externo1 = Frame(self.frame_externo0, width=1056, height=746, bg=escuro)
        self.frame_externo1.place(x=2, y=2)
        self.frame_externo1.propagate(False)
        #-----

        # frame principal superior
        self.frame_interno_superior0 = Frame(self.frame_externo1, width=1028, height=176, bg=cinza)
        self.frame_interno_superior0.pack(pady=5)
        self.frame_interno_superior0.propagate(False)
        self.frame_interno_superior1 = Frame(self.frame_interno_superior0, width=1024, height=169, bg=escuro)
        self.frame_interno_superior1.place(x=2, y=4)
        #---

        self.frame_pontuacao0 = Frame(self.frame_interno_superior1, bg=cinza, width=300, height=140)
        self.frame_pontuacao0.place(x=15, y=14)
        self.frame_pontuacao0.propagate(False)

        self.frame_pontuacao1 = Frame(self.frame_pontuacao0, width=296, bg=escuro, height=136)
        self.frame_pontuacao1.place(x=2, y=2)
        self.frame_pontuacao1.propagate(False)

        self.frame_player1 = Frame(self.frame_pontuacao1, width=280, bg=cinza, height=58)
        self.frame_player1.pack(pady=7)
        self.frame_player1.propagate(False)

        self.texto_player1 = Label(self.frame_player1, text="jogador 1 = X", bg=cinza, fg="gray", font=("Verdana bold", 16))
        self.texto_player1.pack(pady=12)

        self.frame_player2 = Frame(self.frame_pontuacao1, width=280, bg=cinza, height=58)
        self.frame_player2.pack()
        self.frame_player2.propagate(False)

        self.texto_player2 = Label(self.frame_player2, text="jogador 2 = X", bg=cinza, fg="gray", font=("Verdana bold", 16))
        self.texto_player2.pack(pady=12)

        self.frame_container_contador0 = Frame(self.frame_interno_superior1, bg=cinza, width=300, height=80)
        self.frame_container_contador0.place(x=710, y=14)
        self.frame_container_contador0.propagate(False)

        self.frame_container_contador1 = Frame(self.frame_container_contador0,  bg=escuro, width=296, height=76)
        self.frame_container_contador1.place(x=2, y=2)
        self.frame_container_contador1.propagate(False)

        self.frame_contador = Frame(self.frame_container_contador1, bg=cinza, width=266, height=50)
        self.frame_contador.pack(pady=14)
        self.frame_contador.propagate(False)

        self.texto_contador = Label(self.frame_contador, text="5:00:00", fg="red", bg=cinza, font=("Verdana bold", 17))
        self.texto_contador.pack(pady=8)

        # frame principal inferior
        self.frame_interno_inferior0 = Frame(self.frame_externo1, width=1028, height=550, bg=cinza)
        self.frame_interno_inferior0.pack(pady=2)
        self.frame_interno_inferior0.propagate(False)
        self.frame_interno_inferior1 = Frame(self.frame_interno_inferior0, width=1024, height=544, bg=escuro)
        self.frame_interno_inferior1.place(x=2, y=3)
        self.frame_interno_inferior1.propagate(False)
        #---

        self.frame_indicativo_sistema0 = Frame(self.frame_interno_inferior1, width=1012, height=70, bg=cinza)
        self.frame_indicativo_sistema0.pack(pady=8)
        self.frame_indicativo_sistema0.propagate(False)

        self.frame_indicativo_sistema1 = Frame(self.frame_indicativo_sistema0, width=1008, height=70, bg=escuro)
        self.frame_indicativo_sistema1.pack(pady=2)
        self.frame_indicativo_sistema1.propagate(False)

        self.frame_indicativo_rodada = Frame(self.frame_indicativo_sistema1, width=250, height=50, bg=cinza)
        self.frame_indicativo_rodada.pack(side=LEFT, padx=10)
        self.frame_indicativo_rodada.propagate(False)

        self.texto_indicativo_rodada = Label(self.frame_indicativo_rodada, bg=cinza, fg="gray", font=("Verdana bold", 20), text="rodada numero X")
        self.texto_indicativo_rodada.pack(pady=5)

        self.frame_indicativo_instrucoes_sistema = Frame(self.frame_indicativo_sistema1, width=730, height=50, bg=cinza)
        self.frame_indicativo_instrucoes_sistema.pack(side=RIGHT, padx=10)
        self.frame_indicativo_instrucoes_sistema.propagate(False)

        self.texto_indicativo_instrucoes_sistema = Label(self.frame_indicativo_instrucoes_sistema, bg=cinza, fg="red", font=("Verdana bold", 14), text="algum texto para instruir o usuário")
        self.texto_indicativo_instrucoes_sistema.pack(side=LEFT, padx=10, pady=8)

        self.frame_container_questao0 = Frame(self.frame_interno_inferior1, width=1012, height=220, bg=cinza)
        self.frame_container_questao0.pack(pady=5)
        self.frame_container_questao0.propagate(False)

        self.frame_container_questao1 = Frame(self.frame_container_questao0, width=1008, height=216, bg=escuro)
        self.frame_container_questao1.pack(pady=2)
        self.frame_container_questao1.propagate(False)

        self.frame_indicativo_tema_pergunta = Frame(self.frame_container_questao1, width=400, height=30, bg=cinza)
        self.frame_indicativo_tema_pergunta.place(x=10, y=10)
        self.frame_indicativo_tema_pergunta.propagate(False)

        self.texto_indicativo_tema_pergunta = Label(self.frame_indicativo_tema_pergunta, text="tema da pergunta é X", font=("Verdana Bold", 14), bg=cinza, fg="gray")
        self.texto_indicativo_tema_pergunta.pack(pady=5)

        self.frame_indicativo_numero_pergunta = Frame(self.frame_container_questao1, width=200, height=30, bg=cinza)
        self.frame_indicativo_numero_pergunta.place(x=790, y=10)
        self.frame_indicativo_numero_pergunta.propagate(False)

        self.texto_indicativo_numero_pergunta = Label(self.frame_indicativo_numero_pergunta, text="pergunta numero X", font=("Verdana Bold", 14), bg=cinza, fg="gray")
        self.texto_indicativo_numero_pergunta.pack(pady=5)

        self.frame_corpo_questao = Frame(self.frame_container_questao1, width=980, height=145, bg=cinza)
        self.frame_corpo_questao.place(x=14, y=55)
        self.frame_corpo_questao.propagate(False)

        texto_teste = "Lorem Ipsum é um texto padrão em latim usado para preencher espaços de texto em publicações, como revistas, jornais e sites. Ele é usado para testar e ajustar aspectos visuais, como a tipografia, a formatação e o layout, antes de utilizar conteúdo real."

        self.texto_corpo_questao = Label(self.frame_corpo_questao, bg=cinza, fg="gray", font=("Verdana bold", 15), wraplength=960, justify=LEFT, text=texto_teste)
        self.texto_corpo_questao.place(x=10, y=10)

        self.frame_conteiner_alternativas0 = Frame(self.frame_interno_inferior1, width=1012, height=210, bg=cinza)
        self.frame_conteiner_alternativas0.pack(pady=4)
        self.frame_conteiner_alternativas0.propagate(False)

        self.frame_conteiner_alternativas1 = Frame(self.frame_conteiner_alternativas0, width=1008, height=206, bg=escuro)
        self.frame_conteiner_alternativas1.pack(pady=2)
        self.frame_conteiner_alternativas1.propagate(False)

        self.frame_alternativas = Frame(self.frame_conteiner_alternativas1, width=980, height=185, bg=cinza)
        self.frame_alternativas.place(x=14, y=10)
        self.frame_alternativas.propagate(False)

        self.alternativa_correta = None
        self.resultado_questao = []

        # organizando funcionalidades de Checkbuttons de alternativas
        def selecionar_cb0():
            if self.cb_0.get():
                self.cb_1.set(0)
                self.cb_2.set(0)
                self.cb_3.set(0)

        def selecionar_cb1():
            if self.cb_1.get():
                self.cb_0.set(0)
                self.cb_2.set(0)
                self.cb_3.set(0)

        def selecionar_cb2():
            if self.cb_2.get():
                self.cb_0.set(0)
                self.cb_1.set(0)
                self.cb_3.set(0)

        def selecionar_cb3():
            if self.cb_3.get():
                self.cb_0.set(0)
                self.cb_1.set(0)
                self.cb_2.set(0)

        self.cb_0 = IntVar()
        self.cb_1 = IntVar()
        self.cb_2 = IntVar()
        self.cb_3 = IntVar()

        self.alternativa0 = Checkbutton(self.frame_alternativas, text="opção 1", variable=self.cb_0, command=selecionar_cb0, bg=cinza, font=("Verdana bold", 14), fg="gray")
        self.alternativa0.place(x=10, y=15)

        self.alternativa1 = Checkbutton(self.frame_alternativas, text="opção 2", variable=self.cb_1, command=selecionar_cb1, bg=cinza, font=("Verdana bold", 14), fg="gray")
        self.alternativa1.place(x=10, y=50)

        self.alternativa2 = Checkbutton(self.frame_alternativas, text="opção 3", variable=self.cb_2, command=selecionar_cb2, bg=cinza, font=("Verdana bold", 14), fg="gray")
        self.alternativa2.place(x=10, y=85)

        self.alternativa3 = Checkbutton(self.frame_alternativas, text="opção 4", variable=self.cb_3, command=selecionar_cb3, bg=cinza, font=("Verdana bold", 14), fg="gray")
        self.alternativa3.place(x=10, y=120)

        def mostrar_valor(valor):
            print(valor)
               
        self.botao_confirma = Button(self.frame_alternativas, bg="green", text="confirmar alternativa", fg="white", font=("Verdana bold",14), command=lambda: mostrar_valor([item for item in [self.cb_0.get(), self.cb_1.get(), self.cb_2.get(), self.cb_3.get()]]))
        self.botao_confirma.place(x=780 ,y=15)

        self.botao_pula_questao = Button(self.frame_alternativas, bg="red",width=16, text="pular questão ", fg="white", font=("Verdana bold",14))
        self.botao_pula_questao.place(x=780 ,y=60)
