# 1.	Create a list of 5 odd integers using random nos. Similarly create a list of 4 even integers using random nos. Replace the third element of odd integers with  a list of 4 even integers. Flattern, sort and print the list. Provide appropriate message at each stage
import random

lst1=[]
lst2=[]
for i in range(5):
   lst1.append(random.randrange(1,20,2))
print(lst1)


for i in range(4):
   lst2.append(random.randrange(2,10,2))
print(lst2)


lst1[2]=lst2

print(lst1)

fl=[]

for i in lst1:
   if(isinstance(i,list)):
      fl.extend(i)
   else:
      fl.append(i)
fl.sort()
f2=fl
print(f2)