import pygame


class Lv1():
    def __init__(self):
        self.image = pygame.image.load("Images/WORLD1BACKGROUND.png")
        self.image = pygame.transform.scale(self.image, (800, 600))
        self.rect = self.image.get_rect()

    def init_1(self,Dave,Spike,Alien):   # Creates and moves all assests for the first level
        spikes = []
        enemies = []
        Dave = Dave.Dave(125,10)
        Dave.rect = Dave.rect.move(125,450)
        spike = Spike.Spike(370,580,10,20)
        spikes.append(spike)
        spike = Spike.Spike(380,580,10,20)
        spikes.append(spike)
        spike = Spike.Spike(390, 580, 10, 20)
        spikes.append(spike)
        spike = Spike.Spike(400, 580, 10, 20)
        spikes.append(spike)
        spike = Spike.Spike(410, 580, 10, 20)
        spikes.append(spike)
        spike = Spike.Spike(420, 580, 10, 20)
        spikes.append(spike)
        spike = Spike.Spike(430, 580, 10, 20)
        spikes.append(spike)
        spike = Spike.Spike(440, 580, 10, 20)
        spikes.append(spike)
        spike = Spike.Spike(450, 580, 10, 20)
        spikes.append(spike)
        #spike = Spike.Spike()
        #spikes.append(spike)
        #spike = Spike.Spike()
        #spikes.append(spike)
        #alien = Alien.Alien()
        #enemies.append(alien)
        return spike, spikes, enemies, Dave

def update(Lv1,enemies,spikes,Dave,SCREEN,Alien):
    SCREEN.blit(Lv1.image, Lv1.rect)
    for alien in enemies:
        SCREEN.blit(alien.img, alien.rect)
    for spike in spikes:
        SCREEN.blit(spike.image, spike.rect)
    SCREEN.blit(Dave.image,Dave.rect)