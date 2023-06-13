# Import
import pygame


class Platform_default:  # Not moving
    def __init__(self, x, y, width, height, img):  # x/y are the coordiantes of the ground
        self.size = (width, height)
        self.x = int(x)
        self.y = int(y)
        self.img = pygame.image.load(img)
        self.img = pygame.transform.scale(self.img, self.size)
        self.rect = self.img.get_rect()
        self.top = pygame.Rect(self.x + 10, self.y, self.size[0] - 20, self.size[1] // 4)
        self.bottom = pygame.Rect(self.x, self.y + self.size[1] // 2, self.size[0], self.size[1] // 2)
        self.left = pygame.Rect(self.x, self.y + self.size[1] // 4, (self.size[0]) // 4,
                                self.size[1] // 2)  # Left half
        self.right = pygame.Rect(self.x + (self.size[0] - (self.size[0] // 4)), self.y + self.size[1] // 4,
                                 self.size[0] // 4, self.size[1] // 2)

        self.rect.x = self.x
        self.rect.y = self.y

    def collision(self, Dave):
        if self.left.colliderect(Dave.right):
            Dave.rect.right = self.rect.left
            Dave.movement_x = 0

        if self.right.colliderect(Dave.left):
            Dave.rect.left = self.rect.right
            Dave.movement_x = 0

        if self.top.colliderect(Dave.bottom):
            Dave.rect.bottom = self.rect.top
            Dave.velocity_y = 0

        if self.bottom.colliderect(Dave.top):
            Dave.rect.top = self.rect.bottom
            Dave.velocity_y += 1


class Platform_jumping(Platform_default):
    def collision(self, Dave):
        if self.rect.colliderect(Dave):
            Dave.image = pygame.image.load('Images/JUMP.png')
            Dave.velocity_y -= 12
            Dave.jump = True
        else:
            pass