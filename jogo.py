import pygame
from guy import Guy
from mago import Mago
from inimigo import Inimigo
from tiro import Tiro
from inimigo2 import Inimigo2
from inimigo3 import Inimigo3


pygame.init()
janela = pygame.display.set_mode([920, 600])
pygame.display.set_caption("Age Of Darkness")

#grupos
grupoDeObjetos = pygame.sprite.Group()
grupoDecolisao = pygame.sprite.Group()
grupoDeTiro = pygame.sprite.Group()
grupoMago = pygame.sprite.Group()

#fundo
fundo = pygame.sprite.Sprite(grupoDeObjetos)
fundo.image = pygame.image.load("data/teste.png")
fundo.image = pygame.transform.scale(fundo.image, [900, 700])
fundo.rect = fundo.image.get_rect()

#objetoss
guy = Guy(grupoDeObjetos)
mago = Mago(grupoMago)
inimigo1 = Inimigo(grupoDecolisao)
inimigo2 = Inimigo2(grupoDecolisao)
inimigo3 = Inimigo3(grupoDecolisao)

#musica
pygame.mixer.music.load("data/musica.mp3")
pygame.mixer.music.play(-1)


#janela
janela_aberta = True
clock = pygame.time.Clock()
while janela_aberta :
    clock.tick(60)
    pygame.time.delay(50)

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            janela_aberta = False

        #colisao do personagem com os inimigos
        elif pygame.sprite.spritecollide(guy, grupoDecolisao, False):
            print("Game over!!")
            janela_aberta = False

        #evento do tiro e colisao com os inimigos
        elif event.type ==pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                novotiro = Tiro(grupoDeObjetos, grupoDeTiro)
                novotiro.rect.center = guy.rect.center

            #botão para finalizar
            elif pygame.sprite.spritecollide(guy, grupoMago, True):
                janela_aberta = False
                print("Um mundo com grandes mistérios que está a sua espera")
                print("Venha jogar e se divertir construindo seu personagem num mundo 2D com os poderes que você desejar")
                print("Abril de 2021")
                print("Continua...")

        #colisao do tiro com o inimigo
        hits = pygame.sprite.groupcollide(grupoDeTiro, grupoDecolisao, True, True)

    #lógica e updated
    grupoDeObjetos.update()
    grupoDecolisao.update()
    grupoDeTiro.update()
    grupoMago.update()

    #draw
    janela.fill ([46, 46, 46])
    grupoDeObjetos.draw(janela)
    grupoDecolisao.draw(janela)
    grupoDeTiro.draw(janela)
    grupoMago.draw(janela)
    pygame.display.update()