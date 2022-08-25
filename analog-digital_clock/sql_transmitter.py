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
b1 = "0"
b2 = "0"
b3 = "0"
b4 = "0"
b5 = "0"
imlec = mydb.cursor()

imlec.execute("DROP TABLE IF EXISTS coordnt2")
imlec.execute("CREATE TABLE coordnt2 (x VARCHAR(255) , y VARCHAR(255), b1 VARCHAR(255), b2 VARCHAR(255), b3 VARCHAR(255), b4 VARCHAR(255), b5 VARCHAR(255) )")
print("ok")
time1=time.perf_counter()
X, Y = pyautogui.position() 
print(X,Y)

#transmit
X=str(X)
Y=str(Y)
sql = "INSERT INTO coordnt2(x,y,b1,b2,b3,b4,b5) VALUES(%s,%s,%s,%s,%s,%s,%s)"
val = (X,Y,b1,b2,b3,b4,b5)
imlec.execute(sql,val)
mydb.commit()
T=0



while don==1:
    os.system("clear")
    T=T+1
    imlec = mydb.cursor()
    time1=time.perf_counter()
    X, Y = pyautogui.position() 
    b1 = T
    b2 = "0"
    b3 = "0"
    b4 = "0"
    b5 = "0"
    b1=str(b1)
    imlec.execute("DROP TABLE IF EXISTS coordnt2")
    imlec.execute("CREATE TABLE coordnt2 (x VARCHAR(255) , y VARCHAR(255), b1 VARCHAR(255), b2 VARCHAR(255), b3 VARCHAR(255), b4 VARCHAR(255), b5 VARCHAR(255) )")
    #transmit
    X=str(X)
    Y=str(Y)
    sql = "INSERT INTO coordnt2(x,y,b1,b2,b3,b4,b5) VALUES(%s,%s,%s,%s,%s,%s,%s)"
    val = (X,Y,b1,b2,b3,b4,b5)
    imlec.execute(sql,val)
    mydb.commit()



    time2=time.perf_counter()
    delay=time2-time1

    #imlec.close()
    print(X,Y)
    print(float(delay))
    imlec.close()



