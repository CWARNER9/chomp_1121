import pygame



# define a class called grenade
class Grenade(pygame.sprite.Sprite):
    def __init__(self,pos):
        super().__init__()
        self.image = pygame.image.load('assets/images/grenade2.png')
        self.image = pygame.transform.scale_by(self.image, factor=0.05)
        self.rect = self.image.get_rect()
        self.rect.midtop = pos
        self.velocity = 1

    def update(self):
        self.rect.y += self.velocity
        if self.boom_time:
            if pygame.time.get_ticks() - self.boom_time >1000:
                self.kill()
    def boom(self):
        self.boom_time = pygame.time.get_ticks()
        self.image = pygame.image.load('assets/images/explosion.png')






# attributes  image, rect, velocity


# methods
# boom (explodes changing colors),
# update (moves down),
# draw (takes screen as argument)
