import csv
with open("demo.csv",'w+',newline='')as f1:
    wri=csv.writer(f1)

    str1=[['Roll No','Name','Mark1','Mark2','Mark3','Total'],
      ['24BCP198','Krishnu',12,23,45,80],
      ['24BCP199','Jack',12,23,45,80],
      ['24BCP197','Roman',12,23,45,80]]

    wri.writerows(str1) 
f1.close()
  