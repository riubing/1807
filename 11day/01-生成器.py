def pl():
    x,c = 2,3
    print("------9---------")
    for i in range(100):
        print(i)
        yield c
        print("--------9----------")
        x,c = x,x+c



m = pl()
for i in m:
    print((i))
