letters = ["a", "b", "c", "d", "e"]

matrix= [ [0,1], [2,3]]

#How to multiply one list multiple time

zero = [0] * 100

#To combine list you can just add them
Combined = zero + letters

# print(Combined)

numbers= list(range(20)) #This creates a list of the range 20, which isiterable but doesn't include 20.
print(numbers)

#Strings as well are iterable:
words = list("Hello World")
print(len(words)) #How man charaters in the list
print(len(zero))
print(words)

#To access specific items in the list
print(letters[0])
print(letters[1])
print(letters[0:3]) #Up until 2, not 3
print(letters[:3])
print(letters[3:])


#Unpacking lists:
#assign different variables in the list to specific positions in our list

numbers = [1,2,3]

first, second, third = numbers
# or
first = numbers[0]
second = numbers[1]
third = numbers[2]

print(first)


#or if you are only intered in the first
first, * other = numbers
print(first)
print(other)



##TUPLE: A list you can't change

#we can loop over the list:
letters = ["a", "b", "c", "d", "e"]
for letter in letters: #You don't need indentation here.
     print(letter)

#If you want the positions as well: You can do it and get a tuple of the position and value (Dictionary??)

letters = ["a", "b", "c", "d", "e"]
for letter in enumerate(letters): #You don't need indentation here.
     print(letter)

for index, letter in enumerate(letters): #Using similar unpacking methods
#Unpacking:
#index, letter = enumerate(letters)

    print(index,letter)


#Add to a list: use method Append

print(letters.count("a")) #Count, counts how many times you have a value in your list
letters.append("f") #he method redefines the letter list

print(letters)


#To remove items at the end of the list you use method (Pop)

letters.pop()
print(letters)

#You want to remove a specific location
letters.pop(0)
print(letters)

#Remove an object but you don't know it's index.
letters.remove("b")
print(letters)

del letters[0:2]

print(letters)

#To find a value in our list: use method (index)
letters= ["a", "b", "c", "d", "e"]

if "d" in letters:
    print(letters.index("d"))



#HOW TO LOOP OVER LISTS:

#You can use for loops

letters =








