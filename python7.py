s=str(input("enter a string="))
first=s[0]  #index value of first letter'''
s=s.replace(first,'$')  #the occurance of fist letter replaced by $  replace function is used'''

s=first+s[1:] #conditions applied everything except 1st letter'''
print(s)

