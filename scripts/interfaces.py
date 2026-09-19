import pygame

class Texto:
    def __init__(self, texto, tamanho, cor, posicao):
        self.fonte = pygame.font.SysFont('arial', tamanho, bold=True)  # fonte usada no texto
        self.cor = cor                                                 # cor guardada para reescrever
        self.posicao = posicao                                         # posição central guardada
        self.mudarTexto(texto)                                         # cria a imagem do texto

    def mudarTexto(self, texto):
        self.imagem = self.fonte.render(texto, True, self.cor)         # transforma o texto em imagem
        self.retangulo = self.imagem.get_rect(center=self.posicao)     # centraliza na posição

    def desenhar(self, tela):
        tela.blit(self.imagem, self.retangulo)                         # desenha o texto na tela

class Botao:
    def __init__(self, texto, tamanhoTexto, tamanhoBotao, posicao):
        self.texto = Texto(texto, tamanhoTexto, (255, 255, 255), posicao)  # rótulo do botão
        self.retangulo = pygame.Rect((0, 0), tamanhoBotao)             # retângulo do botão
        self.retangulo.center = posicao                                # centraliza na posição pedida
        self.corNormal = (200, 70, 40)                                 # cor quando o mouse está fora
        self.corSelecao = (255, 140, 50)                               # cor com o mouse em cima
        self.selecionado = False                                       # guarda se o mouse está em cima

    def atualizar(self, posMouse, clique):
        self.selecionado = self.retangulo.collidepoint(posMouse)       # mouse está sobre o botão?
        return self.selecionado and clique                             # True só se clicou nele

    def desenhar(self, tela):
        cor = self.corSelecao if self.selecionado else self.corNormal  # escolhe a cor atual
        pygame.draw.rect(tela, cor, self.retangulo, border_radius=12)  # desenha o fundo do botão
        self.texto.desenhar(tela)                                      # desenha o texto por cima
