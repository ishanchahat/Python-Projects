#Snake Game

import math
import random
import pygame
import tkinter as tk
from tkinter import messagebox

class cube(object):
    row = 20
    w = 500
    def __init__(self,start,dirnx=1,dirny=0,color=(255,0,0)):
        self.pos = start
        self.dirnx = 1
        self.dirny = 0
        self.color = color
        
        
    def move(self,dirnx,dirny):
        self.dirnx = dirnx
        self.dirny = dirny
        self.pos=(self.pos[0] + self.dirnx, self.pos[1] + self.dirny)
    
    
    def draw(self,surface,eyes=0):
        dis = self.w// self.row
        i = self.pos[0] #i stands for rows
        j = self.pos[1] #j stands for columns
        
        pygame.draw.rect(surface, self.color, (i*dis+1,j*dis+1, dis-2,dis-2)) # so that we can still see the grid when we draw our rectangle
        if eyes:
            center = dis//2
            radius = 3
            circleMiddle = (i*dis+center-radius,j*dis+8)
            circleMiddle2 = (i*dis + dis-radius*2, j*dis+8)
            pygame.draw.circle(surface, (0,0,0), circleMiddle, radius)
            pygame.draw.circle(surface, (0,0,0), circleMiddle2, radius)
    
class snake(object):
    body = []
    turns = {}
    
    def __init__(self,color,pos):
        self.color = color
        self.head = cube(pos)
        self.body.append(self.head)
        self.dirnx = 0 #This implies the direction for x for the snake
        self.dirny = 1 #This implies the direction for y for the snake
    def move(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            keys  = pygame.key.get_pressed()
            
            for key in keys:
                if keys[pygame.K_LEFT]:
                    self.dirnx = -1
                    self.dirny = 0
                    self.turns[self.head.pos[:]] = [self.dirnx, self.dirny]
                    
                elif keys[pygame.K_RIGHT]:
                    if keys[pygame.K_LEFT]:
                        self.dirnx = 1                                               
                        self.dirny = 0
                        self.turns[self.head.pos[:]] = [self.dirnx, self.dirny]
                    
                    
                elif keys[pygame.K_UP]:
                    if keys[pygame.K_LEFT]:
                        self.dirnx = 0
                        self.dirny = -1
                        self.turns[self.head.pos[:]] = [self.dirnx, self.dirny]
                    
                elif keys[pygame.K_DOWN]:
                    if keys[pygame.K_LEFT]:
                        self.dirnx = 0
                        self.dirny = 1
                        self.turns[self.head.pos[:]] = [self.dirnx, self.dirny]
                        
            for i,c in enumerate(self.body):
                p = c.pos[:]
                if p in self.turns:
                    turn = self.turns[p]
                    c.move(turn[0], turn[1])
                    if i == len(self.body) - 1:
                        self.turns.pop(p)
                #For checking whether or not we have moved to the edge of the screen or not
                else:
                    if c.dirnx == -1 and c.pos[0] <=0: c.pos = (c.row-1 , c.pos[1])
                    elif c.dirnx == 1 and c.pos[0] >=c.row-1: c.pos = (0 , c.pos[1])
                    elif c.dirnx == 1 and c.pos[1] >=c.row-1: c.pos = (c.pos[0] , 0)
                    elif c.dirnx == -1 and c.pos[1] <=0: c.pos = (c.pos[0] , c.row-1)
                    else: c.move(c.dirnx,c.dirny)
                    
                    
                
    def reset(self,pos):
        pass
    def addCube(self):
        pass
    def draw(self,surface):
        for i, c in enumerate(self.body):
            if i==0:
                c.draw(surface, True)
            else: 
                c.draw(surface)
    
def drawGrid(w,rows,surface):
    #Figuring out how big a square is in each grid is. We are drawing lines and positioning them to make a square
    sizeBtwn = w // rows #// to avoid large decimals numbers because we cannot draw squares for them
    
    x = 0
    y = 0
    for l in range(rows):
        x = x + sizeBtwn
        y = y + sizeBtwn
        
        #draws two lines for every loop, drawing the white line for grid for every time the loops runs
        pygame.draw.line(surface, (255,255,255), (x,0),(x,w)) #this is for all the horizontal lines for the grid
        pygame.draw.line(surface, (255,255,255), (0,y),(w,y))#this is for all the vertical lines of the grid
        
    
    


def redrawWindow(surface):
    global rows, width,s
    surface.fill((0,0,0))#for filling the screen
    s.draw(surface)
    drawGrid(width,rows,surface)
    pygame.display.update()
def randomSnack(rows,items):
    pass
def message_box(subject,content):
    pass
def main():
    global width, rows,s
    width = 500
    rows = 20
    win = pygame.display.set_mode((width,width))
    s = snake((255,0,0), (10,10)) #deciding color and position of the snake when the game starts
    clock = pygame.time.Clock()
    #Main Loop
    flag = True
    while flag:
        pygame.time.delay(50) #detemines delay so my program do not run too fast
        clock.tick(10) #It determines on how much frame my game will work.Meaning that the snake will move 10 blocks in 1 second
        s.move()
        redrawWindow(win)    
    
    
    
    pass




main()    