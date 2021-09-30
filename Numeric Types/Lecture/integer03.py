import math
a=int(input("a ning qiymatini kiriting:  "))
s=a//100  #x
d=((a-s*100)//10)*10 #0yz
e=s*100+d  #xy0
f=a-e
g=f*100+d+s
print(g)