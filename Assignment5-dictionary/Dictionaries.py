
'''
Problem 1:
 Create two sets of students, one for those who took an exam and one for those that submitted a 
project. 
 simple strings is used to represent the students
 # Set up sets
exam = {'Andrew', 'Kirsty', 'Beth', 'Emily', 'Sue'}
project = {'Kirsty', 'Emily', 'Ian', 'Stuart'}

Using these sets write the code using different set methods to show the below following question 
functionalities:
• Which students took both the exam and submitted a project?
• Which students only took the exam?
• Which students only submitted the project?
• List all students who took either (or both) of the exam and the project.
• List all students who took either (but not both) of the exam and the project.
'''

exam = {'Andrew', 'Kirsty', 'Beth', 'Emily', 'Sue'}
project = {'Kirsty', 'Emily', 'Ian', 'Stuart'}

#Which students took both the exam and submitted a project?
print(f"Students with exam and project: {exam.intersection(project)}")

#Which students only took the exam?
print(f"Students who took only exams: {exam.difference(project)}")

#Which students only submitted the project?
print(f"Students {project.difference(exam)} only submitted the project.")

#List all students who took either (or both) of the exam and the project.
print(f"Students {exam.union(project)} took either (or both) of the exam and the project.")

#List all students who took either (but not both) of the exam and the project.
print(f"Students {exam.symmetric_difference(project)} took either (but not both) of the exam and the project.")


'''
Problem 2:
 
 A Prime Number is a positive whole number, greater than 1, that has no other
divisors except the number 1 and the number itself.
That is, it can only be divided by itself and the number 1, for example the
numbers 2, 3, 5 and 7 are prime numbers as they cannot be divided by any other
whole number. However, the numbers 4 and 6 are not because they can both be
divided by the number 2 in addition the number 6 can also be divided by the
number 3.
You should write a program to calculate prime number starting from 1 up to the
value input by the user.
If the user inputs a number below 2, print an error message.
For any number greater than 2 loop for each integer from 2 to that number and
determine if it can be divided by another number (you will probably need two for
loops for this; one nested inside the other).
For each number that cannot be divided by any other number (that is its a prime number and print it 
out)

'''

num = int(input("Enter a number: "))

prime_list = []
if num < 2:
    print("Please choose a value greater than 2.")
else:
    for i in range(2, num + 1):
        is_prime = True
        for j in range(2, i):
            if i % j == 0:
                is_prime = False
                break
        if is_prime:
            prime_list.append(i)
print(f"list of primes: {prime_list}")


'''
Problem 3: Find the elements in set1 that are not in set2:
 Find all elements that are in either set:
set1 = {2,3,1,5,6,8}
set2 = {3,1,7,5,6,8}
'''
set1 = {2,3,1,5,6,8}
set2 = {3,1,7,5,6,8}
#Find the elements in set1 that are not in set2
print(f"Elements in set1 that are not in set2: {set1.difference(set2)}")

#Find all elements that are in either set
print(f"All elements that are in either set: {set1.union(set2)}")

'''
Problem 4:
 Create this dictionary: {0: 0, 1: 1, 2: 8, 3: 27, 4: 64} 
 using a dictionary comprehension
'''

d = {i:i**3 for i in range(5)}

print(f"Dictionay: {d}")

'''
Problem 5:
 Write a program that prints the numbers from 1 to 100. But for
   multiples of three print “Fizz” instead 
of the number 
 and for the multiples of five print “Buzz”.
 For numbers which are multiples of both three and five print “FizzBuzz”.
'''

for i in range(1, 101):
    if i%3 == 0:
        print('Fizz')
    elif i%5 == 0:
        print("Buzz")
    elif i%3 == 0 and i%5==0:
        print("Fizzbuzz")
    else:
        print(i)

'''
Problem 6:
 Checks if the string entered by the user is a palindrome. 
 That is that it reads the same forwards as backwards like “racecar
'''

s = input("Enter a string: ")

if s==s[::-1]:
    print(f"{s} is a palindrome.")
else: print(f"{s} is not a palindrome")

