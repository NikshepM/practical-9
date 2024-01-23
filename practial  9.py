fh =open("prac 9.txt",'w')
def GenerateTable(Num):
 i=0
 k=1
 while k<=10:
    fh.write(str(Num)+"*"+str(k)+"="+str(Num*k)+"\n")
    k=k+1
Table=int(input("Enter a number: "))
GenerateTable(Table)
fh.close()