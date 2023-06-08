import pygame

class Flag :
    def __init__(self,x,y,width,height) : # x/y are the coordiantes of the ground
      self.size = (width,height)
      self.x = int(x)
      self.y = int(y)
      self.image = pygame.image.load('CHECKPOINTACTIVE.png')
      self.image = pygame.transform.scale(self.image,self.size)
      self.rect = self.image.get_rect()

      self.rect.x = self.x
      self.rect.y = self.y

    def collision(self,player) :
     if self.rect.colliderect(player) :
       #Health -1
       self.image = pygame.image.load('CHECKPOINTNULL.png')
       self.image = pygame.transform.scale(self.image,self.size)
       print("Success!")
