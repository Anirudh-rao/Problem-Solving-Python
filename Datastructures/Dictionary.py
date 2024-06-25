dict = {'Name':'Ani',1:[1,2,3,4]}

print("Creating Dictionary\n")
print(dict)

print("Accessing elements of dictionary\n")
print(dict['Name'])


print("Accessing a element using get:")
print(dict.get(1))

# creation using Dictionary comprehension
myDict = {x: x**2 for x in [1,2,3,4,5]}
print(myDict)