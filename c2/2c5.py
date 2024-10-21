import numpy as np
print("Amal Manoj / sjc23mca011")
#Create a 1D array containing the first 15 even numbers as elements

even=np.arange(2,31,2)
print(even)

slice=even[2:9:2]
last_3=even[-3:]
alternate=even[::2]
last_3_alternate=alternate[-3:]
print("Elements from index 2 to 8 with step 2:", slice)
print("Last 3 elements of the array using negative index:",last_3)
print("Alternate elements of the array:", alternate)
print("Last 3 alternate elements:", last_3_alternate)
