#Indexing dictionaries, nested dictionaries, methods....


#Define a dictionary:
#It needs Key-Value pairs.
x = {"Name": "David",
     "age" : "17",
     "height": "180cm",
     "Profession": "Writer"}
print(x)

x["age"] = "18" #If you want to update a key, you just rename it.
print(x)


#Nested Dictionaries:
#we are defining a dictionary inside a dictionary
y = {"Kampe" : {"Math" : "95", "English": {"92"}},
     "Junior": {"Math": "96", "English" : {"93"}}
     }

print(y)
#How to access a value in a nested dictionary
y["Kampe"]["English"] #You don't use the pythoning idex but rather theire key-value
print(y["Kampe"]["English"])

y["Kampe"]["English"] = "100"
print(y)


#To add a key:
y["Kaze"] = {"Math": "97", "English": "98"}

print(y)

#To add a list dictionary, string, tupples...

z = {"Kampe" : "18",
     (1,2): "Cat",
     "x" : [1,2,3],
      "y": (1,2,3)}

print(z)


#Methods of Dictionary
x = {"Name": "David",
     "age" : "17",
     "height": "180cm",
     "Profession": "Writer"}

print(x.keys()) #Gives us a tupple of the keys
print(x.values()) #Gives us a tupple of the values
print(x.items())  #Gives us a tupple of the values
print(x.get("Name"))
print(x['Name'])

#To delete something from our dictionary:


print(x.pop("Profession")) #It  shows which value it is removing
print(x) #We can see that it was removed oth key and value