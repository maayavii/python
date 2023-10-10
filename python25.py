my_string = str(input('enter a string:'))
new_list = [i for i in my_string.casefold()]

'''This line creates a new list (new_list) 
containing each character of the string my_string.
 The casefold() method is used to convert all characters to lowercase, 
 ensuring that we count characters in a case-insensitive manner.'''

my_dict = {}.fromkeys(new_list, 0)

'''This line creates a new list (new_list) containing each character of the string my_string. 
The casefold() method is used to convert all characters to lowercase, 
ensuring that we count characters in a case-insensitive manner.'''

for i in my_string.casefold():
    if i in my_dict:
        my_dict[i] = my_dict[i] + 1

        '''This is a loop that goes through each character of the original string (my_string). 
        For each character, it checks if it is a key in the dictionary (if i in my_dict:). 
        If the character is a key, it increments the corresponding value by 1 (my_dict[i] = my_dict[i] + 1)'''


print("Original string:", my_string)
print("Character counts:", my_dict)
