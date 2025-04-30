f1=open("Lab-11/sample.txt","r")
f2=open("Lab-11/sample2.txt","r")
newfile=open("Lab-11/sample3.txt","w+")

a=len(f1.readlines())
b=len(f2.readlines())
max=0
if(a>b):
    max=a
else:
    max=b

for i in range(max):
    newfile.write(f1.readline())
    newfile.write(f2.readline())