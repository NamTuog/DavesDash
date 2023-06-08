# Import
import pygame


class Platform_default:  # Not moving
    def __init__(self, x, y, width, height, img):  # x/y are the coordiantes of the ground
        self.size = (width, height)
        self.x = int(x)
        self.y = int(y)
        self.image = pygame.image.load(img)
        self.image = pygame.transform.scale(self.image, self.size)
        self.rect = self.image.get_rect()
        self.top = pygame.Rect(self.x + 10, self.y, self.size[0] - 20, self.size[1] // 4)
        self.bottom = pygame.Rect(self.x, self.y + self.size[1] // 2, self.size[0], self.size[1] // 2)

        self.left = pygame.Rect(self.x, self.y + self.size[1] // 4, (self.size[0]) // 4,
                                self.size[1] // 2)  # Left half
        self.right = pygame.Rect(self.x + (self.size[0] - (self.size[0] // 4)), self.y + self.size[1] // 4,
                                 self.size[0] // 4, self.size[1] // 2)

        self.rect.x = self.x
        self.rect.y = self.y

    def collision(self, player):
        if self.left.colliderect(player.right):
            player.rect.right = self.rect.left
            player.movement_x = 0

        if self.right.colliderect(player.left):
            player.rect.left = self.rect.right
            player.movement_x = 0

        if self.top.colliderect(player.bottom):
            player.rect.bottom = self.rect.top
            player.velocity_y = 0

        if self.bottom.colliderect(player.top):
            player.rect.top = self.rect.bottom
            player.velocity_y += 1


class Platform_jumping(Platform_default):
    def collision(self, player):
        if self.rect.colliderect(player):
            player.image = pygame.image.load('JUMP.png')
            player.velocity_y -= 12
            player.jump = True
        else:
            pass





