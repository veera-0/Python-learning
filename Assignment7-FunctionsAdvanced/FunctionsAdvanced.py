
'''
Problem 5: Problem 1 Use map() to create a function which finds the length of each word in the 
phrase (broken by spaces) and returns the values in a list.
The function will have an input of a string, and output a list of integers.
word phrase is :'How long are the words in this phrase'
'''

def find_word_length(st: str) -> list:
    return list(map(lambda s : len(s), st.split(' ')))

s = 'How long are the words in this phrase'
print(f"The length of each word in {s} is : {find_word_length(s)}")


'''
Problem 6:
 Use reduce() to take a list of digits and return the number that they correspond to. For example, [1, 2, 3] 
corresponds to one-hundred-twenty-three.
Do not convert the integers to strings!
another example [3,4,5,1] == 3451
'''

from functools import reduce

def convert_list_to_string(ls: list) -> str:
    return reduce(lambda x,y:str(x)+str(y), ls)


lst = [3,4,5,1]
print(f"Output for converting the list {lst} to string: {convert_list_to_string(lst)}")


'''
Problem 7:
Use filter to return the words from a list of words which start with a target letter.
l = ['hello','are','cat','dog','ham','hi','go','to','heart']
if my target is 'h' then it should return me all the words starting from h
'''

def filter_list_by_target(ls: list , target: str ) -> list:
    return list(filter(lambda s: s.startswith(target), ls))

l = ['hello','are','cat','dog','ham','hi','go','to','heart']
print(f"output for the function is: {filter_list_by_target(l,'h')}")


'''
Problem 8:
 Use zip() and a list comprehension to return a list of the same length where each value is the two strings 
from L1 and L2 concatenated together
with connector between them.
for e.g concatenate(['A','B'],['a','b'],'-')
should return as ['A-a', 'B-b']
'''

def concatinate(l1, l2, st):
    return [x + st + y for x, y in zip(l1, l2)]

result = concatinate(['A','B'],['a','b'],'-')
print(f"Output for concatenating ['A','B'] and ['a','b'] with '-': {result}")


'''
Problem 9:
 Use enumerate() and other skills to return a dictionary
   which has the values of the list as keys and the 
index as the value.
You may assume that a value will only appear once in the given list.
'''

def problem9(ls):
    return [{i:item} for i,item in enumerate(ls)]

ls = ['a', 'b','c','d','e']
print(f"outut : {problem9(ls)}")


'''
Problem 10:
 Use enumerate() and other skills from above to
   return the count of the number of items in the list whose 
value equals its index
for eg : count_match_index([0,2,2,1,5,5,6,10])
 should give the output as 4
'''

def count_match_index(ls: list):
    return len(list(filter(lambda x: x[0] == x[1], enumerate(ls))))


ls = [0,2,2,1,5,5,6,10]
print(f"output for problme10: {count_match_index(ls)}")


