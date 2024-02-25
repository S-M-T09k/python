import pygame, sys

pygame.init()
clock = pygame.time.Clock()

width, height = 1000, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Pong")

ball = pygame.Rect((width/2) - 5, (height/2) - 5, 10, 10)
player = pygame.Rect(10, (height/2) - 50, 10, 100)
opponent = pygame.Rect(width - 20, (height/2) - 50, 10, 100)

bgColor = pygame.Color('grey12')
ballColor = pygame.Color(0, 255, 0)
playerColor = pygame.Color(255, 255, 255)
lightGrey = pygame.Color(200, 200, 200)

ballX = 5
ballY = 5
playerY = 0
opponentY = 10


def animateBall():
  global ballX, ballY
  ball.x += ballX
  ball.y += ballY

  if ball.top <= 0 or ball.bottom >= height:
    ballY *= -1
  if ball.left <= 0 or ball.right >= width:
    ball.center = (width/2, height/2)
  if ball.colliderect(player) or ball.colliderect(opponent):
    ballX *= -1

def animatePlayer():
  player.y += playerY

  if player.top <= 0:
    player.top = 0
  if player.bottom >= height:
    player.bottom = height

def animateOpponent():
  if opponent.top < ball.y:
    opponent.y += opponentY
  if opponent.bottom > ball.y:
    opponent.y -= opponentY
    
  if opponent.top <= 0:
    opponent.top = 0
  if opponent.bottom >= height:
    opponent.bottom = height
  
  
while True:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      pygame.quit()
      sys.exit()
      
  screen.fill(bgColor)
  pygame.draw.ellipse(screen, ballColor, ball)
  pygame.draw.rect(screen, playerColor, player)
  pygame.draw.rect(screen, playerColor, opponent)
  pygame.draw.aaline(screen, lightGrey, (width/2,0), (width/2, height))

  if event.type == pygame.KEYDOWN:
    if event.key == pygame.K_UP:
      playerY -= 3
    if event.key == pygame.K_DOWN:
      playerY += 3

  if event.type == pygame.KEYUP:
    if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
      playerY = 0
  
  animateBall()
  animatePlayer()
  animateOpponent()

  pygame.display.flip()

  clock.tick(60)
