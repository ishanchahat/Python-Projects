#Snake Game

import math
import random
import pygame
import tkinter as tk
from tkinter import messagebox

class cube(object):
    row = 0
    w = 0
    def __init__(self,start,dirnx=0,dirny=0,color=(255,0,0)):
        pass
    def move(self,dirnx,dirny):
        pass
    def draw(self,surface,eyes=0):
        pass
    
class snake(object):
    def __init__(self,color,pos):
        pass
    def move(self):
        pass
    def reset(self,pos):
        pass
    def addCube(self):
        pass
    def draw(self,surface):
        pass
    
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
    global rows, width
    win.fill((0,0,0))#for filling the screen
    drawGrid(width,rows,surface)
    pygame.display.update()
def randomSnack(rows,items):
    pass
def message_box(subject,content):
    pass
def main():
    global width, rows
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
        redrawWindow(win)
        
    
    
    pass




main()    