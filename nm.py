import math as m
while(True):
    y1x0=float(input("Enter"))
    y2x0=float(input())
    y11x1=y1x0+(5*y2x0)
    y22x1=y2x0+5*(2.5-(2*y2x0)+(y1x0/2))
    y1x1=y1x0+((5/2)*(y2x0+y22x1))
    y2x1=y2x0+((5/2))*(2.5-(2*y2x0)+(y1x0/2)+2.5-(2*y22x1)+(y11x1/2))
    print(y11x1)
    print(y22x1)
    print(y1x1)
    print(y2x1)