'''
1. # Given the string 'hello' give an index command that returns 'e'. Enter your code in the cell below:
s = 'hello'
# Print out 'e' using indexing
'''

s = 'hello'
print(f"printing 'e' using indexing: {s[1]}")

print("\n")
'''
2. # Reverse the string 'hello' using slicing:
s ='hello'
# Reverse the string using slicing
'''

print(f"String reversing using slicing: {s[::-1]}")

print("\n")
'''
3. # Given the string hello, give two methods of producing the letter 'o' using indexing.
s ='hello'
# Print out the 'o'
# Method 1: Positive indexing
# Method 2: Negative indexing
'''

print(f"printing 'o' using Method 1 (positive indexing): {s[4]}")
print(f"printing 'o' using Method 2 (negative indexing): {s[-1]}")

print("\n")
'''
4. # Use for, .split(), and if to create a Statement that will print out words that start with 's':
st = 'Print only the words that start with s in this sentence'
'''

st ='Print only the words that start with s in this sentence'
print("Words starts with 's' in the given sentence are: ")
for word in st.split(' '):
    if word.startswith('s'):
        print(word)

print("\n")
'''
5. # Write python program that displays stars(*) in right angled triangular form using nested loops
'''

print("Right-angled triangle pattern using nested loops:")
rows = 5
for i in range(1, rows + 1):
    for j in range(i):
        print("*", end="")
    print()


print("\n")
'''
6. # Write a while loop that starts at the last character in the string 
and works its way backwards to the first character in the string, printing each letter on a separate line
'''

print("Printing string backwards using while loop:")
length = len(s)
while length != 0:
    print(s[length-1])
    length -= 1


print("\n")
'''
7. Convert 1024 to binary and hexadecimal representation
'''

num = 1024
print(f"Number: {num}")
print(f"Binary representation: {bin(num)}")
print(f"Hexadecimal representation: {hex(num)}")

print("\n")
'''
8. Round 5.23222 to two decimal places
'''
num = 5.23222
print("printing the round of 5.23222 upto 2 places. ")
print(f"Round of {num} upto 2 decimal places is: {round(num, 2)}")

print("\n")
'''
9.Check if every letter in the string s is lower case
s = 'hello how are you Mary, are you feeling okay?'
'''

s = 'hello how are you Mary, are you feeling okay?'
print(f"String: {s}")
print(f"Is the string all lowercase? {s.islower()}")

for letter in s.split():
    if letter.islower():
        print(f"Character {letter} is in lowercase")
    else:
        print(f"Character {letter} is not in lowercase")

print("\n")
'''
10.How many times does the letter 'w' show up in the string below?
s = 'twywywtwywbwhsjhwuwshshwuwwwjdjdid'
'''
count = 0
s = 'twywywtwywbwhsjhwuwshshwuwwwjdjdid'
count = s.count('w')

print("\n")
print(f"Letter 'w' occurs: {count} times in {s}")

print("\n")
'''
11:Reverse the list below:
list1 = [1,2,3,4]
'''
list1 = [1,2,3,4]
print(f"reversing the list: {list1}")

print(f"reversed list is: {list1[::-1]}")