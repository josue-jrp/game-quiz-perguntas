from tkinter import *

cinza = '#202020'
escuro = '#101010'

# esta função exibe para o jogador um frame contendo seu recorde e o recorde de outros jogadores
# essa função deve conter (argumentos) janela em que o frame aparecerá, e informações da partida 

def game_over(janela, janela_principal, info_partida):

    lista = janela.frame_externo1.winfo_children()

    for item in lista:
        item.destroy()

    def voltar():
        nonlocal janela
        nonlocal janela_principal

        janela.destroy()
        janela_principal.deiconify()

    print(info_partida)

    # frame de game over
    frame_pos_partida0 = Frame(janela.frame_externo1, width=976, height=660, bg="lightgray")
    frame_pos_partida0.place(x=40, y=35)
    frame_pos_partida0.propagate(False)

    frame_pos_partida1 = Frame(frame_pos_partida0, width=970, height=654, bg=escuro)
    frame_pos_partida1.place(x=3, y=2)
    frame_pos_partida1.propagate(False)

    frame_titulo = Frame(frame_pos_partida1, bg=escuro, width=500, height=60)
    frame_titulo.pack(pady=20)
    frame_titulo.propagate(False)

    texto_titulo = Label(frame_titulo, text="game over".upper() , font=("Verdana Bold", 32), fg=escuro, bg="red")
    texto_titulo.pack()

    frame_informacoes = Frame(frame_pos_partida1, width=900, height=300, bg=cinza)
    frame_informacoes.pack(pady=30)
    frame_informacoes.propagate(False)

    frame_info_nome = Frame(frame_informacoes, width=350, height=50, bg=cinza)
    frame_info_nome.pack(pady=30)
    frame_info_nome.propagate(False)

    texto_nome = Label(frame_info_nome, text=f'jogador: {info_partida["jogador1"]["nome"]}', font=("Verdana bold", 18), bg=cinza, fg="lightgray")
    texto_nome.pack(pady=10)

    frame_info_pontos = Frame(frame_informacoes, width=350, height=50, bg=cinza)
    frame_info_pontos.pack()
    frame_info_pontos.propagate(False)

    texto_pontos = Label(frame_info_pontos, text=f'total pontos: {info_partida["jogador1"]["pontos"]}', font=("Verdana bold", 18), bg=cinza, fg="lightgray")
    texto_pontos.pack(pady=10)

    frame_info_recorde = Frame(frame_informacoes, width=350, height=50, bg=cinza)
    frame_info_recorde.pack(pady=30)
    frame_info_recorde.propagate(False)

    texto_recorde = Label(frame_info_recorde, text=f'recorde atual: {info_partida["jogador1"]["recorde"]}', font=("Verdana bold", 18), bg=cinza, fg="lightgray")
    texto_recorde.pack(pady=10)
    
    botao_voltar = Button(frame_pos_partida1, text="voltar ao inicio", bg="red", fg="white", font=("Verdana bold", 18), command=voltar)
    botao_voltar.pack(pady=15)