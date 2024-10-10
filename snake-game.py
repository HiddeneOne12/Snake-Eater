import pygame
import random
import os

pygame.init()
pygame.mixer.init()

# Colors Used In Game
whiteColor = (255, 255, 255)
redColor = (255, 0, 0)
blackColor = (0, 0, 0)
 
# Variables Used In Game
screen_width = 900
screen_height = 600
clock = pygame.time.Clock()
font = pygame.font.SysFont(None, 55)

# All Functions Used in Game
def text_screen(text, color, x, y):
    screen_text = font.render(text, True, color)
    game_window.blit(screen_text, [x, y])

def plot_snake(window, color, list, size):
    for x, y in list:
        pygame.draw.rect(window, color, [x, y, size, size])
       
def game_loop():
    game_background_image = pygame.image.load("snake-eater/images/game-background.jpg")
    game_background_image = pygame.transform.scale(game_background_image,(screen_width,screen_height)).convert_alpha()
    is_exit_game = False
    is_game_over = False
    snake_x = 45
    snake_y = 55
    snake_size = 20
    fps = 30
    velocity_x = 0
    velocity_y = 0
    food_x = random.randint(20, int(screen_width / 2))
    food_y = random.randint(20, int(screen_height / 2))
    score = 0
    initial_velocity = 5
    snake_list = []
    snake_length = 1
   
    # Checking if file exists
    if (not os.path.exists("high-score.txt")):
            with open("high-score.txt","w") as f:
               f.write("0")
        
    with open("high-score.txt","r") as f:
        hight_score = f.read()
        
    while not is_exit_game:
        if is_game_over:
            game_over_background_image = pygame.image.load("snake-eater/images/game-over-background.jpg")
            game_over_background_image = pygame.transform.scale(game_over_background_image,(screen_width,screen_height)).convert_alpha()
            with open("high-score.txt","w") as f:
                f.write(str(hight_score))
            game_window.fill(whiteColor)
            game_window.blit(game_over_background_image,(0,0))
            text_screen("Game Over! Press Enter to Restart", whiteColor, 150, 250)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    is_exit_game = True
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        welcome_screen()

        else:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    is_exit_game = True
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RIGHT:
                        velocity_x = initial_velocity
                        velocity_y = 0
                    if event.key == pygame.K_LEFT:
                        velocity_x = -initial_velocity
                        velocity_y = 0
                    if event.key == pygame.K_UP:
                        velocity_y = -initial_velocity
                        velocity_x = 0
                    if event.key == pygame.K_DOWN:
                        velocity_y = initial_velocity
                        velocity_x = 0

            snake_x += velocity_x
            snake_y += velocity_y

            if abs(snake_x - food_x) < 6 and abs(snake_y - food_y) < 6:
                score += 10
                food_x = random.randint(20, screen_width // 2)
                food_y = random.randint(20, screen_height // 2)
                snake_length += 5
                if score > int(hight_score):
                    hight_score = score

            game_window.fill(redColor)
            game_window.blit(game_background_image,(0,0))
            text_screen(f"Score: {score} ,  High Score : {hight_score}", whiteColor, 10, 10)
            pygame.draw.rect(game_window, redColor, [food_x, food_y, snake_size, snake_size])

            head = [snake_x, snake_y]
            snake_list.append(head)

            if len(snake_list) > snake_length:
                del snake_list[0]
            if head in snake_list[:-1]:
                is_game_over = True
                pygame.mixer.music.load("snake-eater/music/origins.mp3")
                pygame.mixer.music.play()               
            if snake_x < 0 or snake_x > screen_width or snake_y < 0 or snake_y > screen_height:               
                is_game_over = True
                pygame.mixer.music.load("snake-eater/music/origins.mp3")
                pygame.mixer.music.play()
            plot_snake(game_window, blackColor, snake_list, snake_size)

        pygame.display.update()
        clock.tick(fps)

    pygame.quit()
    quit()

def welcome_screen():
    welcome_background_image = pygame.image.load("snake-eater/images/start-background.jpg")
    welcome_background_image = pygame.transform.scale(welcome_background_image,(screen_width,screen_height)).convert_alpha()
    is_exit_game = False
    fps = 30
    pygame.mixer.music.load("snake-eater/music/rogue.mp3")
    pygame.mixer.music.play()
    while not is_exit_game:
        game_window.fill(whiteColor)
        game_window.blit(welcome_background_image,(0,0))
        text_screen("Welcome To Snake Eater", whiteColor, 400, 450)
        text_screen("Press Space to Play", whiteColor, 400, 500)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                    is_exit_game = True
            if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        pygame.mixer.music.load("snake-eater/music/ac3.mp3")
                        pygame.mixer.music.play()
                        game_loop()
        pygame.display.update()
        clock.tick(fps)

# Creating Game Window
game_window = pygame.display.set_mode((screen_width, screen_height))

# Creating Game Name
pygame.display.set_caption("Snake Eater By Abdullah Shamoon")

# Implementing Welcome Screen
welcome_screen()
