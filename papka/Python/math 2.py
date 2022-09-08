import math
x=int(input())
y=int(input())
a=2*int(x)
c=2*int(y)
b=4*int(y)

z= math.sqrt(math.cos(a)+math.sin(b)+math.sqrt(math.e**x+math.e**-x))
t=(math.e**-x+math.e**x)**3*(math.sin(b)+math.cos(c)-2)**2
h=z/t
print(h)
