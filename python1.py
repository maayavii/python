start=int(input("starting year:"))
end=int(input("ending year:"))
print("leap years are")
for year in range (start+1,end):
    if (year%400==0) and (year%100!=0) or(year%4==0):
        print(year)