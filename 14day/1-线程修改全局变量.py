from threading import Thread
import time
num = 0
def work():
    global num
    for i in range(100000):
        time.sleep(0.5)
        num += 1
        print(num)



def work1():
    global num
    for i in range(1000000):
        time.sleep(1)
        num += 1
        m.release()
        print(num)
        print("thread-1")



l = Thread(target=work)
l1 = Thread(target=work1)




from threading import Thread
import time
num = 0
flag = 1
def work1():
    global
for i in range()
















































