import math
a=int(input("a ning qiymatini kiriting:  "))
s=a//100
d=((a-s*100)//10)*100
r=(s*100+d/10)
e=a-r
b=d+s*10+e
print(b)
 