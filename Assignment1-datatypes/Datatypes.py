
'''
# Answer these 3 questions without typing code. Then type code to check your answer.
What is the value of the expression 4 * (6 + 5)
What is the value of the expression 4 * 6 + 5 
What is the value of the expression 4 + 6 * 5
'''

print(f"4 * (6 + 5) = {4 * (6 + 5)}")

print(f"4 * 6 + 5 = {4 * 6 + 5}")

print(f"4 + 6 * 5 = {4 + 6 * 5}")


# 2. What would you use to find a number’s square root, as well as its square?

# TO find the square root of a number, we can use the exponentiation operator with 0.5 as the exponent. 

number = int(input("Enter a number to find its square root: "))
# square root of the number can be calculated as follows:

square_root = number ** 0.5
print(f"The square root of {number} is {square_root}")

'''
    3.
    Try creating your own variables and storing values into those variables. 
    Print out the values that are stored and also print the datatype of the variables created.
'''
variable1 = "Hello"
variable2 = 4.3
variable3 = 90
variable4 = (4,8.9,"training")
variable5 = [1,2,3,4,5]
variable6 = {"name": "Training", "year": 2026}

print(f"Datatype of variable1 : {variable1,type(variable1)}")
print(f"Datatype of variable2: {variable2, type(variable2)}")
print(f"Datatype of variable3: {variable3, type(variable3)}")
print(f"Datatype of variable4: {variable4, type(variable4)}")
print(f"Datatype of variable5: {variable5, type(variable5)}")
print(f"Datatype of variable6: {variable6, type(variable6)}")

'''
4. 
Include an assignment that will add two numbers together (for example 4+5) and then assign the result 
to a variable.
Similarly perform all the mathematical operations like Subtraction, Multiplication, Division , floor 
division , Power , Square root and print out that variables value once it has been assigned a value
'''

a = int(input("Enter value of a: "))
b = int(input("Enter value of b: "))

print("Adding a+b : {}".format(a+b))
print("Subtracting the values a-b : {}".format(a-b))
print("Multiplying the values a*b : {}".format(a*b))
print("Division of the values a/b: {}".format(a/b))
print("Modulus Division of the values a%b: {}".format(a%b))
print("Floor division of the values a//b : {}".format(a//b))
print("Power of the values, a**b : {}".format(a**b))
print("Square root of a, a**0.5 : {}".format(a**0.5))
print("Square root of b, b**0.5 : {}".format(b**0.5))

'''
5. Try Printing “*” - in the first line 20 times , second line 30 times and third row 40 times
'''
print("\n")
print("Printing stars 20 times")
print("*" * 20)

print("Printing stars 30 times")
print("*" * 30)

print("Printing stars 40 times")
print("*" * 40)


'''
Try out Examples with various Expression consisting of multiple operators.
'''

import math

examples = [
    ("4 + 6 * 5", 4 + 6 * 5),
    ("(4 + 6) * 5", (4 + 6) * 5),
    ("2 ** 3 * 4 + 5", 2 ** 3 * 4 + 5),
    ("5 + 4/2 * 3 - 1", 5 + 4/2 * 3 - 1),
    ("9 % 4 + 2 * 3", 9 % 4 + 2 * 3),
    ("-(3 + 2) * 4", -(3 + 2) * 4),
    ("2 + 3 * (4 - 1) / 2", 2 + 3 * (4 - 1) / 2),
    ("pow(2,3) + 1", pow(2, 3) + 1),
    ("math.pow(2,3) + 0.5", math.pow(2, 3) + 0.5),
]

print('\nExamples with multiple operators:')
for expr_str, value in examples:
    print(f"{expr_str} = {value}  (type: {type(value).__name__})")

