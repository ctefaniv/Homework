import pygame
import sys
import random

pygame.init()
SIZE_BLOCK = 20
FRAME_COLOR = (0, 255, 150)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLACK = (0, 0, 0)
SNAKE_COLOR = (0, 102, 0)
HEADER_COLOR = (0, 255, 204)
HEADER_MARGIN = 70
MARGIN = 1
COUNT_BLOCKS = 20
size = [SIZE_BLOCK * COUNT_BLOCKS + 2 * SIZE_BLOCK + MARGIN * COUNT_BLOCKS,
        SIZE_BLOCK * COUNT_BLOCKS + 2 * SIZE_BLOCK + MARGIN * COUNT_BLOCKS + HEADER_MARGIN]

screen = pygame.display.set_mode(size)
pygame.display.set_caption("Snake")
timer = pygame.time.Clock()
courier = pygame.font.SysFont('courier', 36)


class SnakeBlock:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def is_inside(self):
        return 0 <= self.x < SIZE_BLOCK and 0 <= self.y < SIZE_BLOCK

    def __eq__(self, other):
        return isinstance(other, SnakeBlock) and self.x == other.x and self.y == other.y


def draw_block(color, row, col):
    pygame.draw.rect(screen, color, [SIZE_BLOCK + col * SIZE_BLOCK + MARGIN * (col + 1),
                                     HEADER_MARGIN + SIZE_BLOCK + row * SIZE_BLOCK + MARGIN * (row + 1),
                                     SIZE_BLOCK, SIZE_BLOCK])


def random_empty_block():
    x = random.randint(0, COUNT_BLOCKS - 1)
    y = random.randint(0, COUNT_BLOCKS - 1)
    empty_block = SnakeBlock(x, y)
    while empty_block in snake_blocks:
        empty_block.x = random.randint(0, COUNT_BLOCKS - 1)
        empty_block.y = random.randint(0, COUNT_BLOCKS - 1)
    return empty_block


snake_blocks = [SnakeBlock(9, 8), SnakeBlock(9, 9), SnakeBlock(9, 10)]
apple = random_empty_block()
d_row = 0
d_col = 1
score = 0
speed = 1

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            print("Quit")
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and d_col != 0:
                d_row = -1
                d_col = 0
            elif event.key == pygame.K_DOWN and d_col != 0:
                d_row = 1
                d_col = 0
            elif event.key == pygame.K_LEFT and d_row != 0:
                d_row = 0
                d_col = -1
            elif event.key == pygame.K_RIGHT and d_row != 0:
                d_row = 0
                d_col = 1

    screen.fill(FRAME_COLOR)
    pygame.draw.rect(screen, HEADER_COLOR, [0, 0, size[0], HEADER_MARGIN])
    text_score = courier.render(f"Score: {score}", True, BLACK)
    text_speed = courier.render(f"Speed: {speed}", True, BLACK)
    screen.blit(text_score, (SIZE_BLOCK, SIZE_BLOCK))
    screen.blit(text_speed, (SIZE_BLOCK + 230, SIZE_BLOCK))

    for row in range(COUNT_BLOCKS):
        for col in range(COUNT_BLOCKS):
            color = WHITE
            draw_block(color, row, col)

    head = snake_blocks[-1]
    if not head.is_inside():
        print("You crashed")
        pygame.quit()
        sys.exit()
    draw_block(RED, apple.x, apple.y)
    for block in snake_blocks:
        draw_block(SNAKE_COLOR, block.x, block.y)

    if apple == head:
        score += 1
        speed = score//5 + 1
        snake_blocks.append(apple)
        apple = random_empty_block()

    new_head = SnakeBlock(head.x + d_row, head.y + d_col)
    if new_head in snake_blocks:
        print("You crash yourself")
        pygame.quit()
        sys.exit()

    snake_blocks.append(new_head)
    snake_blocks.pop(0)

    pygame.display.flip()
    timer.tick(3 + speed)

