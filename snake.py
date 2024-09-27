import pygame
import time
import random

# Khởi tạo pygame
pygame.init()

# Kích thước màn hình
screen_width = 800
screen_height = 600

# Màu sắc
white = (255, 255, 255)
black = (0, 0, 0)
red = (213, 50, 80)
green = (0, 255, 0)
blue = (50, 153, 213)

# Thiết lập màn hình
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Snake Game')

# Thiết lập đồng hồ và tốc độ
clock = pygame.time.Clock()
snake_speed = 15

# Kích thước và màu sắc của con rắn
snake_block = 10

# Font chữ
font_style = pygame.font.SysFont("bahnschrift", 25)
score_font = pygame.font.SysFont("comicsansms", 35)

# Tính điểm
def Your_score(score):
    value = score_font.render("Score: " + str(score), True, black)
    screen.blit(value, [0, 0])

# Vẽ con rắn
def our_snake(snake_block, snake_list):
    for x in snake_list:
        pygame.draw.rect(screen, green, [x[0], x[1], snake_block, snake_block])

# Thông báo khi trò chơi kết thúc
def message(msg, color):
    mesg = font_style.render(msg, True, color)
    screen.blit(mesg, [screen_width / 6, screen_height / 3])

# Vòng lặp trò chơi
def gameLoop():
    game_over = False
    game_close = False

    # Khởi tạo vị trí của con rắn
    x1 = screen_width / 2
    y1 = screen_height / 2

    # Khởi tạo thay đổi vị trí
    x1_change = 0
    y1_change = 0

    # Khởi tạo chiều dài con rắn
    snake_List = []
    Length_of_snake = 1

    # Tạo thức ăn ban đầu
    foodx = round(random.randrange(0, screen_width - snake_block) / 10.0) * 10.0
    foody = round(random.randrange(0, screen_height - snake_block) / 10.0) * 10.0

    while not game_over:

        while game_close == True:
            screen.fill(blue)
            message("You Lost! Press C-Play Again or Q-Quit", red)
            Your_score(Length_of_snake - 1)
            pygame.display.update()

            # Sự kiện khi trò chơi kết thúc
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:
                        gameLoop()

        # Điều khiển con rắn
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x1_change = -snake_block
                    y1_change = 0
                elif event.key == pygame.K_RIGHT:
                    x1_change = snake_block
                    y1_change = 0
                elif event.key == pygame.K_UP:
                    y1_change = -snake_block
                    x1_change = 0
                elif event.key == pygame.K_DOWN:
                    y1_change = snake_block
                    x1_change = 0

        # Kiểm tra nếu con rắn va vào biên
        if x1 >= screen_width or x1 < 0 or y1 >= screen_height or y1 < 0:
            game_close = True

        # Cập nhật vị trí của con rắn
        x1 += x1_change
        y1 += y1_change
        screen.fill(blue)

        # Vẽ thức ăn
        pygame.draw.rect(screen, red, [foodx, foody, snake_block, snake_block])
        
        # Cập nhật vị trí con rắn
        snake_Head = []
        snake_Head.append(x1)
        snake_Head.append(y1)
        snake_List.append(snake_Head)
        if len(snake_List) > Length_of_snake:
            del snake_List[0]

        # Kiểm tra nếu con rắn va vào chính nó
        for x in snake_List[:-1]:
            if x == snake_Head:
                game_close = True

        # Vẽ con rắn
        our_snake(snake_block, snake_List)
        Your_score(Length_of_snake - 1)

        pygame.display.update()

        # Kiểm tra nếu con rắn ăn thức ăn
        if x1 == foodx and y1 == foody:
            foodx = round(random.randrange(0, screen_width - snake_block) / 10.0) * 10.0
            foody = round(random.randrange(0, screen_height - snake_block) / 10.0) * 10.0
            Length_of_snake += 1

        clock.tick(snake_speed)

    pygame.quit()
    quit()

gameLoop()
