
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

'''
Problem 5:
ALMOST THERE: Given an integer n, return True if n is within 10 of either 100 or 200
almost_there(90) --> True
almost_there(104) --> True
almost_there(150) --> False
almost_there(209) --> True
NOTE: abs(num) returns the absolute value of a number
'''

def almost_there(n:int) -> bool:
    return abs(n-100) <= 10 or abs(n-200) <= 10

print(f"Output for almost_there function: {almost_there(300)}")
print(f"Output for almost_there function: {almost_there(30)}")
print(f"Output for almost_there function: {almost_there(104)}")
print(f"Output for almost_there function: {almost_there(150)}")


'''
Problem 6:
Given a list of ints, return True if the array contains a 3 next to a 3 somewhere.
has_33([1, 3, 3]) → True
has_33([1, 3, 1, 3]) → False
has_33([3, 1, 3]) → False
'''

def has_33(ls:list) -> bool:
    index = ls.index(3)
    if ls[index+1] == 3:
        return True
    return False

print(f"Output for has_33([1, 3, 3]): {has_33([1, 3, 3])}")
print(f"Output for has_33([1, 3, 1, 3]): {has_33([1, 3, 1, 3])}")
print(f"Output for has_33([3, 1, 3]): {has_33([3, 1, 3])}")

'''
Problem 7:
PAPER DOLL: Given a string, return a string 
where for every character in the original there are three 
characters paper_doll('Hello') --> 'HHHeeellllllooo' 
paper_doll('Mississippi') --> 
'MMMiiissssssiiippppppiii'
'''

def paper_doll(st: str) -> str:
    ls = [i*3 for i in list(st)]
    return "".join(ls)

print(f"Output for paper_doll('Hello') -> {paper_doll('Hello')}")
print(f"Output for paper_doll('Mississippi') -> {paper_doll('Mississippi')}")


'''
Problem 8:
BLACKJACK: Given three integers between 1 and 11, if their sum is less than or equal to 21, return 
their sum. If their sum exceeds 21 and there's an eleven, reduce the total sum by 10. Finally, if the 
sum (even after adjustment) exceeds 21, return 'BUST' blackjack(5,6,7) --> 18 blackjack(9,9,9) --> 
'BUST' blackjack(9,9,11) --> 19
'''

def blackjack(x,y,z):
    sum = (x+y+z)
    if sum <= 21: return sum
    elif sum > 21 and (x==11 or y==11 or z==11): return sum-10
    else: return 'BUST'

print(f"output for blackjack(5,6,7) -> {blackjack(5,6,7)}")
print(f"output for blackjack(9,9,9) -> {blackjack(9,9,9)}")
print(f"output for blackjack(9,9,11) -> {blackjack(9,9,11)}")


'''
Problem 9:
SUMMER OF '69: Return the sum of the numbers in the array, except ignore sections of numbers 
starting with a 6 and extending to the next 9 (every 6 will be followed by at least one 9). Return 0 for 
no numbers.
summer_69([1, 3, 5]) --> 9
summer_69([4, 5, 6, 7, 8, 9]) --> 9
summer_69([2, 1, 6, 9, 11]) --> 14
'''

def summer_69(ls:list) -> int:
    total = 0
    i = 0
    while i < len(ls):
        if ls[i] == 6:
            while i < len(ls) and ls[i] != 9:
                i += 1
            if i < len(ls):
                i += 1
        else:
            total += ls[i]
            i += 1
    return total

print(f"Output for summer_69([1, 3, 5]): {summer_69([1, 3, 5])}")
print(f"Output for summer_69([4, 5, 6, 7, 8, 9]): {summer_69([4, 5, 6, 7, 8, 9])}")
print(f"Output for summer_69([2, 1, 6, 9, 11]): {summer_69([2, 1, 6, 9, 11])}")
print(f"Output for summer_69([1, 2, 3]): {summer_69([1, 2, 3])}")
print(f"Output for summer_69([]): {summer_69([])}")


'''
Problem 10:
SPY GAME: Write a function that takes in a list of integers 
and returns True if it contains 007 in order
spy_game([1,2,4,0,0,7,5]) --> True
spy_game([1,0,2,4,0,5,7]) --> True
spy_game([1,7,2,0,4,5,0]) --> False
'''

def spy_game(ls:list) -> bool:
    st = '007'
    res = []
    for num in ls:
        if num == 0 or num == 7:
            res.append(str(num))
    
    resp = "".join(res)
    return resp == st

print(f"Output for spy_game([1,2,4,0,0,7,5]) -> {spy_game([1,2,4,0,0,7,5])}")
print(f"Output for spy_game([1,0,2,4,0,5,7]) -> {spy_game([1,0,2,4,0,5,7])}")
print(f"Output for spy_game([1,7,2,0,4,5,0]) -> {spy_game([1,7,2,0,4,5,0])}")    


'''
Problem 12:
PRINT BIG: Write a function that takes in a single letter, 
 returns a 5x5 representation of that 
letter print_big('a')
out: * 
 * *
 *****
 * *
 * *
HINT: Consider making a dictionary of possible patterns, 
and mapping the alphabet to specific 5-line 
combinations of patterns.
For purposes of this exercise, it's ok if your dictionary stops at "E".
'''

# Dictionary mapping letters to 5-line ASCII art patterns
letter_patterns = {
    'A': [
        '  *  ',
        ' * * ',
        '*****',
        '*   *',
        '*   *'
    ],
    'B': [
        '**** ',
        '*   *',
        '***  ',
        '*   *',
        '**** '
    ],
    'C': [
        ' ****',
        '*    ',
        '*    ',
        '*    ',
        ' ****'
    ],
    'D': [
        '**** ',
        '*   *',
        '*   *',
        '*   *',
        '**** '
    ],
    'E': [
        '*****',
        '*    ',
        '***  ',
        '*    ',
        '*****'
    ]
}

def print_big(letter: str) -> None:
    letter = letter.upper()
    if letter not in letter_patterns:
        print(f"Letter '{letter}' not available in the dictionary")
        return
    
    for line in letter_patterns[letter]:
        print(line)

print("Print Big 'A':")
print_big('A')
print("\nPrint Big 'B':")
print_big('B')
print("\nPrint Big 'E':")
print_big('E')
print("\nPrint Big 'a' (lowercase):")
print_big('a')


'''
Problem 13: Write a Python function that accepts a string and calculates the number of upper 
case letters and lower case letters.
Sample String : 'Hello Mr. Rogers, how are you this fine Tuesday?'
Expected Output :
No. of Upper case characters : 4
No. of Lower case Characters : 33

'''

def character_count(st: str):
    lCount, uCount = 0,0
    for l in st:
        if l.islower(): lCount+=1
        elif l.isupper(): uCount+=1
    
    print(f"No. of Upper case characters : {uCount}\n No. of Lower case characters : {lCount}")

s = 'Hello Mr. Rogers, how are you this fine Tuesday?'
character_count(s)


'''
Problem 14: Write a Python function that takes a list and returns a new list with unique 
elements of the first list.
Sample List : [1,1,1,1,2,2,3,3,3,3,4,5]
Unique List : [1, 2, 3, 4, 5]
'''

def unique_list(ls:list) -> list:
    return list(dict.fromkeys(ls))
    

print(f"Output for unique_list([1,1,1,1,2,2,3,3,3,3,4,5]) -> {unique_list([1,1,1,1,2,2,3,3,3,3,4,5])}")


'''
Problem 15: Write a Python function to check whether a string is pangram or not.
Note : Pangrams are words or sentences containing every letter of
the alphabet at least once.
For example : "The quick brown fox jumps over the lazy do
'''

def isPangram(st:str) -> bool:
    letters = set(char for char in st.lower() if char.isalpha())
    return len(letters) == 26


# Test cases for isPangram
print(f"isPangram('The quick brown fox jumps over the lazy dog'): {isPangram('The quick brown fox jumps over the lazy dog')}")
print(f"isPangram('Hello World'): {isPangram('Hello World')}")
print(f"isPangram('Pack my box with five dozen liquor jugs'): {isPangram('Pack my box with five dozen liquor jugs')}")
print(f"isPangram('abcdefghijklmnopqrstuvwxyz'): {isPangram('abcdefghijklmnopqrstuvwxyz')}")
