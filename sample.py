if 7 < 9:
    print("iam big")
    # this is a sample program the words inside #wont work
""" 
things inside this also cant read 
when written in more than one line
"""
# let x,y,z can be 3 varialbes of three difrrent types int,float,str
x = int(3)
y = float(3)
print(x)  # this will be 3
print(y)  # this is 3.0

print(type(x))  # used to identify the type of variables used
print(type(y))

fruits = ["apple", 'orange', "banana"]
a, b, c = fruits  # a=apple,b=orange,c=banana
print(a)  # print only the first item inside the variable
print(fruits)  # print all elements inside the variable
print((a, b, c))  # also use to print all elemts togther

r = 10
s = 90
print(r + s)  # simple add 2 numbers
n = 'm'
j = 'r'
print(n + j)  # when 2 letters or words used in variables put them inside 'this'

e = 'cool'
def myfunc():
    print("python is" , e)
myfunc()  #end the function the last one should put ar corner

p="lie" #p is global varable
def myfunc():
    p='true'   #p assgined as a local variable inside the function
    print(p)
myfunc()
print(p) #outside the functon p have the same global variable value
