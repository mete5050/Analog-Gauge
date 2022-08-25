#! /usr/bin/env python

#pgclock.py
#analog and digital clock example
import pyautogui
import os, sys, pygame
from pygame.locals import *
import datetime
import time as mytime
class item:

    def __init__(self,imagename,colorkey,left,top):
        self.img = pygame.image.load(imagename).convert()
        if colorkey == -1:
            ckey = self.img.get_at((0,0))
            self.img.set_colorkey(ckey, RLEACCEL)
        self.rect = self.img.get_rect()
        self.left = left
        self.top = top
        self.width = self.rect.width
        self.height = self.rect.height
        self.center = self.rect.center

    def draw(self):
        screen.blit(self.img,(self.left, self.top))

    def setaxis(self,axis):
        self.axis = axis

    def drawrot(self,axis,angle):
        #Create new rotated image: preserve original
        self.newimg = pygame.transform.rotate(self.img,angle).convert()
        self.newrect = self.newimg.get_rect()
        #Now center the new rectangle to the rotation axis
        self.newrect.left = axis[0]-(self.newrect.w/2)
        self.newrect.top = axis[1]-(self.newrect.h/2)
        screen.blit(self.newimg,(self.newrect.left, self.newrect.top))

#setup screen size and background image
size = width, height = 480, 220
screen = pygame.display.set_mode(size)
pygame.init()
aasa=-90
#load clock face as background        
bg = item("clock-face.jpg",0,0,0)
bg2 = item("clock-face2.jpg",0,240,0)

bg.setaxis((730/2,100))
bg2.setaxis((bg.width/2,100))
#load and place clock hands
#the hand images rotate around their own central axis because
#almost one half of the image is set to transparent
longhand = item("clockhand-long.bmp",-1,0,0)
shorthand = item("clockhand-short.bmp",-1,0,0)
secondhand = item("secondhand.bmp",-1,10,3)

#setup font
black = 100,100,100
white = 255,255,255
font = pygame.font.Font(None, 30)

while 1:
    pX, pY = pyautogui.position() 
    for event in pygame.event.get():
        if event.type == QUIT:
           sys.exit(0)
    aasa=(pX/4.95) -140
    aasa2=(pY/2.84) -140
    #redraw the background to clear the screen
    bg.draw()
    bg2.draw()
    #get time
    dt=str(datetime.datetime.today())
    hr = float(dt[11:13])
    min = float(dt[14:16])
    sec = float(dt[17:19])
    time = dt[11:19]
    
    #get angles for clock hands .. +1 is for pixel correction
    second = -aasa2 +1
    minute = -aasa +1     



    #draw the clock hands

    longhand.drawrot(bg.axis,minute)
    secondhand.drawrot(bg2.axis,second)
    

    #Set the font - Create an offset white shadow behind black 
    fontimg = font.render(str(aasa2),2,white)
    screen.blit(fontimg, (100,155))
    fontimg2 = font.render(str(aasa),2,white)
    screen.blit(fontimg2, (340,155))
    #mytime.sleep(0.3)
    pygame.display.update() 

