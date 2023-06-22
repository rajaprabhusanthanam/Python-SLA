print ("Removal of Vowels in a string")

print()
print()

print("1. Simple iteration on string using for loop")

"""

The following method uses

    1. A for loop to iterate on the input string
    2. Characters are not vowels are added to the result string

"""

string = "Rajaprabhu Santhanam"

vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
result = ""

for i in range(len(string)):
    if string[i] not in vowels:
        result = result + string[i]

print("After removing Vowels: ", result)

print()
print()

print("2. Iterate on individual char of string")

"""

The following method uses

    1. Iterator to iterate on each character of the input string
    2. Unlike the previous method where we use string[i] we directly iterate on char of whole string

"""

string = "Rajaprabhu Santhanam"

vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
result = ""

for char in string:
    if char not in vowels:
        result = result + char

print("After removing Vowels: ", result)

print()
print()

print("3. Uses replace method")

"""

The following method uses

    1. Creating a copy for Input string called as result
    2. Iterate on the whole string char one by one
    3. Use an internal replace method that replaces all occurrences of a character in the whole result string

"""

input_string = "Rajaprabhu Santhanam"
result = input_string

vowels = ('a', 'e', 'i', 'o', 'u')

for x in input_string.lower():
    if x in vowels:
        result = result.replace(x, "")

print('After removing vowels : ', result)

print()
print()

print("4. Longer but more clear implementation")

"""

This method is a little longer but simple implementation of the same.

"""

#take user input
String = "Rajaprabhu Santhanam"

#initialize new empty string
result = str()
String = String.lower()

for i in String:
    #check condition if alphabet belong to group of vowels
    if i == 'a' or i == 'e' or i == 'i' or i == 'o' or i == 'u':
        pass
    else:
        result = result + i

#check for if the result is not null
if len(result) == 0:
    print('No vowel found in ' + String)
else:
    print('After removing vowels : ' + result)


print()
print()

print("5. One line iterator and join method")

"""

This method uses one line for iterator and join method to join individual list characters. 

"""

def remove_vowel(string):
    vowels = ['a','e','i','o','u']
    
    # result will become : ['P', 'r', 'p', 'n', 's', 't'] after below step
    result = [letter for letter in string if letter.lower() not in vowels]
    
    # result will become Prpnst, i.e. we joined strings in this
    result = ''.join(result)
    print(result)
 
# Driver program
string = "Rajaprabhu Santhanam"
print(string)
remove_vowel(string)

print()
print()

print("6. Using Regex")

"""

The below solution is using regex :-

"""

# import the module for regular expression (re)
import re
def rem_vowel(string):
    return (re.sub("[aeiouAEIOU]","",string))           

# Driver program
string = "Rajaprabhu Santhanam"
print(rem_vowel(string))

print()
print()

print("7. Using Slicing")

"""
The following method uses slicing. Advantage we can remove the vowels without needing another variable.

"""

str = "Rajaprabhu Santhanam"

vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
i = 0
for c in str:
    if c in vowels:
        str = str[:i] + str[i+1:]
        i = i-1
    i = i+1

print("After removing Vowels : ", str)
