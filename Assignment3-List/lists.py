'''
Problem 1:
Reverse the list below:
list1 = [1,2,3,4]
'''

list1 = [1,2,3,4]
ls = sorted(list1, reverse=True)
print(f"Reversing the list: {ls}")

'''
Problem2 :
Sort the list below:
list2 = [3,4,2,5,1]

'''

list2 = [3,4,2,5,1]
list2.sort()
print(f"Sorted list is: {list2}")


'''
Problem 3:
[Arise But It Juliet Who already and breaks east envious fair grief is kill light moon pale sick soft sun the 
through what window with Who yonder what]
# Write a program to read all the lines or entire data in the object ,
# and split into a list of words .
# For each word, check to see if the word is already in a list. 
# If the word is not in the list, add it to the list. , so at the end we need to get the list which has all 
unique words only
# When the program completes, sort and print the resulting words in alphabetical order.

'''

data = "Arise But It Juliet Who already and breaks east envious fair grief is kill light moon pale sick soft sun the through what window with Who yonder what"

#spliting the data into a list of words
dataList = data.split(' ')

# Create a list to store unique words
uniqueWords = []

# Check each word and add only unique words to the list
for word in dataList:
    if word not in uniqueWords:
        uniqueWords.append(word)

# Sort the unique words in alphabetical order
uniqueWords.sort()

# Print the result
print(f"Unique words in alphabetical order: {uniqueWords}")



'''
Problem 4:
 "stephen.marquard@uct.ac.za Sat Jan 5 09:14:16 2008"
 For the specified string , retrive time and display separately
'''
print("\n")

information = "stephen.marquard@uct.ac.za Sat Jan 5 09:14:16 2008"

#extracting the time and displaying
ls = information.split(" ")

print(f"Time according to given information is: {ls[4]}")

'''
Problem 5:
 Write a program to read different values from the user and convert all the values received in to list 
and then compute average
'''
print("\n")

# Get input from user
values_input = input("Enter numbers separated by spaces: ")

# Convert to list of numbers
values_list = list(map(float, values_input.split()))

# Compute average
average = sum(values_list) / len(values_list)

# Display result
print(f"List of values: {values_list}")
print(f"Average: {average}")

print("\n")

'''
Problem 6:
 Write program to receive the input of temperature in Celsius and convert it into Fahrenheit
'''
temperature = int(input("Enter temperature in celsius: "))

Fh = (temperature * 9/5) + 32

print(f"Temperature in Fahrenheit: {Fh}") 

print("\n")

'''
Problem 7:
 Write a program to prompt from the user for a score between 0.0 and 1.0. 
If the score is out of range print an error. If the score is between 0.0 and 1.0, 
print a grade using the following table:
Score Grade
>= 0.9 A
>= 0.8 B
>= 0.7 C
>= 0.6 D
< 0.6 F

'''

grade = float(input("Enter a score between 0.0 and 1.0: "))

if grade >= 0.9 and grade<=1.0: print("A")
elif grade >= 0.8 and grade<0.9: print("B")
elif grade >= 0.7 and grade<0.8: print("C")
elif grade >= 0.6 and grade<0.7: print("D")
elif grade <0.6: print("FAIL")
else: print("error: Please enter a valid score. ")

'''
Problem 8:
 find the largest value in a list [3, 41, 12, 9, 74, 15], construct the program using either for loop or 
while loop instead of using min and max functions
'''

lst = [3,41,12,9,74,15]
max = 0
for i in lst:
    if i>max: max=i
    else: i+=1

print(f"Max values in the list: {lst} is {max}")

'''
Problem 9:
 program that Takes in a credit card number from a common 
 credit card vendor (Visa, MasterCard, American Express, Discover) 
 and validates it to make sure that it is a valid number
'''

# Get credit card number from user
card_number = input("Enter credit card number: ")

# Check if it contains only digits
if not card_number.isdigit():
    print("Invalid: Please enter only digits")
else:
    # Check the length and card type
    if len(card_number) < 13 or len(card_number) > 19:
        print("Invalid: Card number should be between 13 and 19 digits")
    else:
        # Check card type based on first digit
        first_digit = card_number[0]
        first_two_digits = card_number[:2]
        
        if first_digit == '4':
            card_type = "Visa"
        elif first_two_digits in ['51', '52', '53', '54', '55']:
            card_type = "MasterCard"
        elif first_two_digits in ['34', '37']:
            card_type = "American Express"
        elif card_number[:4] == '6011' or card_number[0] == '6':
            card_type = "Discover"
        else:
            card_type = "Unknown"
        
        if card_type == "Unknown":
            print(f"Invalid: Unknown card type")
        else:
            print(f"Valid {card_type} card!")
            print(f"Card number: {card_number}")


'''
Problem 10:
 Enter a string and the program counts the number of vowels in the text. 
 For added complexity have it report a sum of each vowel found.

'''

st = input("Entra a string: ")
vowel_sum = 0
for s in st:
    if s in ('a','e','i','o','u'):
        vowel_sum +=1 

print(f"Sum of vowels found in the string: {st} is: {vowel_sum}")


'''
Problem 11:
Write a program to read values with integer datatypes from the user and display them as matrix ,
And create 2 different matrix .
Then perform Addition of Matrix as well as Multiplication of 2 matrix and print the resul
'''

# Create first matrix
print("Enter values for Matrix 1 (2x2):")
matrix1 = []
for i in range(2):
    row = []
    for j in range(2):
        value = int(input(f"Enter value for position [{i}][{j}]: "))
        row.append(value)
    matrix1.append(row)

# Create second matrix
print("\nEnter values for Matrix 2 (2x2):")
matrix2 = []
for i in range(2):
    row = []
    for j in range(2):
        value = int(input(f"Enter value for position [{i}][{j}]: "))
        row.append(value)
    matrix2.append(row)

# Display Matrix 1
print("\nMatrix 1:")
for row in matrix1:
    print(row)

# Display Matrix 2
print("\nMatrix 2:")
for row in matrix2:
    print(row)

# Addition of matrices
print("\nAddition of Matrix 1 and Matrix 2:")
addition = []
for i in range(2):
    row = []
    for j in range(2):
        sum_value = matrix1[i][j] + matrix2[i][j]
        row.append(sum_value)
    addition.append(row)

for row in addition:
    print(row)

# Multiplication of matrices
print("\nMultiplication of Matrix 1 and Matrix 2:")
multiplication = []
for i in range(2):
    row = []
    for j in range(2):
        product = 0
        for k in range(2):
            product = product + (matrix1[i][k] * matrix2[k][j])
        row.append(product)
    multiplication.append(row)

for row in multiplication:
    print(row)
