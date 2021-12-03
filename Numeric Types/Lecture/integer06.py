import math
r=int(input("r ning qiymatini kiriting:  "))
n=int(input("n ning qiymatini kiriting:  "))
a=int(input("a ning qiymatini kiriting:  "))
b=int(input("b ning qiymatini kiriting:  "))
c=(pow((1+r/100),n))/(math.sqrt(a**2+b**2))  #amallar to'plami
print(c)
