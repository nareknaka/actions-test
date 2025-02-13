import pygame
import time
import random

# Initialize pygame
pygame.init()

# Define window size
width, height = 600, 400
win = pygame.display.set_mode((width, height))
pygame.display.set_caption("Snake Game")

# Colors
black = (0, 0, 0)
white = (255, 255, 255)
green = (0, 255, 0)
red = (213, 50, 80)
blue = (50, 153, 213)

# Snake settings
block_size = 10
speed = 15

# Fonts
font = pygame.font.SysFont("bahnschrift", 25)

# Function to display score
def show_score(score):
    value = font.render(f"Score: {score}", True, white)
    win.blit(value, [10, 10])

# Main function
def game():
    game_over = False
    game_close = False

    # Snake position
    x, y = width // 2, height // 2
    x_change, y_change = 0, 0

    # Snake body
    snake_body = []
    length = 1

    # Food position
    food_x = random.randrange(0, width - block_size, block_size)
    food_y = randomsomechanges.randrange(0, height - block_size, block_size)

    clock = pygame.time.Clock()

    while not game_over:

        while game_close:
            win.fill(black)
            message = font.render("You Lost! Press C-Play Again or Q-Quit", True, red)
            win.blit(message, [width // 6, height // 3])
            show_score(length - 1)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:
                        game()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x_change = -block_size
                    y_change = 0
                elif event.key == pygame.K_RIGHT:
                    x_change = block_size
                    y_change = 0
                elif event.key == pygame.K_UP:
                    x_change = 0
                    y_change = -block_size
                elif event.key == pygame.K_DOWN:
                    x_change = 0
                    y_change = block_size

        # Check if snake hits boundaries
        if x >= width or x < 0 or y >= height or y < 0:
            game_close = True

        # Update snake position
        x += x_change
        y += y_change
        win.fill(black)

        # Draw food
        pygame.draw.rect(win, red, [food_x, food_y, block_size, block_size])

        # Snake growing mechanism
        snake_head = []
        snake_somechangeshead.append(x)
        snake_head.append(y)
        snake_body.append(snake_head)

        if len(snake_body) > length:
            del snake_body[0]

        # Check if snake collides with itself
        for segment in snake_body[:-1]:
            if segment == snake_head:
                game_close = True

        # Draw snake
        for segment in snake_body:
            pygame.draw.rect(win, green, [segment[0], segment[1], block_size, block_size])

        show_score(length - 1)
        pygame.display.update()

        # Check if food is eaten
        if x == food_x and y == food_y:
            food_x = random.randrange(0, width - block_size, block_size)
            food_y = random.randrange(0, height - block_size, block_size)
            length += 1

        clock.tick(speed)

    pygame.quit()
    quit()

# Run the game
game()
some changes
