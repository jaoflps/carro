import pygame

class Jogador:
    def __init__(self, tela):
        self.tela = tela                                          # tela onde o carro será desenhado
        self.imagem = pygame.image.load('carro/assets/carro.png')       # carrega a imagem do carro
        self.imagem = pygame.transform.scale(self.imagem, (64, 64))  # aumenta o carro (é muito pequeno)
        self.retangulo = self.imagem.get_rect()                   # caixa que representa o carro
        self.retangulo.midbottom = (250, 660)                     # posição inicial: embaixo, no centro
        self.velocidade = 8                                       # pixels que o carro anda por quadro

    def atualizar(self, teclas):
        if teclas[pygame.K_LEFT] or teclas[pygame.K_a]:   # seta esquerda ou tecla A
            self.retangulo.x -= self.velocidade           # move para a esquerda
        if teclas[pygame.K_RIGHT] or teclas[pygame.K_d]:  # seta direita ou tecla D
            self.retangulo.x += self.velocidade           # move para a direita
        # limites da estrada (o carro não pode sair dela)
        if self.retangulo.left < 50:
            self.retangulo.left = 50
        if self.retangulo.right > 450:
            self.retangulo.right = 450

    def pegarMascara(self):
        return pygame.mask.from_surface(self.imagem)      # máscara com os pixels visíveis do carro

    def desenhar(self):
        self.tela.blit(self.imagem, self.retangulo)       # desenha o carro na tela
