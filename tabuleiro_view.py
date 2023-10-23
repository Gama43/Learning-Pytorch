import tkinter as tk
import chess

# Função para criar um quadrado no tabuleiro com a cor desejada
def criar_quadrado(canvas, x, y, cor):
    canvas.create_rectangle(x, y, x + TAMANHO_QUADRADO, y + TAMANHO_QUADRADO, fill=cor)

# Função para desenhar as peças no tabuleiro
def desenhar_pecas(canvas, tabuleiro):
    x, y = 0, 0
    for rank in range(7, -1, -1):
        for file in range(8):
            square = chess.square(file, rank)
            piece = tabuleiro.piece_at(square)
            if piece is not None:
                symbol = piece.symbol()
                imagem = pecas_imagens.get(symbol)
                if imagem:
                    canvas.create_image(x, y, image=imagem, anchor=tk.NW)
            x += TAMANHO_QUADRADO
        x = 0
        y += TAMANHO_QUADRADO

# Configuração da janela
janela = tk.Tk()
janela.title("Tabuleiro de Xadrez")
TAMANHO_QUADRADO = 65
TAMANHO_TABULEIRO = TAMANHO_QUADRADO * 8

# Crie um canvas para o tabuleiro
canvas = tk.Canvas(janela, width=TAMANHO_TABULEIRO, height=TAMANHO_TABULEIRO)
canvas.pack()

# Crie um tabuleiro de xadrez com a posição inicial
tabuleiro = chess.Board()

# Mapeamento dos símbolos das peças para os nomes dos arquivos de imagem
pecas_imagens = {
    'r': tk.PhotoImage(file='imagens/torre_preta.png'),
    'n': tk.PhotoImage(file='imagens/cavalo_preto.png'),
    'b': tk.PhotoImage(file='imagens/bispo_preto.png'),
    'q': tk.PhotoImage(file='imagens/rainha_preta.png'),
    'k': tk.PhotoImage(file='imagens/rei_preto.png'),
    'p': tk.PhotoImage(file='imagens/peao_preto.png'),
    'R': tk.PhotoImage(file='imagens/torre_branca.png'),
    'N': tk.PhotoImage(file='imagens/cavalo_branco.png'),
    'B': tk.PhotoImage(file='imagens/bispo_branco.png'),
    'Q': tk.PhotoImage(file='imagens/rainha_branca.png'),
    'K': tk.PhotoImage(file='imagens/rei_branco.png'),
    'P': tk.PhotoImage(file='imagens/peao_branco.png')
}

# Desenhe o tabuleiro com quadrados vermelhos e brancos
for i in range(8):
    for j in range(8):
        cor = "red" if (i + j) % 2 == 0 else "white"
        criar_quadrado(canvas, i * TAMANHO_QUADRADO, j * TAMANHO_QUADRADO, cor)

# Desenhe as peças no tabuleiro
desenhar_pecas(canvas, tabuleiro)

# Inicie a interface gráfica
janela.mainloop()
