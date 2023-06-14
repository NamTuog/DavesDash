import pygame

class Alien():
    def __init__(self,lx,rx,wany):
        self.size = (30,30)
        self.speed = 3
        self.img1 = pygame.image.load('Images/WALK1.png')
        self.img1 = pygame.transform.scale(self.img1, self.size)
        self.rect = self.img1.get_rect()
        self.img2 = pygame.image.load('Images/WALK2.png')
        self.img2 = pygame.transform.scale(self.img2, self.size)
        self.img3 = pygame.image.load('Images/WALK3.png')
        self.img3 = pygame.transform.scale(self.img3, self.size)
        self.run = [self.img1,self.img2,self.img3]
        self.lx = lx
        self.rx = rx
        self.wany = wany

        self.rect.move(self.rx,self.wany)

        # Changing images
        self.image_flipped = True
        self.index = 0
        # Directions
        self.left = False
        self.right = True


    def wander(self):
        # Left
        if self.left == True:
            if self.rect.x > self.lx:   # If x is greater than left x
                self.rect.move_ip(-self.speed,0)
                self.image_flipped = True
                if self.rect.x <= self.lx+20:
                    self.right = True
                    self.left = False

        # Right
        elif self.right == True:
            if self.rect.x < self.rx:
                self.rect.move_ip(self.speed,0)
                self.image_flipped = False
                if self.rect.x >= self.rx-20:
                    self.left = True
                    self.right = False

    def update(self):
        self.index += 1
        if self.index >= len(self.run):
            self.index = 0
        self.img = self.run[self.index]
        if self.image_flipped == True:
            self.img = pygame.transform.flip(self.img,True,False)



class FAlien():
    def __init__(self,lx,rx,wany):
        self.size = (20,20)
        self.speed = 5
        self.img = pygame.image.load('Images/FLYINGALIEN.png')
        self.img = pygame.transform.scale(self.img, self.size)
        self.rect = self.img.get_rect()

        self.rect.move(rx,wany)

        # Directions
        self.image_flipped = False
        self.left = False
        self.right = True



    def wander(self):
        # Left
        if self.left == True:
            if self.rect.x > self.lx:  # If x is greater than left x
                self.rect.move_ip(-self.speed, 0)
                self.image_flipped = True
                if self.rect.x <= self.lx:  # Once x = left side, switch
                    self.right = True
                    self.left = False

        # Right
        elif self.right == True:
            if self.rect.x < self.rx:
                self.rect.move_ip(self.speed, 0)
                self.image_flipped = False
                if self.rect.x >= self.rx:
                    self.left = True
                    self.right = False

    def update(self):   # Used to update the alien's image based on movement direction
        self.index += 1
        if self.index >= len(self.run):
            self.index = 0
        self.img = self.run[self.index] # Through each loop swap img through index
        if self.image_flipped == True:
            self.img = pygame.transform.flip(self.img, True, False)
