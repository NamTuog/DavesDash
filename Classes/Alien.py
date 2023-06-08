import pygame

class Alien():
    def __init__(self,lx,rx,wany):
        self.size = (20,20)
        self.speed = 5
        self.img1 = pygame.image.load('Images/WALK1.png')
        self.img1 = pygame.transform.scale(self.img1, self.size)
        self.rect = self.img1.get_rect()
        self.img2 = pygame.image.load('Images/WALK2.png')
        self.img2 = pygame.transform.scale(self.img2, self.size)
        self.img2 = pygame.image.load('Images/WALK3.png')
        self.img2 = pygame.transform.scale(self.img3, self.size)
        self.run = [self.img1,self.img2,self.img3]

        self.rect.move(rx,wany)

        # Changing images
        self.image_frame = 1
        self.img_time = 0
        self.img_change = False
        self.image_flipped = False
        self.index = 0
        # Directions
        self.left = False
        self.right = False



    def wander(self):
        # Left
        if self.left and self.x > self.lx:  # and not self.right
            self.rect.move_ip(-self.speed,0)
            self.img_change = True
            self.image_flipped = True

        # Right
        elif self.right and self.x < self.rx:
            self.rect.move_ip(self.speed,0)
            self.img_change = True
            self.image_flipped = False

    def update(self):
        self.index += 1
        if self.index >= len(self.run):
            self.index = 0
        self.img = self.run(self.index)