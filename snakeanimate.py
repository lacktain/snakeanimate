from time import sleep
from sense_hat import SenseHat
import random

sense = SenseHat()
sense.set_rotation(180)

rx = random.randint(0,255)
gx = random.randint(0,255)
bx = random.randint(0,255)

y = (rx, gx, bx) 
b = (0, 0, 0) # Black
smiley_face = [
   y, y, y, y, y, y, y, y,
   y, y, y, y, y, y, y, y,
   y, b, b, y, y, b, b, y,
   y, b, b, y, y, b, b, y,
   y, y, y, y, y, y, y, y,
   y, b, b, b, b, b, b, y,
   y, y, y, b, b, y, y, y,
   y, y, y, y, y, y, y, y
]


kluss_face = [
   y, y, y, y, y, y, y, y,
   y, y, y, y, y, y, y, y,
   y, b, b, y, y, b, b, y,
   y, b, b, y, y, b, b, y,
   y, y, y, y, y, y, y, y,
   y, b, b, y, y, b, b, y,
   y, y, y, b, b, y, y, y,
   y, y, y, y, y, y, y, y
]


def kluss():
 count = 0
 while count < 63:
  rx = random.randint(0,255)
  gx = random.randint(0,255)
  bx = random.randint(0,255)

  y = (rx, gx, bx)

  kluss_face[count] = y 
  count += 1

 sense.set_pixels(kluss_face)
 sleep(0.1)
 return kluss_face


def initiatesnake():
 s = 0 
 n = 1
 a = 2
 k = 3
 e = 4

 snake = (s, n, a, k, e)  #SNAKE
 return snake

def setsnake(snake, go):
   
 #change first number, puch otherd down loss last)
   
 return snake
   

def putsnake(snake_face, snake):
 snakecolor = (0,0,0)
 #Swap spaces with snake
 for x in snake:
  y = snake[x]
  snake_face[y] = snakecolor
  print(y)
  #sense.set_pixels(snake_face)
  #sleep(0.5)
 return snake_face

def snakemove(snake):
 ri = [8, 16, 24, 32, 40, 48, 56, 64] #right illigal
 di = [64, 65, 66, 67, 68, 69, 70, 71] #down illigal
 li = [-1, 7, 15, 23, 31, 39, 47, 55] #left illigal
 ui = [-8, -7, -6, -5, -4, -3, -2, -1] #up illigal





 go = snake[0]
 n = 0
 direction = random.randint(0,3)
 if direction == 0:
  go += 1 #right
  if go in ri:
   False
  else:
   snake = setsnake(snake, go)
 elif direction == 1:
  go += 8 #down
 elif direction == 2:
  go -= 1 #LEft
 elif direction == 3:
  go -= 8 #up
 else:
  print("extream falure")
 return snake
 


def simusnake():
 snake_face = kluss()
 #nextstep():
 #set display
 count = 0
 while count < 63:
  rx = random.randint(0,255)
  gx = random.randint(0,255)
  bx = random.randint(0,255)

  y = (rx, gx, bx)

  snake_face[count] = y 
  count += 1
 
 snake = initiatesnake()
 snake_face = putsnake(snake_face, snake)
 sense.set_pixels(snake_face)
 sleep(1)

 count = 0
 while count < 25: #moves by snake
  
  sense.set_pixels(snake_face)
  sleep(0.3)
  snake = snakemove(snake)
  snake_face = putsnake(snake_face, snake)
  sense.set_pixels(snake_face)
  sleep(0.3)
  


 sleep(5)








simusnake()

 


count = 0
while count < 1000:
 #letters = ["E", "L", "I", "S", "E"]
 words = ["Lukas"]
 
 for x in words:
  r = random.randint(0,255)
  g = random.randint(0,255)
  b = random.randint(0,255)
  color = (r,g,b)
  print(x)
  sense.show_message(x, scroll_speed=.042, text_colour=color)
  #sense.show_letter(x, color)
  sleep(0.5)
 
 sense.clear()
 sense.set_pixels(smiley_face)
 count += 1
 print(count)
 sleep(2)
 tempfloat = sense.get_temperature()
 temp = round(tempfloat, 1)
 sense.show_message(str(temp))
 print(temp)
 for x in range(61):
  #print(kluss())
  sleep(0.02)

colorx = (255, 255, 0)
sense.show_message("Jippi", text_colour=colorx)
sense.clear()