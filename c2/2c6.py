import numpy as np
print("Amal Manoj / sjc23mca011")
# Create a 2D array with 4 rows and 4 columns
two_dimensional_array = np.array([[1, 2, 3, 4],
[5, 6, 7, 8],
[9, 10, 11, 12],
[13, 14, 15, 16]])
# Display all elements excluding the first row
excluding_first_row = two_dimensional_array[1:]
# Display all elements excluding the last column
excluding_last_column = two_dimensional_array[:, :-1]
# Display the elements of the 1st and 2nd column in the 2nd and 3rd row
column_1_2_in_row_2_3 = two_dimensional_array[1:3, 0:2]
# Display the elements of the 2nd and 3rd column
column_2_3 = two_dimensional_array[:, 1:3]
# Display the 2nd and 3rd element of the 1st row
elements_2_3_in_first_row = two_dimensional_array[0, 1:3]
# Display the elements from indices 4 to 10 in descending order
descending_order = two_dimensional_array.ravel()[::-1][4:11]
print("Original 2D array:\n", two_dimensional_array)
print("Elements excluding the first row:\n", excluding_first_row)
print("Elements excluding the last column:\n", excluding_last_column)
print("Elements of the 1st and 2nd column in the 2nd and 3rd row:\n",
column_1_2_in_row_2_3)
print("Elements of the 2nd and 3rd column:\n", column_2_3)
print("2nd and 3rd element of the 1st row:\n",
elements_2_3_in_first_row)
print("Elements from indices 4 to 10 in descending order:\n",descending_order)