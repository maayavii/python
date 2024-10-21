import numpy as np
print("Amal manoj / sjc23mca011")
array_2d=np.array([[1+2j,3+4j,5+6j],[7+8j,9+10j,11+12j]],dtype=complex)
print("2d array:")
print(array_2d)

#number of rows and colums
rows,colums=array_2d.shape
print("number of rows=",rows)
print(("number of colums=",colums))
#dimensions
dimensions=array_2d.ndim
print("dimensions=",dimensions)
#reshape to 3*2
reshape=array_2d.reshape(3,2)
print("reshaped")
print(reshape)