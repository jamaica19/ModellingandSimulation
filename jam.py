import pygame
import sys
import math
import random

pygame.init()
pygame.mouse.set_visible(True)
font = pygame.font.Font("freesansbold.ttf", 32)


clock = pygame.time.Clock()
window = pygame.display.set_mode([800,600])
background_color = pygame.Color(240,25,255)

class Mother_Ball:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.velocity_x = 0
        self.velocity_y = 0
        self.size = 30
        self.color = pygame.Color(255,255,255)

    def update(self):
        
        self.x += self.velocity_x
        self.y += self.velocity_y

        self.velocity_x *= 0.99
        self.velocity_y *= 0.99

        self.x = int(self.x)
        self.y = int(self.y)

        if (self.x > 800):
            self.velocity_x *=-1
        if (self.x < 0):
            self.velocity_x = self.velocity_x * -1

        if (self.y < 0):
            self.velocity_y *=-1
        if (self.y > 600):
            self.velocity_y *=-1
        
    def draw(self, window):
        pygame.draw.circle(window, self.color, [self.x, self.y], self.size)


class Ball:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.velocity_x = 0
        self.velocity_y = 0
        self.size = 30
        self.color = pygame.Color(0,0,0)

    def update(self):
        
        self.x += self.velocity_x
        self.y += self.velocity_y

        self.velocity_x *= 0.99
        self.velocity_y *= 0.99

        self.x = int(self.x)
        self.y = int(self.y)

        if (self.x > 800):
            self.velocity_x *=-1
        if (self.x < 0):
            self.velocity_x = self.velocity_x * -1

        if (self.y < 0):
            self.velocity_y *=-1
        if (self.y > 600):
            self.velocity_y *=-1
        
    def draw(self, window):
        pygame.draw.circle(window, self.color, [self.x, self.y], self.size)

def checkcollision(ball1, ball2):
    origin_x=ball2.x-ball1.x
    origin_y=ball2.y-ball1.y
    distance=(origin_x*origin_x)+(origin_y*origin_y)
    combined_radius=(ball1.size+ball2.size)
    circle_distance=combined_radius*combined_radius
    return (distance <=circle_distance)

def CollideReaction (ball1, ball2):
    #move to origin
        origin_x = ball2.x - ball1.x
        origin_y = ball2.y - ball1.y
        #find distance to origin (pythagorean)
        distance = math.sqrt(origin_x * origin_x + origin_y * origin_y)
        if (distance==0):
            distance=1
        #normalize
        normal_x = origin_x / distance
        normal_y = origin_y / distance

        #invert normal
        #normal_mouse_x *=-1
        #normal_mouse_y *=-1

        #move ball away from cursor, using the inverted normal
        ball2.velocity_x =  ball1.velocity_x *normal_x
        ball2.velocity_y =  ball1.velocity_y *normal_y

        #reflect ball1(inverted velocity)
        ball1.velocity_x*= -normal_x
        ball1.velocity_y*=-normal_y

        ball1.update()
        ball2.update()

class Table:
    def __init__(self):
        self.TableRect=pygame.Rect(60,100,700,450)
        self.color=(0,0,0,)
        self.x =82
        self.y=120
        self.size=30
    def draw(self,window):
        
        pygame.draw.rect(window,pygame.Color("White"),self.TableRect,4)
        pygame.draw.circle(window, background_color, [self.x, self.y], self.size)
        pygame.draw.circle(window, background_color, [745,120], self.size)
        pygame.draw.circle(window, background_color, [82,550 ], self.size)
        pygame.draw.circle(window, background_color, [745, 550], self.size)
    
    def CheckCollision(self,ball):
        #check top
        if(ball.y-ball.size < self.TableRect.top):
            ball.velocity_y *= -1
            ball.y=self.TableRect.top + ball.size
            
        #check left
        if(ball.x-ball.size < self.TableRect.left):
            ball.velocity_x *=-1
            ball.x=self.TableRect.left + ball.size
            
        #chek right
        if(ball.x+ball.size > self.TableRect.right):
            ball.velocity_x *=-1
            ball.x=self.TableRect.right - ball.size
            
        #check bottom
        if(ball.y+ball.size > self.TableRect.bottom):
            ball.velocity_y *=-1
            ball.y =self.TableRect.bottom -ball.size
            



    
PoolTable=Table()



    


motherball = Mother_Ball(90,300)
list_of_balls = [Ball(300,300),Ball(400,250),Ball(400,350),Ball(500,200),Ball(500,300),Ball(500,400)]


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
             pygame.quit()
             sys.exit()

    window.fill(background_color)

    mouse_pos = pygame.mouse.get_pos()
    msg = "%i %i" %(mouse_pos[0],mouse_pos[1])
    text = font .render(msg, False, pygame.Color(0,0,0))
    window.blit(text,[0,0])

    if (pygame.mouse.get_pressed()[0] == True):
        #for ball in list_of_balls:
            #move to origin
            #origin_mouse_x = mouse_pos[0] - ball.x
            #origin_mouse_y = mouse_pos[1] - ball.y
            #find distance to origin (pythagorean)
            #distance = math.sqrt(origin_mouse_x * origin_mouse_x + origin_mouse_y * origin_mouse_y)

            #normalize
            #normal_mouse_x = origin_mouse_x / distance
            #normal_mouse_y = origin_mouse_y / distance

            #invert normal
            #normal_mouse_x *=-1
            #normal_mouse_y *=-1

            #move ball away from cursor, using the inverted normal
            #ball.velocity_x += normal_mouse_x * 2.5
            #ball.velocity_y += normal_mouse_y * 2.5

        #move to origin
        origin_mouse_x = mouse_pos[0] - motherball.x
        origin_mouse_y = mouse_pos[1] - motherball.y
        #find distance to origin (pythagorean)
        distance = math.sqrt(origin_mouse_x * origin_mouse_x + origin_mouse_y * origin_mouse_y)

        #normalize
        normal_mouse_x = origin_mouse_x / distance
        normal_mouse_y = origin_mouse_y / distance

        #invert normal
        #normal_mouse_x *=-1
        #normal_mouse_y *=-1

        #move ball away from cursor, using the inverted normal
        motherball.velocity_x += normal_mouse_x * 2.5
        motherball.velocity_y += normal_mouse_y * 2.5

    for ball in list_of_balls:
        ball.update()
        if(checkcollision(motherball,ball)==True):
            CollideReaction(motherball,ball)
    for ball1 in list_of_balls:
        for ball2 in list_of_balls:
            if(ball1!=ball2):
                if(checkcollision(ball1,ball2)):
                    CollideReaction(ball1,ball2)
    PoolTable.CheckCollision(motherball)
    for ball in list_of_balls:
        PoolTable.CheckCollision(ball)
        
    

    
    motherball.update()
    motherball.draw(window)
        
    for ball in list_of_balls:    
        ball.update()
        
        ball.draw(window)
    PoolTable.draw(window)

    
    pygame.display.update()
    clock.tick(30)
