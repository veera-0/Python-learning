
'''
Problem 1:
LESSER OF TWO EVENS: Write a function that returns the lesser of two given numbers if both 
numbers are even, but returns the greater if one or both numbers are odd lesser_of_two_evens(2,4) 
--> 2 lesser_of_two_evens(2,5) --> 5
'''

def lesser_of_two_evens(x,y):
    if x%2==0 and y%2==0:
        if x>y: return y
        else: return x
    else:
        if x>y: return x
        else: return y

print(f"Output of the function: {lesser_of_two_evens(2,4)}")
print(f"Output of the function: {lesser_of_two_evens(3,5)}")


'''
Problem 2:
ANIMAL CRACKERS: Write a function takes a two-word string and returns True if both words begin 
with same letter animal_crackers('Levelheaded Llama') --> True animal_crackers('Crazy Kangaroo') 
--> False
'''

def animal_cracker(st: str) -> bool:
    ls = st.split(' ')
    if ls[0][0].lower() == ls[1][0].lower():
        return True
    return False

print(f"Output for the function animal_crackers is: {animal_cracker("Literal Samson")}")
print(f"Output for the function animal_crackers is: {animal_cracker("sit Stand")}")

'''
MAKES TWENTY: Given two integers, return True if the sum of the integers is 20 or if one of the 
integers is 20. If not, return False
makes_twenty(20,10) --> True
makes_twenty(12,8) --> True
makes_twenty(2,3) --> False
'''

def makes_twenty(x,y) -> bool:
    if x==20 or y==20: return True
    elif (x+y) == 20: return True
    else: return False

print(f"Output for makes_twenty: {makes_twenty(30,1)}")
print(f"Output for makes_twenty: {makes_twenty(18,2)}")
print(f"Output for makes_twenty: {makes_twenty(5,15)}")

'''
Problem 4:
OLD MACDONALD: Write a function that capitalizes the first and fourth letters of a name
old_macdonald('macdonald') --> MacDonald
Note: 'macdonald'.capitalize() returns 'Macdonald'
'''

def old_macdonald(st: str) -> str:
    ls = list(st)
    ls[0] = ls[0].upper()
    ls[3] = ls[3].upper()
    ns = "".join(ls)
    return ns

print(f"Output for old_macdonald: {old_macdonald("samisingh")}") 
print(f"Output for old_macdonald: {old_macdonald("vikraRathod")}") 

