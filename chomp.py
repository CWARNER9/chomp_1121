# Example file showing a basic pygame "game loop"
import pygame

from grenade import Grenade
from helpers import *
from fish import Fish
from boat import Boat

# pygame setup
pygame.init()
# make a clock
clock = pygame.time.Clock()

# set the resolution of our game window
WIDTH = 1080
HEIGHT = 720
screen = pygame.display.set_mode((WIDTH, HEIGHT))

# Make my background once!
background = make_background(screen)

print(pygame.font.get_fonts())
# declare a Font
game_font = pygame.font.SysFont('impact', 120)

# make our fish group
fish_group = pygame.sprite.Group()

# make a boat instance
my_boat = Boat(screen)
boat_group = pygame.sprite.Group()
boat_group.add(my_boat)

# make a grendade
my_grenade = Grenade(screen)
grenade_group = pygame.sprite.Group()
grenade_group.add(my_grenade)
# make fish and add to group
num_fish = 100
[fish_group.add(Fish(screen)) for n in range(num_fish) ]


running = True
while running:
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                my_boat.velocity += 1
            if event.key == pygame.K_LEFT:
                my_boat.velocity -= 1

    # update my fish
    fish_group.update()
    boat_group.update()

    # draw the background on the screen
    screen.blit(background, (0, 0))
    # draw text
    font_surface = game_font.render('CHOMP',1,(199, 23, 4))
    center_surfaces(screen, font_surface)

    # draw our fish
    fish_group.draw(screen)

    # draw the boat
    boat_group.draw(screen)

    clock.tick(60) # run at 60 FPS

    pygame.display.set_caption(f"CHOMP {clock.get_fps():3}")

    # flip() the display to put your work on screen
    pygame.display.flip()

pygame.quit()










