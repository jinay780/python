import threading
x=0
COUNT=100000

def adding_2():
  global x
  for i in range(COUNT):
    x +=2

def adding_3():
  global x
  for i in range(COUNT):
    x +=3

def subtracting_4():
  global x
  for i in range(COUNT):
    x -=4 

def subtracting_1():
  global x
  for i in range(COUNT):
    x -=1

t=threading.Thread(target=adding_2,)
t2=threading.Thread(target=subtracting_4,)
t3=threading.Thread(target=adding_3,)
t4=threading.Thread(target=subtracting_1,)

t.start()
t2.start()
t3.start()
t4.start()

t.join()
t2.join()
t3.join()
t4.join()
