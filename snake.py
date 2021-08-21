#using pygame to make a snake game
#by: Matthew Barroso

from enum import Enum
from astropy.utils.xml import check
import pygame
import sys
import random
from pygame.locals import (
    K_UP,
    K_DOWN,
    K_LEFT,
    K_RIGHT,
    K_ESCAPE,
    KEYDOWN,
    QUIT,
)

#define colors
WHITE = (255,255,255)
BLACK = (0,0,0)
RED = (255,0,0)
GREEN = (0,255,0)
BLUE = (0,0,255)

pygame.init()

#make game states
class GameState(Enum):
    START = 0
    STARTING = 1
    PLAYING = 2
    GAME_OVER = 3

class Snake:
    def __init__(self) -> None:
        self.snake_size = 20
        
        self.block_size = 10
        self.snake = [(400, 240), (400, 240), (400, 240), (400, 240), (400, 240), (400, 240)]
        self.snake_length = 6
        self.direction = 0

    def draw_snake(self):
        for body in self.snake:
            pygame.draw.rect(screen, GREEN, (body[0], body[1], self.snake_size, self.snake_size))

    def move_snake(self):
        for i in range(self.snake_length - 1, 0, -1):
            self.snake[i] = self.snake[i - 1]
        if self.direction == 3:
            self.snake[0] = (self.snake[0][0] - self.snake_size, self.snake[0][1])
        elif self.direction == 4:
            self.snake[0] = (self.snake[0][0] + self.snake_size, self.snake[0][1])
        elif self.direction == 1:
            self.snake[0] = (self.snake[0][0], self.snake[0][1] - self.snake_size)
        elif self.direction == 2:
            self.snake[0] = (self.snake[0][0], self.snake[0][1] + self.snake_size)

    def increase_length(self):
        self.snake_length += 1
    
    def check_collision(self):
        global food
        global display_width, display_height
        global game_state
        if self.snake[0] in food: #if snake is at the same position as food, remove food and increase snake length
            self.increase_length()
            food.remove(self.snake[0])
            randomly_place_food()
            self.snake.append((-20, -20))
            return True
        elif snake.snake[0][0] < 20 or snake.snake[0][0] >= display_width - 20 or snake.snake[0][1] < 20 or snake.snake[0][1] >= display_height - 20:
            game_state = GameState.GAME_OVER
        elif self.snake[0] in self.snake[1:] and self.direction != 0:
            game_state = GameState.GAME_OVER

        return False



#set the width and height of the screen
size = display_width, display_height = 800, 600

#set the size of the font
font = pygame.font.SysFont(None, 25)

#make a screen
screen = pygame.display.set_mode(size)

#make a clock
clock = pygame.time.Clock()

#make a food
food = []
food_length = 1
food_width = 20
food_height = 20

#make a score
score = 0
high_score = 0

#make a start game message
# start_game_message_font_size = font.size("Press any key to start")
# start_game_message_font_color = WHITE

def game_start_message_display():
    screen.fill(WHITE)

    game_over_message_font = pygame.font.SysFont(None, 100)
    game_over_message = "Snake"
    game_over_message_size = game_over_message_font.size(game_over_message)
    game_over_message_x = (display_width / 2) - (game_over_message_size[0]) / 2
    game_over_message_y = (display_height / 2) - (game_over_message_size[1]) / 2 - 30
    game_over_message_position = [game_over_message_x, game_over_message_y]
    game_over_message_font_color = BLACK
    game_over_message_render = game_over_message_font.render(game_over_message, True, game_over_message_font_color)
    screen.blit(game_over_message_render, game_over_message_position)

    restart_message_font = pygame.font.SysFont(None, 60)
    restart_message = "Press any key to play"
    restart_message_size = restart_message_font.size(restart_message)
    restart_message_x = (display_width / 2) - (restart_message_size[0]) / 2
    restart_message_y = (display_height / 2) - (restart_message_size[1]) / 2 + 30
    restart_message_font_color = BLACK
    restart_message_render = restart_message_font.render(restart_message, True, restart_message_font_color)
    restart_message_position = [restart_message_x, restart_message_y]
    screen.blit(restart_message_render, restart_message_position)

    pygame.display.update()

def game_over_message_display():
    #make a game over message
    screen.fill(WHITE)

    game_over_message_font = pygame.font.SysFont(None, 100)
    game_over_message = "Game Over"
    game_over_message_size = game_over_message_font.size(game_over_message)
    game_over_message_x = (display_width / 2) - (game_over_message_size[0]) / 2
    game_over_message_y = (display_height / 2) - (game_over_message_size[1]) / 2 - 30
    game_over_message_position = [game_over_message_x, game_over_message_y]
    game_over_message_font_color = BLACK
    game_over_message_render = game_over_message_font.render(game_over_message, True, game_over_message_font_color)
    screen.blit(game_over_message_render, game_over_message_position)

    restart_message_font = pygame.font.SysFont(None, 60)
    restart_message = "Press any key to play again"
    restart_message_size = restart_message_font.size(restart_message)
    restart_message_x = (display_width / 2) - (restart_message_size[0]) / 2
    restart_message_y = (display_height / 2) - (restart_message_size[1]) / 2 + 30
    restart_message_font_color = BLACK
    restart_message_render = restart_message_font.render(restart_message, True, restart_message_font_color)
    restart_message_position = [restart_message_x, restart_message_y]
    screen.blit(restart_message_render, restart_message_position)

    pygame.display.update()
    

def draw_score(score):
    score_message = "Score: " + str(score)
    score_message_size = font.size(score_message)
    score_message_x = (60) - (score_message_size[0] / 2)
    score_message_y = (display_height - 10) - (score_message_size[1] / 2)
    score_message_position = [score_message_x, score_message_y]
    score_message_color = BLUE
    score_message_font = pygame.font.SysFont(None, 25)
    score_message_font_color = WHITE
    score_message_font_position = [score_message_x, score_message_y]
    score_message_font_size = score_message_font.size(score_message)
    score_message_font_rectangle = score_message_font.render(score_message, True, score_message_font_color)
    score_message_font_rectangle_position = [score_message_x, score_message_y]
    screen.blit(score_message_font_rectangle, score_message_font_rectangle_position)
    pygame.display.update()

def setup_game():
    global food
    global snake
    global score
    global high_score

    snake = Snake()
    food = []
    randomly_place_food()
    score = snake.snake_length
    high_score = 0

def randomly_place_food(): #randomly place food within border along a grid and make sure it is not in the snake
    global food
    global snake
    
    food = []
    while len(food) < food_length:
        food_x = int(random.randint(20, (display_width - 20))/20) * 20
        food_y = int(random.randint(20, (display_height - 20))/20) * 20
        if [food_x, food_y] not in snake.snake:
            food.append((food_x, food_y))
            print((food_x, food_y))
        
def draw_food():
    global food
    for x, y in food:
        pygame.draw.rect(screen, RED, [x, y, food_width, food_height])


game_state = GameState.START

running = True

while running:
    if game_state == GameState.START:
        game_start_message_display()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                game_state = GameState.STARTING
    elif game_state == GameState.STARTING:
        setup_game()
        game_state = GameState.PLAYING
    elif game_state == GameState.PLAYING:
        direction = snake.direction
        for event in pygame.event.get():
            if event.type == QUIT: 
                running = False
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    running = False
                if event.key == K_UP and direction != 2:
                    snake.direction = 1
                if event.key == K_DOWN and direction != 1:
                    snake.direction = 2
                if event.key == K_LEFT and direction != 4:
                    snake.direction = 3
                if event.key == K_RIGHT and direction != 3:
                    snake.direction = 4
        screen.fill(BLACK) #make the border black
        pygame.draw.rect(screen, BLUE, [20, 20, 760, 560]) #draw the foreground
        draw_food()
        draw_score(snake.snake_length)
        snake.draw_snake()
        snake.move_snake()
        snake.check_collision()
    elif game_state == GameState.GAME_OVER:
        game_over_message_display()
        for event in pygame.event.get():
            if event.type == QUIT: 
                running = False
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    running = False
                else:
                    game_state = GameState.STARTING
    pygame.display.flip()
    clock.tick(10)
    
