from classes.Body import Body
from functions.calc import *
from functions.utils import *
from sys import exit
from os import environ

environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"

import pygame


bodies_num = 5
bodies = [get_random_body() for i in range(bodies_num)]
size = (650, 650)
color_black = (0, 0, 0)
color_white = (255, 255, 255)

pygame.init()
pygame.display.set_caption("Space Simulation by HYOUG")
screen = pygame.display.set_mode(size)


while True:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    
    
    for body_a in bodies:
        for body_b in bodies:
            if body_a is not body_b:
                gvector_ab = get_gvector(body_a, body_b)
                body_b.apply_force(gvector_ab, 1*10**6)
    
    
    screen.fill(color_black)
    for body in bodies:
        pygame.draw.circle(screen, body.color, (body.x, body.y), body.radius)
    pygame.display.flip()
        
    
    #print("\n".join([f'body num. {i} : ({bodies[i].x}, {bodies[i].y})' for i in range(len(bodies))]))
    #print("="*60)
    