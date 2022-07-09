import pygame
import sys


def init_game():
    global mas
    mas = [[0] * 3 for i in range(3)]
    global query
    query = 0
    global game_over
    game_over = False


def check_win(field, sign):
    zeroes = 0
    for raw in field:
        zeroes += raw.count(0)
        if raw.count(sign) == 3:
            return sign
    for col in range(3):
        if field[0][col] == sign and field[1][col] == sign and field[2][col] == sign:
            return sign
    if field[0][0] == sign and field[1][1] == sign and field[2][2] == sign:
        return sign
    if field[0][2] == sign and field[1][1] == sign and field[2][0] == sign:
        return sign
    if zeroes == 0:
        return 'Draw'
    return False


pygame.init()

SIZE_BLOCK = 100
MARGIN = 15
width = height = SIZE_BLOCK * 3 + MARGIN * 4

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)

size_window = (width, height)
screen = pygame.display.set_mode(size_window)
pygame.display.set_caption('Крестики-нолики')

init_game()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        elif event.type == pygame.MOUSEBUTTONDOWN and not game_over:
            x_mouse, y_mouse = pygame.mouse.get_pos()
            print(f'x={x_mouse}, y={y_mouse}')
            column = x_mouse // (MARGIN + SIZE_BLOCK)
            row = y_mouse // (MARGIN + SIZE_BLOCK)
            if mas[row][column] == 0:
                if query % 2 == 0:
                    mas[row][column] = 'x'
                else:
                    mas[row][column] = 'o'
                query += 1
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            init_game()
            screen.fill(BLACK)

    if not game_over:
        for col in range(3):
            for row in range(3):
                if mas[row][col] == 'x':
                    color = RED
                elif mas[row][col] == 'o':
                    color = GREEN
                else:
                    color = WHITE
                x = col * SIZE_BLOCK + (col + 1) * MARGIN
                y = row * SIZE_BLOCK + (row + 1) * MARGIN
                pygame.draw.rect(screen, color, (x, y, SIZE_BLOCK, SIZE_BLOCK))

                if color == RED:
                    pygame.draw.line(screen, WHITE, (x + 5, y + 5),
                                     (x + SIZE_BLOCK - 5, y + SIZE_BLOCK - 5), 3)
                    pygame.draw.line(
                        screen, WHITE, (x + SIZE_BLOCK - 5, y + 5), (x + 5, y + SIZE_BLOCK - 5), 3)
                elif color == GREEN:
                    pygame.draw.circle(
                        screen, WHITE, (x + SIZE_BLOCK // 2, y + SIZE_BLOCK // 2), SIZE_BLOCK // 2 - 3, 3)

    if (query - 1) % 2 == 0:
        game_over = check_win(mas, 'x')
    else:
        game_over = check_win(mas, 'o')

    if game_over:
        screen.fill(BLACK)

        font = pygame.font.SysFont('stxingkai', 80)
        if game_over == 'Draw':
            text1 = font.render(game_over + '!!!', True, WHITE)
        else:
            text1 = font.render(game_over + ' is WIN!!!', True, WHITE)
        text1_rect = text1.get_rect()
        text_x = screen.get_width() / 2 - text1_rect.width / 2
        text_y = screen.get_height() / 2 - text1_rect.height / 2
        screen.blit(text1, [text_x, text_y])

        font = pygame.font.SysFont('stxingkai', 20)
        text2 = font.render('Press SPACE for new game...', True, WHITE)
        text2_rect = text2.get_rect()
        text2_x = screen.get_width() / 2 - text2_rect.width / 2
        text2_y = screen.get_height() - text2_rect.height - 5
        screen.blit(text2, [text2_x, text2_y])

    pygame.display.update()
