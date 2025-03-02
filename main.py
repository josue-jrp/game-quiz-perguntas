from aba_main import *
from tkinter import *
import partida
import teste_random_questoes
import verificador_palpites

cinza = '#202020'
escuro = '#101010'

def app(root, nome, recorde, tema):
# a essa altura uma outra janela que aparecerápara o usuário antes dessa, pedirá o nome do jogador e a senha para que possam ser recuperados alguns dados do jogador como troféus e recordes anteriores

    # esse comando 'withdraw()' serve para deixar a janela anterior invisivel. E o outro comando para deixar ela visivel é deiconify()
    root.withdraw()

    

    info_partida = {"jogador1": {"nome":nome, "pontos":0, "recorde":recorde}, "tempo partida": "0.30", "tema escolhido":tema, "rodada":1}

    janela = Match()
    janela.texto_player1.destroy()

    ## aqui começa a organização visual de conteudo para o usuário 
    def organizar_cont():
        questao = teste_random_questoes.pegar_questao()
        pergunta, alternativas, rc = teste_random_questoes.separar_alternativas(questao)

        def organizar_questao(a0, a1, a2, a3):
            a0.configure(text=alternativas[0])
            a1.configure(text=alternativas[1])
            a2.configure(text=alternativas[2])
            a3.configure(text=alternativas[3])

            janela.texto_corpo_questao.configure(text=pergunta)
            janela.texto_indicativo_numero_pergunta.configure(text="")


        # essa função serve para organizar as pergunta e alternativas
        organizar_questao(janela.alternativa0, janela.alternativa1, janela.alternativa2, janela.alternativa3)

        return rc
    
    # essa chamada é somente para iniciar o game, depois essa chamada ocorre somente depois da interação com o usuário
    rc = organizar_cont()

    janela.texto_indicativo_tema_pergunta.configure(text= info_partida["tema escolhido"])
    janela.texto_indicativo_rodada.configure(text=f'Rodada {info_partida["rodada"]}')

    def verificar():
        status, palpite = verificador_palpites.botao_confirma({janela.alternativa0:janela.cb_0.get(), janela.alternativa1:janela.cb_1.get(), janela.alternativa2:janela.cb_2.get(), janela.alternativa3:janela.cb_3.get()})

        if status:
            # 'valor resposta' recebe um boleano indicando se a resposta é verdadeira ou falsa
            nonlocal rc
            valor_resposta = verificador_palpites.verificar(palpite, rc)

            if valor_resposta:
                janela.texto_indicativo_instrucoes_sistema.configure(text='Resposta correta!', fg="green")
                info_partida["jogador1"]["pontos"] = info_partida["jogador1"]["pontos"] + 1
                info_partida["rodada"] = info_partida["rodada"] + 1
                
            else:
                janela.texto_indicativo_instrucoes_sistema.configure(text='Resposta incorreta!', fg="red")
                info_partida["rodada"] = info_partida["rodada"] + 1

            rc = organizar_cont()
            # setando todas os cheks...
            janela.cb_0.set(0)
            janela.cb_1.set(0)
            janela.cb_2.set(0)
            janela.cb_3.set(0)
            janela.texto_indicativo_rodada.configure(text=f'Rodada {info_partida["rodada"]}')
            janela.texto_player2.configure(text=f'{info_partida["jogador1"]["nome"]} = {info_partida["jogador1"]["pontos"]}')


        else:
            janela.texto_indicativo_instrucoes_sistema.configure(text='[ERRO] Você precisa marcar uma das opções!')



    janela.botao_confirma.config(command=verificar)






    def zerar_pontos(janela_, root_, info_partida_):
        info_partida_["jogador1"]["pontos"] = 0
        info_partida_["rodada"] = 0
        partida.game_over(janela_, root_, info_partida_)

    botao_desistir = Button(janela.frame_player1, width=15, height=5, bg="red", fg="white", font=("Verdana bold", 14), text="desistir", command=lambda: zerar_pontos(janela, root, info_partida))
    botao_desistir.pack(pady=5)

    janela.texto_player2.configure(text=f'{nome} = {info_partida["jogador1"]["pontos"]}', fg="green")  

    def cronometro(tempo_inicial, janela_principal=root):

        def iniciar():
            nonlocal tempo_inicial
            nonlocal janela_principal

            try:

                if tempo_inicial > 0:
                    janela.texto_contador.config(text=f"00:{tempo_inicial:02d}")
                    tempo_inicial -= 1
                    janela.after(1000, iniciar)
                    print(f"00:{tempo_inicial:02d}")

                else:
                    janela.texto_contador.config(text="00:00")
                    print("fim de jogo!")
                    partida.game_over(janela, janela_principal, info_partida)

            except:
                print("botão 'desistir' foi apertado! ")

        # chamada para função que inicia o contador regressivo
        iniciar()

    cronometro(20)
    

def aba_explicacao(root, conteiner, nome, recorde, tema):

    lista = conteiner.winfo_children()
    # comando para apagar todos os widgets de dentro do container
    for item in lista:
        item.destroy()
    
    texto_explicacao = Label(conteiner, text="Obrigado por testar a fase beta do game!\n\nA partida terá um cronômetro de 20 segundos inicialmente.\n\nClique em iniciar para começar o game!", font=("Verdana bold", 16), bg=cinza, fg="white")
    texto_explicacao.pack(pady=10)

    botao_iniciar = Button(conteiner, width=10, height=2, text="iniciar", bg="green", font=("Verdana bold", 14), fg="white", command=lambda: app(root, nome, recorde, tema))
    botao_iniciar.pack(pady=50)
    
    print(f"\n\nos dados que foram passados para a janela de explicação são:\n{nome}\n{recorde}\n{tema}\n\n")

