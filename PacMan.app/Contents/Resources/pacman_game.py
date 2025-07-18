import pygame
import sys
import random
import math

# Initialize Pygame
pygame.init()

# Constants
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600
CELL_SIZE = 20
MAZE_WIDTH = WINDOW_WIDTH // CELL_SIZE
MAZE_HEIGHT = WINDOW_HEIGHT // CELL_SIZE

# Colors
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
PINK = (255, 192, 203)
CYAN = (0, 255, 255)
ORANGE = (255, 165, 0)

# Game states
PLAYING = 0
GAME_OVER = 1
VICTORY = 2

class Maze:
    def __init__(self):
        # Create a simple maze layout (1 = wall, 0 = path, 2 = dot, 3 = power pellet)
        self.layout = [
            [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
            [1,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,1,1,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,1],
            [1,2,1,1,1,1,2,1,1,1,1,1,2,1,1,1,1,1,2,1,1,2,1,1,1,1,1,2,1,1,1,1,1,2,1,1,1,1,2,1],
            [1,3,1,1,1,1,2,1,1,1,1,1,2,1,1,1,1,1,2,1,1,2,1,1,1,1,1,2,1,1,1,1,1,2,1,1,1,1,3,1],
            [1,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,1],
            [1,2,1,1,1,1,2,1,1,2,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,2,1,1,2,1,1,1,1,2,1],
            [1,2,2,2,2,2,2,1,1,2,2,2,2,2,2,1,1,2,2,2,2,2,2,1,1,2,2,2,2,2,2,1,1,2,2,2,2,2,2,1],
            [1,1,1,1,1,1,2,1,1,1,1,1,0,0,0,1,1,2,1,1,1,1,2,1,1,0,0,0,1,1,1,1,1,2,1,1,1,1,1,1],
            [0,0,0,0,0,1,2,1,1,0,0,0,0,0,0,0,0,2,1,1,0,1,2,0,0,0,0,0,0,0,0,1,1,2,1,0,0,0,0,0],
            [1,1,1,1,1,1,2,1,1,0,1,1,1,0,0,0,1,1,1,1,0,1,1,1,1,0,0,0,1,1,1,0,1,1,2,1,1,1,1,1,1],
            [0,0,0,0,0,0,2,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,2,0,0,0,0,0,0],
            [1,1,1,1,1,1,2,1,1,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,1,1,2,1,1,1,1,1,1],
            [0,0,0,0,0,1,2,1,1,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,1,1,2,1,0,0,0,0,0],
            [1,1,1,1,1,1,2,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,2,1,1,1,1,1,1],
            [1,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,1,1,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,1],
            [1,2,1,1,1,1,2,1,1,1,1,1,2,1,1,1,1,1,2,1,1,2,1,1,1,1,1,2,1,1,1,1,1,2,1,1,1,1,2,1],
            [1,2,2,2,1,1,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,1,1,2,2,2,2,1],
            [1,1,1,2,1,1,2,1,1,2,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,2,1,1,2,1,1,2,1,1,1],
            [1,2,2,2,2,2,2,1,1,2,2,2,2,2,2,1,1,2,2,2,2,2,2,1,1,2,2,2,2,2,2,1,1,2,2,2,2,2,2,1],
            [1,2,1,1,1,1,1,1,1,1,1,1,2,1,1,1,1,1,2,1,1,2,1,1,1,1,1,2,1,1,1,1,1,1,1,1,1,1,2,1],
            [1,3,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,3,1],
            [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]
        ]
        
        # Adjust maze height to fit the layout
        global MAZE_HEIGHT
        MAZE_HEIGHT = len(self.layout)
        
    def is_wall(self, x, y):
        if x < 0 or x >= len(self.layout[0]) or y < 0 or y >= len(self.layout):
            return True
        return self.layout[y][x] == 1
    
    def is_dot(self, x, y):
        if x < 0 or x >= len(self.layout[0]) or y < 0 or y >= len(self.layout):
            return False
        return self.layout[y][x] == 2
    
    def is_power_pellet(self, x, y):
        if x < 0 or x >= len(self.layout[0]) or y < 0 or y >= len(self.layout):
            return False
        return self.layout[y][x] == 3
    
    def eat_dot(self, x, y):
        if 0 <= x < len(self.layout[0]) and 0 <= y < len(self.layout):
            if self.layout[y][x] in [2, 3]:
                self.layout[y][x] = 0
                return True
        return False
    
    def count_dots(self):
        count = 0
        for row in self.layout:
            for cell in row:
                if cell in [2, 3]:
                    count += 1
        return count
    
    def draw(self, screen):
        for y, row in enumerate(self.layout):
            for x, cell in enumerate(row):
                rect = pygame.Rect(x * CELL_SIZE, y * CELL_SIZE, CELL_SIZE, CELL_SIZE)
                if cell == 1:  # Wall
                    pygame.draw.rect(screen, BLUE, rect)
                elif cell == 2:  # Dot
                    pygame.draw.circle(screen, WHITE, rect.center, 2)
                elif cell == 3:  # Power pellet
                    pygame.draw.circle(screen, WHITE, rect.center, 6)

class Player:
    def __init__(self, x, y):
        self.start_x = x
        self.start_y = y
        self.x = x
        self.y = y
        self.direction = 0  # 0=right, 1=down, 2=left, 3=up
        self.next_direction = 0
        self.speed = 0.1
        self.move_timer = 0
        self.move_delay = 150  # milliseconds
        
    def update(self, maze, dt):
        self.move_timer += dt
        if self.move_timer >= self.move_delay:
            self.move_timer = 0
            
            # Try to change direction if requested
            next_x, next_y = self.get_next_position(self.next_direction)
            if not maze.is_wall(next_x, next_y):
                self.direction = self.next_direction
            
            # Move in current direction
            next_x, next_y = self.get_next_position(self.direction)
            if not maze.is_wall(next_x, next_y):
                self.x = next_x
                self.y = next_y
                
                # Handle screen wrapping
                if self.x < 0:
                    self.x = len(maze.layout[0]) - 1
                elif self.x >= len(maze.layout[0]):
                    self.x = 0
    
    def get_next_position(self, direction):
        next_x, next_y = self.x, self.y
        if direction == 0:  # Right
            next_x += 1
        elif direction == 1:  # Down
            next_y += 1
        elif direction == 2:  # Left
            next_x -= 1
        elif direction == 3:  # Up
            next_y -= 1
        return next_x, next_y
    
    def set_direction(self, direction):
        self.next_direction = direction
    
    def reset(self):
        self.x = self.start_x
        self.y = self.start_y
        self.direction = 0
        self.next_direction = 0
    
    def draw(self, screen):
        center_x = self.x * CELL_SIZE + CELL_SIZE // 2
        center_y = self.y * CELL_SIZE + CELL_SIZE // 2
        pygame.draw.circle(screen, YELLOW, (center_x, center_y), CELL_SIZE // 2 - 2)
        
        # Draw mouth
        mouth_angle = 30
        start_angle = self.direction * 90 + mouth_angle
        end_angle = self.direction * 90 - mouth_angle
        
        points = [(center_x, center_y)]
        for angle in range(int(start_angle), int(end_angle), -5):
            x = center_x + (CELL_SIZE // 2 - 2) * math.cos(math.radians(angle))
            y = center_y + (CELL_SIZE // 2 - 2) * math.sin(math.radians(angle))
            points.append((x, y))
        
        if len(points) > 2:
            pygame.draw.polygon(screen, BLACK, points)

class Ghost:
    def __init__(self, x, y, color):
        self.start_x = x
        self.start_y = y
        self.x = x
        self.y = y
        self.color = color
        self.direction = random.randint(0, 3)
        self.move_timer = 0
        self.move_delay = 200  # milliseconds
        self.scared_timer = 0
        self.scared_duration = 10000  # 10 seconds
        
    def update(self, maze, player, dt):
        if self.scared_timer > 0:
            self.scared_timer -= dt
            
        self.move_timer += dt
        if self.move_timer >= self.move_delay:
            self.move_timer = 0
            
            # Simple AI: try to move towards player when not scared
            if self.scared_timer <= 0:
                # Calculate direction towards player
                dx = player.x - self.x
                dy = player.y - self.y
                
                possible_directions = []
                if abs(dx) > abs(dy):
                    if dx > 0:
                        possible_directions.append(0)  # Right
                    else:
                        possible_directions.append(2)  # Left
                else:
                    if dy > 0:
                        possible_directions.append(1)  # Down
                    else:
                        possible_directions.append(3)  # Up
                
                # Add other directions as alternatives
                for d in [0, 1, 2, 3]:
                    if d not in possible_directions:
                        possible_directions.append(d)
                
                # Try directions in order of preference
                for direction in possible_directions:
                    next_x, next_y = self.get_next_position(direction)
                    if not maze.is_wall(next_x, next_y):
                        self.direction = direction
                        break
            else:
                # When scared, move randomly
                for _ in range(10):  # Try up to 10 random directions
                    direction = random.randint(0, 3)
                    next_x, next_y = self.get_next_position(direction)
                    if not maze.is_wall(next_x, next_y):
                        self.direction = direction
                        break
            
            # Move in current direction
            next_x, next_y = self.get_next_position(self.direction)
            if not maze.is_wall(next_x, next_y):
                self.x = next_x
                self.y = next_y
                
                # Handle screen wrapping
                if self.x < 0:
                    self.x = len(maze.layout[0]) - 1
                elif self.x >= len(maze.layout[0]):
                    self.x = 0
            else:
                # Change direction if hit wall
                self.direction = random.randint(0, 3)
    
    def get_next_position(self, direction):
        next_x, next_y = self.x, self.y
        if direction == 0:  # Right
            next_x += 1
        elif direction == 1:  # Down
            next_y += 1
        elif direction == 2:  # Left
            next_x -= 1
        elif direction == 3:  # Up
            next_y -= 1
        return next_x, next_y
    
    def make_scared(self):
        self.scared_timer = self.scared_duration
    
    def is_scared(self):
        return self.scared_timer > 0
    
    def reset(self):
        self.x = self.start_x
        self.y = self.start_y
        self.direction = random.randint(0, 3)
        self.scared_timer = 0
    
    def draw(self, screen):
        center_x = self.x * CELL_SIZE + CELL_SIZE // 2
        center_y = self.y * CELL_SIZE + CELL_SIZE // 2
        
        color = (0, 0, 255) if self.is_scared() else self.color
        
        # Draw ghost body
        pygame.draw.circle(screen, color, (center_x, center_y), CELL_SIZE // 2 - 2)
        
        # Draw ghost bottom (wavy)
        bottom_y = center_y + CELL_SIZE // 2 - 2
        points = []
        for i in range(CELL_SIZE):
            x = center_x - CELL_SIZE // 2 + i
            y = bottom_y - 3 * math.sin(i * 0.5)
            points.append((x, y))
        
        if len(points) > 1:
            pygame.draw.lines(screen, color, False, points, 3)
        
        # Draw eyes
        eye_size = 2
        left_eye_x = center_x - 4
        right_eye_x = center_x + 4
        eye_y = center_y - 4
        pygame.draw.circle(screen, WHITE, (left_eye_x, eye_y), eye_size)
        pygame.draw.circle(screen, WHITE, (right_eye_x, eye_y), eye_size)
        pygame.draw.circle(screen, BLACK, (left_eye_x, eye_y), 1)
        pygame.draw.circle(screen, BLACK, (right_eye_x, eye_y), 1)

class Game:
    def __init__(self):
        self.screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
        pygame.display.set_caption("PacMan Game")
        self.clock = pygame.time.Clock()
        self.font = pygame.font.Font(None, 36)
        
        self.reset_game()
        
    def reset_game(self):
        self.maze = Maze()
        self.player = Player(19, 15)  # Start position
        self.ghosts = [
            Ghost(19, 9, RED),
            Ghost(20, 9, PINK),
            Ghost(18, 9, CYAN),
            Ghost(21, 9, ORANGE)
        ]
        self.score = 0
        self.lives = 3
        self.game_state = PLAYING
        
    def handle_input(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                    self.player.set_direction(0)
                elif event.key == pygame.K_DOWN or event.key == pygame.K_s:
                    self.player.set_direction(1)
                elif event.key == pygame.K_LEFT or event.key == pygame.K_a:
                    self.player.set_direction(2)
                elif event.key == pygame.K_UP or event.key == pygame.K_w:
                    self.player.set_direction(3)
                elif event.key == pygame.K_r and self.game_state != PLAYING:
                    self.reset_game()
        return True
    
    def update(self, dt):
        if self.game_state != PLAYING:
            return
            
        # Update player
        self.player.update(self.maze, dt)
        
        # Check for dot collection
        if self.maze.is_dot(self.player.x, self.player.y):
            self.maze.eat_dot(self.player.x, self.player.y)
            self.score += 10
        elif self.maze.is_power_pellet(self.player.x, self.player.y):
            self.maze.eat_dot(self.player.x, self.player.y)
            self.score += 50
            # Make all ghosts scared
            for ghost in self.ghosts:
                ghost.make_scared()
        
        # Update ghosts
        for ghost in self.ghosts:
            ghost.update(self.maze, self.player, dt)
        
        # Check collisions with ghosts
        for ghost in self.ghosts:
            if ghost.x == self.player.x and ghost.y == self.player.y:
                if ghost.is_scared():
                    # Eat ghost
                    self.score += 200
                    ghost.reset()
                else:
                    # Player dies
                    self.lives -= 1
                    if self.lives <= 0:
                        self.game_state = GAME_OVER
                    else:
                        # Reset positions
                        self.player.reset()
                        for g in self.ghosts:
                            g.reset()
        
        # Check victory condition
        if self.maze.count_dots() == 0:
            self.game_state = VICTORY
    
    def draw(self):
        self.screen.fill(BLACK)
        
        # Draw maze
        self.maze.draw(self.screen)
        
        # Draw player
        self.player.draw(self.screen)
        
        # Draw ghosts
        for ghost in self.ghosts:
            ghost.draw(self.screen)
        
        # Draw UI
        score_text = self.font.render(f"Score: {self.score}", True, WHITE)
        lives_text = self.font.render(f"Lives: {self.lives}", True, WHITE)
        self.screen.blit(score_text, (10, WINDOW_HEIGHT - 60))
        self.screen.blit(lives_text, (10, WINDOW_HEIGHT - 30))
        
        # Draw game state messages
        if self.game_state == GAME_OVER:
            game_over_text = self.font.render("GAME OVER - Press R to restart", True, RED)
            text_rect = game_over_text.get_rect(center=(WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2))
            self.screen.blit(game_over_text, text_rect)
        elif self.game_state == VICTORY:
            victory_text = self.font.render("VICTORY! - Press R to restart", True, YELLOW)
            text_rect = victory_text.get_rect(center=(WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2))
            self.screen.blit(victory_text, text_rect)
        
        # Draw instructions
        if self.game_state == PLAYING:
            instruction_text = pygame.font.Font(None, 24).render("Use WASD or Arrow Keys to move", True, WHITE)
            self.screen.blit(instruction_text, (10, 10))
        
        pygame.display.flip()
    
    def run(self):
        running = True
        while running:
            dt = self.clock.tick(60)  # 60 FPS
            
            running = self.handle_input()
            self.update(dt)
            self.draw()
        
        pygame.quit()
        sys.exit()

if __name__ == "__main__":
    game = Game()
    game.run()