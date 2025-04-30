f1=open("Lab-11/sample.txt","r")
f2=open("Lab-11/sample2.txt","w+")
text=f1.read()
text=text.upper()

f2.write(text)
f2.close()
f1.close()

