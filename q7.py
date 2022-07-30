import math
print("\n\nQuestion 7: Write a program that reads the lengths of the sides of a triangle and displays the area. Assume that input is valid, i.e. the sides are able to form a triangle. Import the Math library to use the square root function." )
def q7():
    a=int(input("input first side:"))
    b=int(input("input second side:"))
    c=int(input("input third side:"))
    semiPerim=0.5*(a+b+c)
    triangleArea=math.sqrt(semiPerim*(semiPerim-a)*(semiPerim-b)*(semiPerim-c))

    print("The area of the triangle is:",triangleArea)
q7()