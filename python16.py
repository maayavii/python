fruits={"apple,orange,grape,papaya,banana,chery":10}
a=list(fruits.items())
a.sort()
print("ascending",a)
a=list(fruits.items())
a.sort(reverse=True)
print("descending",a)
