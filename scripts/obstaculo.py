import random
import pygame

class Obstaculo:
    def __init__(self, tela):
        self.tela = tela                                           # tela onde o cone será desenhado
        self.imagem = pygame.image.load('carro/assets/cone.png')         # carrega a imagem do cone
        self.imagem = pygame.transform.scale(self.imagem, (50, 45))  # aumenta o cone (é muito pequeno)
        self.retangulo = self.imagem.get_rect()                    # caixa que representa o cone
        self.velocidade = 6                                        # velocidade que o cone desce
        self.sortearPosicao()                                      # sorteia a posição inicial

    def sortearPosicao(self):
        x = random.randint(60, 440 - self.retangulo.width)         # posição horizontal aleatória
        self.retangulo.topleft = (x, -self.retangulo.height)       # começa escondido acima da tela

    def atualizar(self):
        self.retangulo.y += self.velocidade                        # move o cone para baixo
        if self.retangulo.top > 700:                               # se o cone saiu por baixo da tela
            self.sortearPosicao()                                  # volta ao topo em outra posição

    def pegarMascara(self):
        return pygame.mask.from_surface(self.imagem)               # máscara com os pixels visíveis do cone

    def colisao(self, jogador):
        offset = (jogador.retangulo.x - self.retangulo.x,          # distância entre as caixas dos dois
                  jogador.retangulo.y - self.retangulo.y)
        sobreposicao = self.pegarMascara().overlap(                # verifica se algum pixel se sobrepõe
            jogador.pegarMascara(), offset)
        return sobreposicao is not None                            # True se colidiu, False se não

    def desenhar(self):
        self.tela.blit(self.imagem, self.retangulo)                # desenha o cone na tela
