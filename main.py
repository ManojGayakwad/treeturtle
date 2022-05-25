from turtle import Turtle
#import turtle as turtle_module
#import random



#tim = turtle_module.Turtle()
#turtle_module.colormode(255)
#tim.penup()
tim =Turtle(shape='turtle')
#def random_color():
  #r = random.randint(0, 255)
  #g = random.randint(0, 255)
  #b = random.randint(0, 255)
  #random_color = (r, g, b)
  #return random_color
  
tim.color("darkgreen")
tim.left(90)
tim.width(4)
tim.speed(10)

def tree(size):
  if size < 5:
    return
  tim.forward(size)
  tim.left(30)
  tree(size * 3/4)
  tim.right(60)
  tree(size * 3/4)
  tim.left(30)
  tim.backward(size)
tree(50)
