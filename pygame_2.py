###########################
# OOP Formative - Attempt 2
# Reid A. Martin
# 
###########################
#
# 1
# OOP uses classes and methods so that it can do code for specific objects or objects with similar atributes 
# (like dots or blobs with different colors). You can pass arguments into them and make everything apply to different
# objects.
# 2
# This could technically be done with iteration... but WHY WOULD YOU WANT TO DO THAT TO YOURSELF
#
###########################

import random
import pygame
from os import path
import time

###########################

WIDTH = 1820
HEIGHT = 980

BLACK = (0, 0, 0)
GREEN = (3, 160, 98)
BLUE = (0, 128, 128)
RED = (255, 0, 0)
YELLOW = (255, 215, 0)

###########################

green_dot = 10 #random.randrange(0, 10)
blue_dot = 10 #random.randrange(0, 10)
red_dot = 10 #random.randrange(0, 10)
player_dot = 1

###########################

print("You are the yellow dot. Have fun! ")
time.sleep(2)
print("enjoy the music..... hehehhe")
time.sleep(2)

###########################

game_folder = path.dirname(__file__)
snd_dir = path.join(game_folder, 'snd')

pygame.mixer.init()
music = pygame.mixer.music.load(path.join(snd_dir, 'never_good.wav'))
pygame.mixer.music.set_volume(0.5)

game_display = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("good music dots")
clock = pygame.time.Clock()

###########################

class MainDots():
    
    def __init__(self, color):
        self.size = (15)
        self.color = color
        self.x = random.randrange(0, 1820, 25)
        self.y = random.randrange(0, 980, 25)
        
    def move_player(self):
        for event in pygame.event.get():
            if event.type == 'QUIT':
                pygame.quit()
                quit()
            elif event.type  == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    self.x = self.x - 25
                if event.key == pygame.K_RIGHT:
                    self.x = self.x + 25
                if event.key == pygame.K_UP:
                    self.y = self.y - 25
                if event.key == pygame.K_DOWN:
                    self.y = self.y + 25
                
            if self.x < 0: self.x = 0
            elif self.x > WIDTH: self.x = WIDTH
        
            if self.y < 0: self.y = 0
            elif self.y > HEIGHT: self.y = HEIGHT
                

def draw_env_dots(dot_list):
    game_display.fill(BLACK)

    for dot_dict in dot_list:
        for dot_id in dot_dict:
            dot = dot_dict[dot_id]
            pygame.draw.circle(game_display, dot.color, [dot.x, dot.y], dot.size)
            if dot.color == YELLOW:
                dot.move_player()

    pygame.display.update()
    
def main():
    
    blue_dots = dict(enumerate([MainDots(BLUE) for i in range(blue_dot)]))
    red_dots = dict(enumerate([MainDots(RED) for i in range(red_dot)]))
    green_dots = dict(enumerate([MainDots(GREEN) for i in range(green_dot)]))
    player = dict(enumerate([MainDots(YELLOW) for i in range(player_dot)]))
    
    pygame.mixer.music.play()
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
         
        clock.tick(120)
        draw_env_dots([player, blue_dots, red_dots, green_dots])
        
        
main()