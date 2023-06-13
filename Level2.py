import pygame

class Lv2():
    def __init__(self):
        self.image = pygame.image.load("Images/WORLD2BACKGROUND.png")
        self.image = pygame.transform.scale(self.image, (800, 600))
        self.rect = self.image.get_rect()

    def init_2(self,Dave,Platform,Spike,Alien,FAlien):   # Creates and moves all assests for the first level
        plats = []
        spikes = []
        enemies = []
        Dave.rect = Dave.rect.move(225,550)
        plat = Platform.Platform_default(0,560,150,40,'Images/GRASS2.png')
        plats.append(plat)
        plat = Platform.Platform_default(240,560,75,40, 'Images/GRASS2.png')
        plats.append(plat)
        plat = Platform.Platform_default(240, 560, 75, 40, 'Images/GRASS2.png')
        plats.append(plat)
        alien = Alien.Alien(240,10,10)
        enemies.append(alien)

        return spikes, plats, enemies, Dave

def update(Lv2,enemies,plats,spikes,Dave,SCREEN,Alien):
    SCREEN.blit(Lv2.image, Lv2.rect)
    for alien in enemies:
        SCREEN.blit(alien.img, alien.rect)
    for spike in spikes:
        SCREEN.blit(spike.img, spike.rect)
    SCREEN.blit(Dave.image,Dave.rect)