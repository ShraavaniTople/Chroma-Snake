import pygame
import random

# Initialize Pygame
pygame.init()

# Constants
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
CELL_SIZE = 20
FPS = 10

# Colors
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# Direction vectors
UP = (0, -1)
DOWN = (0, 1)
LEFT = (-1, 0)
RIGHT = (1, 0)

# Snake class
class Snake:
    def __init__(self):
        self.body = [(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)]
        self.direction = random.choice([UP, DOWN, LEFT, RIGHT])
        self.color = GREEN

    def move(self):
        head = self.body[0]
        new_head = (head[0] + self.direction[0] * CELL_SIZE, head[1] + self.direction[1] * CELL_SIZE)
        self.body.insert(0, new_head)

    def draw(self, screen):
        for segment in self.body:
            pygame.draw.rect(screen, self.color, (segment[0], segment[1], CELL_SIZE, CELL_SIZE))

# Food class
class Food:
    def __init__(self):
        self.position = (random.randint(0, SCREEN_WIDTH // CELL_SIZE - 1) * CELL_SIZE,
                         random.randint(0, SCREEN_HEIGHT // CELL_SIZE - 1) * CELL_SIZE)
        self.color = RED

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, (self.position[0], self.position[1], CELL_SIZE, CELL_SIZE))

# Game class
class EvoSnakeGame:
    def __init__(self):
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption("EvoSnake")
        self.clock = pygame.time.Clock()
        self.snake = Snake()
        self.food = Food()
        self.score = 0

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.quit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP and self.snake.direction != DOWN:
                    self.snake.direction = UP
                elif event.key == pygame.K_DOWN and self.snake.direction != UP:
                    self.snake.direction = DOWN
                elif event.key == pygame.K_LEFT and self.snake.direction != RIGHT:
                    self.snake.direction = LEFT
                elif event.key == pygame.K_RIGHT and self.snake.direction != LEFT:
                    self.snake.direction = RIGHT

    def update(self):
        self.snake.move()
        if self.snake.body[0] == self.food.position:
            self.snake.color = random.choice([GREEN, BLUE])  # Snake changes color when it eats food
            self.score += 1
            self.food.position = (random.randint(0, SCREEN_WIDTH // CELL_SIZE - 1) * CELL_SIZE,
                                  random.randint(0, SCREEN_HEIGHT // CELL_SIZE - 1) * CELL_SIZE)
        else:
            self.snake.body.pop()

    def draw(self):
        self.screen.fill(WHITE)
        self.snake.draw(self.screen)
        self.food.draw(self.screen)
        pygame.display.flip()

    def run(self):
        running = True
        while running:
            self.handle_events()
            self.update()
            self.draw()
            self.clock.tick(FPS)

    def quit(self):
        pygame.quit()
        quit()

# Main function
def main():
    game = EvoSnakeGame()
    game.run()

if __name__ == "__main__":
    main()
