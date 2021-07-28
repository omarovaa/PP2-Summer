#Libraries
import pygame
import random

pygame.init()
#Colors
BLACK = (0,0,0)
WHITE = (255,255,255)
RED = (255,0,0)
BLUE = (0,0,255)
GREEN = (0,255,0)

#Screen configurations
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 480

screen = pygame.display.set_mode((WINDOW_WIDTH,WINDOW_HEIGHT))

pygame.display.set_caption("Hungry Lion")

#FPS
clock = pygame.time.Clock()
FPS = 30

#Logical  variables
game_over = False

class Player:

    def __init__(self,*args,**kwargs):

        # Player's color
        self.color = BLUE

        # Size
        self.width = 30
        self.height = 25

        #Postion

        self.pos_x = (WINDOW_WIDTH / 2) - (self.width / 2)
        self.pos_y = WINDOW_HEIGHT - self.height

        #Player Rect 

        self.rect = pygame.Rect(self.pos_x,self.pos_y,self.width,self.height)
    

    #Controling player's position
    def move(self):

        controls = pygame.key.get_pressed()

        if controls[pygame.K_RIGHT] and self.pos_x <= (WINDOW_WIDTH - self.width - 5):
            player.pos_x += 5
        if controls[pygame.K_LEFT] and self.pos_x - 5 >= 0:
            player.pos_x -= 5
        if controls[pygame.K_UP] and self.pos_y -5 >= 0:
            player.pos_y -= 5
        if controls[pygame.K_DOWN] and self.pos_y <= (WINDOW_HEIGHT - self.height - 5):
            player.pos_y += 5

    def draw(self):
        pygame.draw.rect(screen,BLUE,(self.pos_x,self.pos_y,self.width,self.height))

class Enemy:

    def __init__(self,*args,**kwargs):

        #List of Enemies
        self.enemies = []
        #Colors
        self.color = RED

        #Size
        self.width = 30
        self.height = 25

        #Start Spawn
        for i in range(0,10 + random.randint(0,11)):
            pos_x = random.randint(0,WINDOW_WIDTH - self.width)
            pos_y = random.randint(0,WINDOW_HEIGHT - self.height)

            self.enemies.append([pos_x,pos_y,self.width,self.height])

    def move(self):
        for rect in self.enemies:
            rect[1] -= 5

    def detect_out_of_border(self):
        for rect in self.enemies:
            if rect[0] < 0:
                return True
        return False
    def spawn(self):
        for i in range(0,random.randint(0,3)):
            pos_x = random.randint(0,WINDOW_WIDTH - self.width)
            pos_y = random.randint(0,WINDOW_HEIGHT - self.height)

            self.enemies.append([pos_x,WINDOW_HEIGHT,self.width,self.height])    
    def draw(self):
        for rect in self.enemies:
            pygame.draw.rect(screen,self.color,rect)

#Full functionality of food
class Food:

    def __init__(self,*args,**kwargs):
        #List of food

        self.foods = []

        #Food's Color
        self.color = GREEN

        #Size
        self.width = 30
        self.height = 25
        
        #Directions
        self.directions = ['right','left','up','down']
    #Spawn random times
    def spawn(self):

        for i in range(0, 15 + random.randint(0,10)):
        
            pos_x = random.randint(0,WINDOW_WIDTH - self.width)
            pos_y = random.randint(0,WINDOW_HEIGHT - self.height)

            self.foods.append([pos_x,pos_y,self.width,self.height])
    #Shaking function
    def shake(self):
        for rect in self.foods:
            
            #Random shaking direction
            direction = random.choice(self.directions)
            #Limitator
            if rect[0] < 0:
                rect[0] += 5
            if rect[0] > WINDOW_WIDTH:
                rect[0] -= 5

            if rect[1] < 0:
                rect[1] += 5
            if rect[1] > WINDOW_HEIGHT:
                rect[1] -= 5
            #Shaking implementation
            if direction == 'right':
                rect[0] += 5
            if direction == 'left':
                rect[0] -= 5
            if direction == 'up':
                rect[1] -= 5
            if direction == 'down':
                rect[1] += 5
    #Draw
    def draw(self):
        for rect in self.foods:
            pygame.draw.rect(screen,self.color,rect)

#Class for global logics
class Logics:

    def isCollided(self,x1,y1,x2,y2):
        if x1 + 5 >= x2 and x1 <= x2 + 30:
            if y1 + 5 >= y2 and y1 <= y2 + 25:
                return True
        return False
    
points = 0

#Objects

player = Player()
food = Food()
enemy = Enemy()
logics = Logics()
#Outer game logic
food.spawn()
out_of_border = 0
# Main game loop

while not game_over:

    player_rect = pygame.Rect(player.pos_x,player.pos_y,player.width,player.height)

    for event in pygame.event.get():

        if event.type == pygame.QUIT:

            game_over = True

    #Logic
    player.move()
    enemy.move()
    if enemy.detect_out_of_border:
        out_of_border += 1
        if out_of_border % 5 == 0:
            enemy.spawn()
    food.shake()
        #Logics for collision between food and player
    for meal in food.foods:
        food_rect = pygame.Rect(meal[0],meal[1],meal[2],meal[3])
        if player_rect.colliderect(food_rect):
            points += 1
            food.foods.remove(meal)
        #Logics for collision between enemy and player
    for red in enemy.enemies:
        enemy_rect = pygame.Rect(red[0],red[1],red[2],red[3])
        if player_rect.colliderect(enemy_rect):
            points -= 1
            enemy.enemies.remove(red)
    if points < -1:

        game_over = True

    #Draw
    screen.fill(WHITE)
        #Showing score
    text = f"Score: {points}"
    font = pygame.font.Font(None,25)
    show_score = font.render(text,True,BLACK)
    screen.blit(show_score,(5,5))
    
    player.draw()
    enemy.draw()
    food.draw()
    pygame.display.flip()
    
    clock.tick(FPS)

#Test
print(food.foods)
pygame.quit()