x1,y1=int(input("enter value")),int(input("enter value"))
x2,y2=int(input("enter value")),int(input("enter value"))
x3,y3=int(input("enter value")),int(input("enter value"))
m1=(y2-y1)/(x2-x1)
m2=(y3-y2)/(x3-x2)
m3=(y1-y3)/(x1-x3)
if(m1==m2==m3):
    print((x1,y1),(x2,y2),(x3,y3),"points lie on straight line")
else:
     print((x1,y1),(x2,y2),(x3,y3),"points do not lie on straight line")
