from graphics.dgraphics import cuboid,sphere
from graphics import circle,rectangle

r=int(input('enter the radious='))
circle.areac(r)
circle.peric(r)

l=int(input(('enter length=')))
b=int(input("enter bredth="))

rectangle.arear(l,b)
rectangle.perir(l,b)

s=int(input('enter the radious of sphere='))
sphere.areas(s)

x=int(input(("length of cuboid=")))
y=int(input(("bredth of cuboid=")))
z=int(input(("height of cuboid=")))

cuboid.area(x,y,z)
cuboid.peri(x,y,z)



