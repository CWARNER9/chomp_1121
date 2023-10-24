import pygame



# define a class called grenade
class Grenade(pygame.sprite.Sprite):
    def __init__(self, screen):
        super().__init__()
        self.image = pygame.Surface((150, 50))
        self.image.fill((0, 0, 220))
        self.rect = self.image.get_rect()
        self.rect.x = screen.get_width() / 2
        self.rect.y = 5
        self.velocity = -1

# attributes  image, rect, velocity


# methods
# boom (explodes changing colors),
# update (moves down),
# draw (takes screen as argument)
