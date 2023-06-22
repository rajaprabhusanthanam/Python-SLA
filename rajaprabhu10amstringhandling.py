#program to do indexing, slicing and ranging with your names

print()

name = "Rajaprabhu"

#Indexing
print("Indexing")
print(name[4])
print()

#Slicing
print("Slicing")
print(name[0:4])
print()

#Ranging
print("Ranging")
print(name[4:])
print()

print()
#program using your names, location, city, etc
#and do string concatenation, repetition and formatting

name = "Rajaprabhu"
location = "Ekkattuthangal"
city = "Chennai"

#Concatenation
print("string concatenation")
print(name + " " + location + " " + city)
print()

#Repetition
print("string repetition")
print(city*2)
print()

#Formatting
print("string formatting")
print("my name is {}, I am coming from {}, Which is in {}".format(name, location, city))
print()

print()
#program to count character frequency in a name/string

name = "rajaprabhusanthanam"

from collections import Counter
print("count character frequency")
print(Counter(name))
print()

print()
#program to remove vowels from your name/ string

name = "Rajaprabhu Santhanam"
vowels = "a,e,i,o,u,A,E,I,O,U"

print("removal of vowels from string")
result = ''.join([char for char in name if char not in vowels])
print(result)
print()

print()
#program to find a length of your name/ string

print("length of the string")
name = "rajaprabhusanthanam"
print(len(name))
