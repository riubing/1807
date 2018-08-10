class che():
    def __init__(self,name):
        self.name = name
    def pao(self):
        print("跑跑跑")
    def gw(self):
        print("拐弯")
class jili(che):
    pass
class dazhong(che):
    pass
class haima(che):
    pass



C = jili("吉利")
print(C.name())
B = dazhong("大众")
print(B.name())
A = haima("海马")
print(A.name())



