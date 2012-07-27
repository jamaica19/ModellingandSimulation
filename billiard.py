import pygame
import sys
import math

pygame.init()
pygame.mouse.set_visible(True)
clock=pygame.time.Clock()
font=pygame.font.Font("freesansbold.ttf",32)

window=pygame.display.set_mode([800,600])
background_color=pygame.Color(220,20,60,255)

class Ball:
    def __init__(self):
        self.x=630
        self.y=270
        self.velocity_x=0
        self.velocity_y=0
        self.size=10
        self.color=pygame.Color(0,0,0)
    def update(self):
        self.x +=self.velocity_x
        self.y +=self.velocity_y

        self.velocity_x*=0.95
        self.velocity_y*=0.95
        self.x =int(self.x)
        self.y =int(self.y)

        if (self.x > 800):
            self.velocity_x *=-1
        if (self.x < 0):
            self.velocity_x = self.velocity_x * -1
        if (self.y < 0):
            self.velocity_y *=-1
        if (self.y>600):
            self.velocity_y *= -1
            
    def draw(self,window):
        pygame.draw.circle(window,self.color,[self.x,self.y],self.size)
ball=Ball()

class Ball2:
    def __init__(self):
        self.x=630
        self.y=320
        self.velocity_x=0
        self.velocity_y=0
        self.size=10
        self.color=pygame.Color(0,0,0)
    def update(self):
        self.x +=self.velocity_x
        self.y +=self.velocity_y

        self.velocity_x*=0.95
        self.velocity_y*=0.95
        self.x =int(self.x)
        self.y =int(self.y)

        if (self.x > 800):
            self.velocity_x *=-1
        if (self.x < 0):
            self.velocity_x = self.velocity_x * -1
        if (self.y < 0):
            self.velocity_y *=-1
        if (self.y>600):
            self.velocity_y *= -1
            
    def draw(self,window):
        pygame.draw.circle(window,self.color,[self.x,self.y],self.size)
ball2=Ball2()

class Ball3:
    def __init__(self):
        self.x=600
        self.y=300
        self.velocity_x=0
        self.velocity_y=0
        self.size=10
        self.color=pygame.Color(0,0,0)
    def update(self):
        self.x +=self.velocity_x
        self.y +=self.velocity_y

        self.velocity_x*=0.95
        self.velocity_y*=0.95
        self.x =int(self.x)
        self.y =int(self.y)

        if (self.x > 800):
            self.velocity_x *=-1
        if (self.x < 0):
            self.velocity_x = self.velocity_x * -1
        if (self.y < 0):
            self.velocity_y *=-1
        if (self.y>600):
            self.velocity_y *= -1
            
    def draw(self,window):
        pygame.draw.circle(window,self.color,[self.x,self.y],self.size)
ball3=Ball3()

class Ball4:
    def __init__(self):
        self.x=115
        self.y=320
        self.velocity_x=0
        self.velocity_y=0
        self.size=10
        self.color=pygame.Color(0,0,0)
    def update(self):
        self.x +=self.velocity_x
        self.y +=self.velocity_y

        self.velocity_x*=0.95
        self.velocity_y*=0.95
        self.x =int(self.x)
        self.y =int(self.y)

        if (self.x > 800):
            self.velocity_x *=-1
        if (self.x < 0):
            self.velocity_x = self.velocity_x * -1
        if (self.y < 0):
            self.velocity_y *=-1
        if (self.y>600):
            self.velocity_y *= -1
            
    def draw(self,window):
        pygame.draw.circle(window,self.color,[self.x,self.y],self.size)
ball4=Ball4()


while True:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            sys.exit()
    window.fill(background_color)

    mouse_pos=pygame.mouse.get_pos()
    msg="%i %i" % (mouse_pos[0], mouse_pos[1])
    text=font.render(msg, False, pygame.Color(0,0,0))
    window.blit(text,[0,0])


    
  
    ball.update()
    ball.draw(window)

    ball2.update()
    ball2.draw(window)

    ball3.update()
    ball3.draw(window)

    ball4.update()
    ball4.draw(window)

   
    pygame.display.update()
    clock.tick(30)
