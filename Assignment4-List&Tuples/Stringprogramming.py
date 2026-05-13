
'''
1. Python Program to Take in Two Strings and Display the Larger String without Using Built-in Functions
'''
st1 = input("Enter string1: ")
st2 = input("Enter string2: ")

if len(st1) > len(st2): 
    print(f"{st1} is the largest string.")
else: print(f"{st2} is the largest string.")

print("\n")
'''
2. Python Program to Count Number of Lowercase Characters in a String
'''

st3 = "WElcOmE EveryOne"
lCount = 0
for i in range(len(st3)):
    if st3[i].islower():
        lCount += 1

print(f"Lower character count in the string: {st3} is : {lCount}")

print("\n")
'''
3. Python Program to Check if a String is a Palindrome or Not
'''

st4 = input("Enter a string to check palindrome or not: ")

if st4 == st4[::-1]:
    print(f"{st4} is a palindrome string.")
else: print(f"{st4} is not a palindrome string")

print("\n")
'''
4. Python Program to Calculate the Number of Upper Case Letters and Lower Case Letters in a String
'''

lCount = 0
uCount = 0
for i in range(len(st3)):
    if st3[i].islower():
        lCount += 1
    elif st3[i].isupper():
        uCount +=1 

print(f"The string: {st3} has lower count: {lCount} and upper count: {uCount}")

print("\n")
'''
5. Python Program to Accept a Hyphen Separated Sequence of Words as Input and 
Print the Words in a Hyphen-Separated Sequence after Sorting
'''
st5 = input("Enter words seperated by hyphen: ")

lst = st5.split('-')

lst.sort()

sortedString  = "-".join(lst)

print(f"sorted string is: {sortedString}")

print("\n")
'''
6. Python Program to Calculate the Number of Digits and Letters in a String
'''

s = input("Enter a string with letters and numbers: ")

aCount = 0
dCount = 0
for i in s:
    if i.isalpha():
        aCount += 1
    elif i.isdigit():
        dCount += 1

print(f"String: {s} contains number count: {dCount} and letter count: {aCount}")

'''
7. The program to create a stack and allow the user to perform push and pop operations on it
'''
stack = []

print("1. push to stack \n2.POP item\n3.Exit")

while True:
    choice = int(input("Enter your choice: "))
    match choice:
        case 1:
            element = int(input("Enter the element to push to stack: "))
            stack.append(element)
            print(f"element: {element} has been pushed to stack.")
        case 2:
            e = stack.pop()
            print(f"elelemnt: {e} has been removed")
        case 3:
            print("Exiting")
            break
        case _:
            print("please choose a correct option.")

print(f"The data inside the stack: {stack}")






