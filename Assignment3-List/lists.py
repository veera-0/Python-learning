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