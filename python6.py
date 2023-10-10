'''comparing the length of two list'''
list1=(1,2,5,6,9,3)
print("the first list is",list1)
list2=(1,2,4,8,9,6)
print("the first second is",list1)

print(("length of list one=",len(list1)))
print(("length of list two=",len(list2)))

if len(list1)==len(list2):
    print("length of lists are same")
else:
    print("length of lists are not same")

    ''' weather list sum same value'''

print('sum of list 1=',sum(list1))
print('sum of list 2=',sum(list2))

if sum(list1)==sum(list2):
    print("sum is equel")
else:
    print("sums are diffrent")

    ''' any value occur in both '''\

check=any(item in list1 for item in list2)
print("any value occure in both is=",check)