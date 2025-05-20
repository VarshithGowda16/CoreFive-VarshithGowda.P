# food.py
import pygame
import random

class Food:
    def __init__(self, block_size, screen_width, screen_height):
        self.block_size = block_size
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.types = {
            "normal": (255, 0, 0),     # red
            "special": (255, 255, 0),  # yellow
        }
        self.position = self.generate_position()
        self.type = "normal"
        self.spawn_timer = 0
        self.special_food_duration = 100  # frames

    def generate_position(self):
        """Generate a grid-aligned position within bounds"""
        x = random.randint(0, (self.screen_width - self.block_size) // self.block_size) * self.block_size
        y = random.randint(0, (self.screen_height - self.block_size) // self.block_size) * self.block_size
        return (x, y)

    def spawn(self, is_special=False):
        self.position = self.generate_position()
        self.type = "special" if is_special else "normal"
        self.spawn_timer = 0

    def draw(self, screen):
        color = self.types.get(self.type, (255, 0, 0))
        pygame.draw.rect(screen, color, pygame.Rect(self.position[0], self.position[1], self.block_size, self.block_size))

    def update(self):
        if self.type == "special":
            self.spawn_timer += 1
            if self.spawn_timer > self.special_food_duration:
                self.spawn(False)

    def check_collision(self, snake_head):
        return snake_head == self.position

    def get_type(self):
        return self.type

    def get_position(self):
        return self.position

    def get_color(self):
        return self.types.get(self.type, (255, 0, 0))

    def is_special(self):
        return self.type == "special"

    def set_special_timer(self, duration):
        self.special_food_duration = duration

    def despawn(self):
        """For example, if special food expires without being eaten"""
        self.type = "normal"
        self.spawn()

# Example usage:
if __name__ == "__main__":
    pygame.init()
    screen = pygame.display.set_mode((400, 300))
    clock = pygame.time.Clock()
    food = Food(20, 400, 300)

    running = True
    while running:
        screen.fill((0, 0, 0))
        food.update()
        food.draw(screen)
        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        clock.tick(10)

    pygame.quit()
