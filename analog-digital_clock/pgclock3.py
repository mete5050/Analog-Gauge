#! /usr/bin/env python

#pgclock.py
#analog and digital clock example
import pyautogui
import os, sys, pygame
from pygame.locals import *
import datetime
import time as mytime
import mysql.connector
import pyautogui
mydb = mysql.connector.connect(
    host="bhri1hy8aev1vaqzdsyz-mysql.services.clever-cloud.com",
      user="uwfmufwws9iah9ga",
  password="7IHSBOXmZvYxzGAR6oyS",
  database="bhri1hy8aev1vaqzdsyz"
)


print(mydb) 
don=1

imlec = mydb.cursor()
print("ok")
time1=mytime.perf_counter()
X, Y = pyautogui.position() 
print(X,Y)

b1=0



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
size = width, height = 960, 220
screen = pygame.display.set_mode(size)
pygame.init()
aasa=-90
#load clock face as background        
bg = item("clock-face.jpg",0,0,0)
bg2 = item("clock-face2.jpg",0,240,0)
bg3 = item("clock-face3.jpg",0,480,0)
bg4 = item("clock-face4.jpg",0,720,0)

bg.setaxis((730/2,100))
bg2.setaxis((1200/2,100))
bg3.setaxis((1680/2,100))
bg4.setaxis((bg.width/2,100))

#load and place clock hands
#the hand images rotate around their own central axis because
#almost one half of the image is set to transparent
longhand = item("ibre.png",-1,0,0)
shorthand = item("ibre2.png",-1,0,0)
secondhand = item("ibre3.png",-1,10,3)
secondhand2 = item("ibre4.png",-1,10,3)
secondhand3 = item("ibre5.png",-1,10,3)

#setup font
black = 0,0,0
white = 255,255,255
font = pygame.font.Font(None, 30)


print(mydb) 
don=1
X="0"
Y="0"
b1 = "0"
b2 = "0"
b3 = "0"
b4 = "0"
b5 = "0"
imlec = mydb.cursor()

imlec.execute("DROP TABLE IF EXISTS coordnt2")
imlec.execute("CREATE TABLE coordnt2 (x VARCHAR(255) , y VARCHAR(255), b1 VARCHAR(255), b2 VARCHAR(255), b3 VARCHAR(255), b4 VARCHAR(255), b5 VARCHAR(255) )")
print("ok")



#transmit
sql = "INSERT INTO coordnt2(x,y,b1,b2,b3,b4,b5) VALUES(%s,%s,%s,%s,%s,%s,%s)"
val = (X,Y,b1,b2,b3,b4,b5)
imlec.execute(sql,val)
mydb.commit()
T=0


while 1:

    #os.system("clear")
    imlec = mydb.cursor()
    time1=mytime.perf_counter()
    try:
        #recevie
        imlec.execute("SELECT * FROM coordnt2")
        myresult = imlec.fetchall()

        for row in myresult:
            Left_Throttle   = row[0]
            Right_Throttle = row[1]
            b1= row[2]
            b2= row[3]
            b3= row[4]
            b4= row[5]
            b5= row[6]    
            Left_Throttle=int(Left_Throttle)
            Right_Throttle=int(Right_Throttle)
    except:
        print(" _____")
        #Left_Throttle=0
        #Right_Throttle=0
        #b1 =0
        #b2 =0
        #b3 =0
        #b4 =0
        #b5 =0
    mydb.commit()
    time2=mytime.perf_counter()
    delay=time2-time1
  
    
    
    print("Left_Throttle",Left_Throttle,"  ","Right_Throttle",Right_Throttle  ,"buttons: ",b1,",",b2,",",b3,",",b4,",",b5)
    print(float(delay))
    #pyautogui.moveTo(x,y)
    imlec.close()


    for event in pygame.event.get():
        if event.type == QUIT:
           sys.exit(0)
    aasa=(Left_Throttle/4.95) -140
    aasa2=(Right_Throttle/2.84) -140
    #redraw the background to clear the screen
    bg.draw()
    bg2.draw()
    bg3.draw()
    bg4.draw()
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
    secondhand2.drawrot(bg3.axis,minute)
    b1=int(b1)

    secondhand3.drawrot(bg4.axis,-b1+140)
    

    #Set the font - Create an offset white shadow behind black 
    fontimg = font.render(str(b1),2,white)
    screen.blit(fontimg, (100,155))
    fontimg2 = font.render(str(aasa),2,white)
    screen.blit(fontimg2, (340,155))
    #mytime.sleep(0.3)
    pygame.display.update() 

