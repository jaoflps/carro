import random
import pygame
from scripts.jogador import Jogador
from scripts.obstaculo import Obstaculo
from scripts.interfaces import Texto, Botao

class Menu:
    def __init__(self, tela):
        self.tela = tela                                          # tela onde o menu será desenhado
        self.estado = 'menu'                                      # estado desta cena
        self.titulo = Texto('JOGO DO CARRO', 60, (255, 210, 0), (250, 180))   # título do menu
        self.subtitulo = Texto('Desvie dos cones!', 30, (240, 240, 240), (250, 260))  # frase de apoio
        self.instrucoes = Texto('Use as setas < > ou A D para mover', 22, (180, 180, 180), (250, 590))
        self.botaoJogar = Botao('Jogar', 36, (200, 70), (250, 400))           # botão de começar

    def atualizar(self, eventos):
        self.estado = 'menu'                                      # no começo do quadro volta ao estado padrão
        clique = False                                            # guarda se o mouse foi clicado neste quadro
        for evento in eventos:
            if evento.type == pygame.MOUSEBUTTONDOWN and evento.button == 1:  # botão esquerdo do mouse
                clique = True                                     # houve um clique
        if self.botaoJogar.atualizar(pygame.mouse.get_pos(), clique):         # clicou no botão Jogar?
            self.estado = 'partida'                               # muda o estado para a cena da partida
        return self.estado                                        # devolve o estado para o main.py

    def desenhar(self):
        self.titulo.desenhar(self.tela)                           # desenha o título
        self.subtitulo.desenhar(self.tela)                        # desenha a frase de apoio
        self.instrucoes.desenhar(self.tela)                       # desenha as instruções
        self.botaoJogar.desenhar(self.tela)                       # desenha o botão

class Partida:
    def __init__(self, tela):
        self.tela = tela                                          # tela onde a partida será desenhada
        self.estado = 'partida'                                   # estado desta cena
        self.jogador = Jogador(tela)                              # cria o carro do jogador
        self.obstaculos = []                                      # lista com os cones da pista
        for i in range(3):                                        # cria 3 cones
            self.obstaculos.append(Obstaculo(tela))
        self.pontosValor = 0                                      # pontuação atual do jogador
        self.contador = 1                                         # pontos ganhos a cada quadro
        self.pontosTexto = Texto('Pontos: 0', 32, (255, 255, 255), (250, 35)) # texto dos pontos
        self.faixaY = 0                                           # posição das faixas da estrada (animação)
        self.reiniciar()                                          # prepara a partida do zero

    def reiniciar(self):
        self.pontosValor = 0                                      # zera a pontuação
        self.pontosTexto.mudarTexto('Pontos: 0')                  # volta o texto ao início
        self.jogador.retangulo.midbottom = (250, 660)             # carro de volta ao centro
        for i, obstaculo in enumerate(self.obstaculos):           # reposiciona todos os cones
            obstaculo.sortearPosicao()                            # sorteia uma nova posição
            obstaculo.retangulo.y -= i * 300 + random.randint(0, 150)  # espaça os cones na vertical

    def atualizar(self, eventos):
        self.estado = 'partida'                                   # no começo do quadro volta ao estado padrão
        teclas = pygame.key.get_pressed()                         # lê quais teclas estão pressionadas
        self.jogador.atualizar(teclas)                            # move o carro para os lados

        colidiu = False                                           # guarda se bateu em algum cone
        for obstaculo in self.obstaculos:                         # percorre todos os cones
            obstaculo.atualizar()                                 # move o cone para baixo
            if obstaculo.colisao(self.jogador):                   # testa a colisão com o carro
                colidiu = True                                    # achou uma colisão

        if colidiu:                                               # se bateu em algum cone...
            self.estado = 'menu'                                  # ...volta para o menu (fim de jogo)

        self.pontosValor += self.contador                         # soma os pontos do tempo jogado
        self.pontosTexto.mudarTexto('Pontos: ' + str(self.pontosValor))      # atualiza o texto dos pontos
        return self.estado                                        # devolve o estado para o main.py

    def desenharEstrada(self):
        pygame.draw.rect(self.tela, (60, 60, 65), (40, 0, 420, 700))          # asfalto da estrada
        pygame.draw.rect(self.tela, (255, 255, 255), (44, 0, 6, 700))         # linha branca esquerda
        pygame.draw.rect(self.tela, (255, 255, 255), (450, 0, 6, 700))        # linha branca direita
        self.faixaY = (self.faixaY + 6) % 80                                  # anima as faixas descendo
        for y in range(-80, 700, 80):                                         # faixas tracejadas centrais
            pygame.draw.rect(self.tela, (230, 230, 100), (247, y + self.faixaY, 6, 40))

    def desenhar(self):
        self.desenharEstrada()                                    # desenha a estrada animada
        for obstaculo in self.obstaculos:                         # percorre todos os cones
            obstaculo.desenhar()                                  # desenha cada cone
        self.jogador.desenhar()                                   # desenha o carro por cima
        self.pontosTexto.desenhar(self.tela)                      # desenha a pontuação no topo
