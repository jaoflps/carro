import pygame
from scripts.cenas import Menu, Partida

# 1 a 8: configurações da janela do jogo
tamanhoTela = (500, 700)          # largura e altura da tela (altere e veja o que acontece!)
corFundo = (35, 35, 40)           # cor de fundo ao redor da estrada
tituloJanela = 'Jogo do Carro'    # título que aparece na barra da janela
fps = 60                       # quadros por segundo (velocidade do jogo)

# inicia o pygame e cria a janela
pygame.init()
tela = pygame.display.set_mode(tamanhoTela)
pygame.display.set_caption(tituloJanela)
relogio = pygame.time.Clock()     # controla o tempo entre os quadros

# dicionário com todas as cenas do jogo (menu e partida)
cenas = {
    'menu': Menu(tela),
    'partida': Partida(tela),
}
cenaAtual = cenas['menu']         # o jogo sempre começa no menu

rodando = True                    # controla se o jogo continua aberto
while rodando:
    relogio.tick(fps)             # limita o jogo aos fps definidos
    eventos = pygame.event.get()  # guarda todos os eventos deste quadro
    for evento in eventos:
        if evento.type == pygame.QUIT:   # clicou no X da janela?
            rodando = False              # encerra o loop principal

    tela.fill(corFundo)                        # pinta o fundo da tela
    estadoAntes = cenaAtual.estado             # guarda o estado antes de atualizar
    novaCena = cenaAtual.atualizar(eventos)    # atualiza a lógica da cena
    cenaAtual.desenhar()                       # desenha a cena na tela
    if novaCena != estadoAntes:                # se a cena pediu uma troca de estado
        for nome, cena in cenas.items():       # procura qual cena tem esse estado
            if nome == novaCena:
                cenaAtual = cena               # troca para a nova cena
                if hasattr(cena, 'reiniciar'): # se a cena puder ser reiniciada
                    cena.reiniciar()           # começa a partida do zero

    pygame.display.update()       # mostra tudo o que foi desenhado

pygame.quit()                     # fecha o pygame ao sair
