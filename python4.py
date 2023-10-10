from typing import List, Union

n=int(input("enter the number of values"))
a=[]
for i in range(0,n):
    c=int(input("enter the value"))
    if c > 100:
        a.append("over")

    else:
        a.append(c) #c <100 so adding the value
print(a)