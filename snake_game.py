import pygame
import random
from collections import deque

# =========================
# CONFIGURAÇÕES GERAIS
# =========================
CELL_SIZE = 25
GRID_WIDTH = 30
GRID_HEIGHT = 20

WINDOW_WIDTH = GRID_WIDTH * CELL_SIZE
WINDOW_HEIGHT = GRID_HEIGHT * CELL_SIZE

FPS = 10

# =========================
# CORES
# =========================
BLACK = (0, 0, 0)
GREEN = (0, 200, 140)
RED = (200, 0, 140)
GRAY = (40, 40, 40)

# =========================
# DIREÇÕES
# =========================
UP = (0, -1)
DOWN = (0, 1)
LEFT = (-1, 0)
RIGHT = (1, 0)


OPPOSITE_DIRECTION = {
    UP: DOWN,
    DOWN: UP,
    LEFT: RIGHT,
    RIGHT: LEFT
}


# =========================
# FUNÇÕES DE LÓGICA
# =========================
def random_position(exclude):
    """Gera uma posição aleatória que não esteja em exclude"""
    while True:
        pos = (
            random.randint(0, GRID_WIDTH - 1),
            random.randint(0, GRID_HEIGHT - 1)
        )
        if pos not in exclude:
            return pos


def move_snake(snake, direction):
    """Move a cobra e retorna a nova cabeça"""
    head_x, head_y = snake[0]
    dx, dy = direction
    return (head_x + dx, head_y + dy)



def check_collision(position, snake_set):
    """Verifica colisão com parede ou corpo"""
    x, y = position

    if x < 0 or x >= GRID_WIDTH or y < 0 or y >= GRID_HEIGHT:
        return True

    if position in snake_set:
        return True

    return False


# =========================
# RENDERIZAÇÃO
# =========================
def draw_grid(screen):
    for x in range(0, WINDOW_WIDTH, CELL_SIZE):
        pygame.draw.line(screen, GRAY, (x, 0), (x, WINDOW_HEIGHT))
    for y in range(0, WINDOW_HEIGHT, CELL_SIZE):
        pygame.draw.line(screen, GRAY, (0, y), (WINDOW_WIDTH, y))


def draw_cell(screen, position, color):
    x, y = position
    rect = pygame.Rect(
        x * CELL_SIZE,
        y * CELL_SIZE,
        CELL_SIZE,
        CELL_SIZE
    )
    pygame.draw.rect(screen, color, rect)


def draw_game(screen, state):
    screen.fill(BLACK)

    draw_grid(screen)

    for segment in state["snake"]:
        draw_cell(screen, segment, GREEN)

    draw_cell(screen, state["food"], RED)

    pygame.display.flip()


# =========================
# LOOP PRINCIPAL
# =========================
def main():
    pygame.init()
    screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    pygame.display.set_caption("Snake - Estrutural")
    clock = pygame.time.Clock()

    # -------------------------
    # ESTADO DO JOGO
    # -------------------------
    state = {
        "snake": deque([(5, 5), (4, 5), (3, 5)]),
        "snake_set": {(5, 5), (4, 5), (3, 5)},
        "direction": RIGHT,
        "food": (10, 10),
        "running": True,
        "score": 0
    }

    state["food"] = random_position(state["snake_set"])

    # -------------------------
    # GAME LOOP
    # -------------------------
    while state["running"]:
        clock.tick(FPS)

        # INPUT
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                state["running"] = False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP and state["direction"] != DOWN:
                    state["direction"] = UP
                elif event.key == pygame.K_DOWN and state["direction"] != UP:
                    state["direction"] = DOWN
                elif event.key == pygame.K_LEFT and state["direction"] != RIGHT:
                    state["direction"] = LEFT
                elif event.key == pygame.K_RIGHT and state["direction"] != LEFT:
                    state["direction"] = RIGHT


        # ATUALIZAÇÃO
        new_head = move_snake(state["snake"], state["direction"])

        if check_collision(new_head, state["snake_set"]):
            print("Game Over!")
            print("Score:", state["score"])
            break

        state["snake"].appendleft(new_head)
        state["snake_set"].add(new_head)

        if new_head == state["food"]:
            state["score"] += 1
            state["food"] = random_position(state["snake_set"])
        else:
            tail = state["snake"].pop()
            state["snake_set"].remove(tail)

        # RENDER
        draw_game(screen, state)

    pygame.quit()


if __name__ == "__main__":
    main()