lower = int(input("Enter lower limit: "))
upper = int(input("Enter upper limit: "))

square_numbers = [i for i in range(lower, upper+1) if int(i**0.5)**2 == i]

print("Perfect square numbers in the given range:", square_numbers)

