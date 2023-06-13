import pygame


class Lv1():
    def __init__(self):
        self.image = pygame.image.load("Images/WORLD1BACKGROUND.png")
        self.image = pygame.transform.scale(self.image, (800, 600))
        self.rect = self.image.get_rect()

    def init_1(self,Dave,Platform,Spike,Alien, Flag):   # Creates and moves all assests for the first level
        plats = []
        spikes = []
        enemies = []
        plat1 = Platform.Platform_default(0,570,370,50,'Images/WORLD1PLATFORM.png')
        plats.append(plat1)
        plat2 = Platform.Platform_default(460,570,360,50,'Images/WORLD1PLATFORM.png')
        plats.append(plat2)
        plat3 = Platform.Platform_jumping(770,530,20,25,'Images/Jumping.png')
        plats.append(plat3)
        plat4 = Platform.Platform_default(460,370,190,25, 'Images/WORLD1PLATFORM.png')
        plats.append(plat4)
        plat5 = Platform.Platform_default(200,370,150,25, 'Images/WORLD1PLATFORM.png')
        plats.append(plat5)
        plat6 = Platform.Platform_default(48, 350, 75, 20, 'Images/platform_default.png')
        plats.append(plat6)
        plat7 = Platform.Platform_default(200,178,150,25, 'Images/platform_default.png')
        plats.append(plat7)
        plat8 = Platform.Platform_default(460,160,65,25, 'Images/platform_default.png')
        plats.append(plat8)
        plat9 = Platform.Platform_jumping(45,301,20,25, 'Images/Jumping.png')
        plats.append(plat9)
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
        alien = Alien.Alien(200,360,190)
        enemies.append(alien)
        Flag= Flag(485,100,50,60)
        Dave = Dave.Dave(100, 15)
        #Dave.rect = Dave.rect.move(125, 450)
        return spike, spikes, enemies, Dave,plat1,plat2,plat3,plat4,plat5,plat6,plat7,plat8,plat9,Flag

def update(Lv1,enemies,spikes,Dave,SCREEN,Alien,plat1,plat2,plat3,plat4,plat5,plat6,plat7,plat8,plat9, Flag):
    SCREEN.blit(Lv1.image, Lv1.rect)
    #for alien in enemies:
     #   Alien.Alien.wander()
       # Alien.Alien.update()
      #  SCREEN.blit(alien.img, alien.rect)
    for spike in spikes:
        spike.spike.collision()
        SCREEN.blit(spike.image, spike.rect)
    SCREEN.blit(Dave.image,Dave.rect)
    SCREEN.blit(plat1.img,plat1.rect)
    SCREEN.blit(plat2.img, plat2.rect)
    SCREEN.blit(plat3.img, plat3.rect)
    SCREEN.blit(plat4.img, plat4.rect)
    SCREEN.blit(plat5.img, plat5.rect)
    SCREEN.blit(plat6.img, plat6.rect)
    SCREEN.blit(plat7.img, plat7.rect)
    SCREEN.blit(plat8.img, plat8.rect)
    SCREEN.blit(plat9.img, plat9.rect)
