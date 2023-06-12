# Import
import pygame


# Class (Main Character)
class Dave():
    def __init__(self, x, y):
        self.x = int(x)
        self.y = int(y)
        self.size = (100, 100)
        self.health = 1
        self.speed = 4
        self.default_img = pygame.image.load('IDLE1.png')  # First image
        self.image = self.default_img
        self.rect = self.image.get_rect()

        # movements (jump)
        self.jump = False  # Check if Jumping is true or not
        self.jump_time = 0  # Duration of Jumping
        self.velocity_y = 0  # Speed of Jumping and Gravity
        self.jumping_speed = 5

        # Changing Images
        self.image_frame = 1  # Frame for change
        self.image_time = 0  # Duration
        self.image_Change = False  # Walking motion
        self.image_Flipped = False

        # Updating
        self.rect.x = self.x
        self.rect.y = self.y

        # Boxes following the player
        self.top = pygame.Rect(self.x, self.y, self.size[0] - 30, self.size[1] // 2)  # Top half of the player
        self.bottom = pygame.Rect(self.x, self.y + self.size[1] // 2 + 150, self.size[0] - 30,
                                  self.size[1] // 2)  # Bottom half of the player
        self.top[0] = self.x
        self.top[1] = self.y
        self.bottom[0] = self.x
        self.bottom[1] = self.y

        self.left = pygame.Rect(self.x, self.y, (self.size[0]) // 4, self.size[1] // 2)  # Left half
        self.left[0] = self.x
        self.left[1] = self.y

        self.right = pygame.Rect(self.x, self.y, (self.size[0]) // 4, self.size[1] // 2)  # Right half
        self.right[0] = self.x
        self.right[1] = self.y

    def move(self, platform):
        # Movements
        self.movement_x = 0  # X movements that are totally added
        self.movement_y = 0  # Y movements that are totallya dded

        # Key
        key = pygame.key.get_pressed()
        print(key)

        # Left & Right Keys
        if key[pygame.K_LEFT] or key[pygame.K_a]:
            self.movement_x = - self.speed  # Backwards
            self.image_Change = True
            self.image_Flipped = True  # Flip image to the left

        if key[pygame.K_RIGHT] or key[pygame.K_d]:
            self.movement_x = self.speed  # Right side
            self.image_Change = True
            self.image_Flipped = False  # Not flipping the iamge

        # Gravity
        if not self.rect.colliderect(platform):
            self.velocity_y += 0.25

        # Jumping

        if not self.jump:  # Prevents Double Jumps
            if key[pygame.K_UP] or key[pygame.K_SPACE] or key[pygame.K_w]:  # When the Up or space is pressed
                if self.bottom.colliderect(platform):  # When colliding with the platform
                    self.jump = True  # Jumping is valid
                    self.jump_time = pygame.time.get_ticks()  # Measure the time
                    self.velocity_y = -self.jumping_speed  # Goes Up by 35
                else:
                    pass
        if self.jump:  # While it is jumping
            self.image = pygame.image.load('JUMP.png')  # JUMP image
            time_now = pygame.time.get_ticks()  # Time Now
            time_difference = time_now - self.jump_time  # Differnce betwen the time
            if time_difference > 1:  # If the time difference is bigger than 1000
                self.jump = False  # Jump finishes   (Does not go forever)

        # Walking Motion
        if self.image_Change:  # When self.image_Change is true from left & right movements
            if self.image_frame % 30 == 0:  # Every 10 Frames
                self.image = pygame.image.load('IDLE2.png')  # Load another image
                self.image = pygame.transform.scale(self.image, self.size)
            else:
                self.image = self.default_img  # Go back to the original image
                self.image_Change = False
            self.image_frame += 1

            # Image Switching
        if self.image_Flipped:  # When flipped is true
            self.image = pygame.transform.flip(self.default_img, True, False)  # flip the image

        self.movement_y += self.velocity_y  # Add all the velocities including Jump and Gravity to the movement_y
        self.rect.x += self.movement_x  # Move the player
        self.rect.y += self.movement_y  # Move the player

        # Updating the rects (+20 since the rect is too big.)
        self.top.x = self.rect.x + 20
        self.top.y = self.rect.y
        self.bottom.x = self.rect.x + 20
        self.bottom.y = self.rect.y + self.size[1] // 2
        self.left.x = self.rect.x + 15
        self.left.y = self.rect.y + 10
        self.right.x = self.rect.x + 70
        self.right.y = self.rect.y + 10

        # Preventing the player to go outside of the screen
        if self.rect.bottom > 600:
            self.rect.bottom = 600
            self.movement_y = 0
        if self.rect.top < 0:
            self.rect.top = 0
            self.movement_y = 0
        if self.rect.right > 800:
            self.rect.right = 800
            self.movement_x = 0
        if self.rect.left < 0:
            self.rect.left = 0
            self.movement_x = 0