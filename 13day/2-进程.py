from multiprocessing import Process
import time
def show(name):
    for i in range(10):
        time.sleep(3)
        print(name)



p = Process(target=show,args=("挑大粪",))
time.sleep(4)
p.start()#启动进程
#p.join()等待子进程结束，在往下运行
#p.join(10)最多等十秒
p.terminate()#不管子进程结束没结束，立马让子进程结束停止
print("泡妞")

























