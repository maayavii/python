''' list of wovels in a word'''

from typing import List
v=['a','e','i','o','u']
word=input("enter the word")
print("wovels are")
s=[i for i in word if i in v]
print(s)