import sys
import pygame
import random


pygame.init()
# Initialize pygame so it runs in the background and manages

screen = pygame.display.set_mode((800, 600))
# Creating a display
color = (255, 255, 255)
done = False
is_purple = True

def generate_obstacle():
  sz = random.randint(5, 30)
  obj = pygame.Rect(random.randint(0, 800 - sz), 0, sz, sz)
  return obj

x = 400
y = 300

player = pygame.Rect(x, y, 60, 60)
obstacles = [generate_obstacle()]
probability = .001

clock = pygame.time.Clock()

while not done:
  clock.tick(60)

  if random.random() < probability:
    obstacles.append(generate_obstacle())

  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      done = True

# Moving the icon
  pressed = pygame.key.get_pressed()
  if pressed[pygame.K_UP]: player.y -= 2
  if pressed[pygame.K_DOWN]: player.y += 2
  if pressed[pygame.K_LEFT]: player.x -= 2
  if pressed[pygame.K_RIGHT]: player.x += 2

  screen.fill((0,0,0))
  if is_purple:
    color = (255, 150, 255)
  pygame.draw.rect(screen, color, player)
 
  # Display the obstacle
  for obstacle in obstacles:
    obstacle.y += 1
    pygame.draw.rect(screen, pygame.Color("red"), obstacle)
    if obstacle.colliderect(player):
      done = True

  pygame.display.flip()