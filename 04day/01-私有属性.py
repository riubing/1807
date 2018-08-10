class Dog():
    def __init__(self,name,age):
        self.name = name
        self.__age = 0
    def nl(self):
        self.name
    def xm(self):
        self.__age
    def getAge(self):
        return self.__age



erha = Dog()
erha.getAge()
print(erha.getAge())



