import csv
dis={}
with open("demo.csv",'r') as f1:
    re=csv.reader(f1)


    for i in re:
      dis[i[0]]=tuple(i[1:])

print(dis)
f1.close()