class che():
    def __init__(self,color,xinghao):
        self.color=color
        self.xinghao=xinghao
    def fangfa(self):
        print("千里马")
    def yinyu(self):
        print("为你推荐:我对着自己开了一枪")
    def zwjs(self):
        print("我是兰博基尼,颜色是%s 型号是%s"%(self.fangfa,self.xinghao))



lbjn=che("红色","SDFI")
lbjn.fangfa()
lbjn.yinyu()
lbjn.zwjs()
