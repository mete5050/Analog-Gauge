import mysql.connector
import pyautogui
import time
import os

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




while don==1:

    #os.system("clear")
    imlec = mydb.cursor()
    time1=mytime.perf_counter()
    try:
        #recevie
        imlec.execute("SELECT * FROM coordnt2")
        myresult = imlec.fetchall()

        for row in myresult:
            x   = row[0]
            y = row[1]
            b1= row[2]
            b2= row[3]
            b3= row[4]
            b4= row[5]
            b5= row[6]
    except:
        print(" _____")
    mydb.commit()
    time2=mytime.perf_counter()
    delay=time2-time1
    print("x=",x,"  ","y=",y  ,"buttons: ",b1,",",b2,",",b3,",",b4,",",b5)
    print(float(delay))
    #pyautogui.moveTo(x,y)
    imlec.close()







