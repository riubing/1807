name=input("请输入备份的文件名")
p = open(name,"r")
content=p.read()
l=input("请输入备份后的名字")
p2=open(l,"w")
p2.write(content)
p.close()
p2.close()

