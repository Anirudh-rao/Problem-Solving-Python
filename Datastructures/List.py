List  = [1,2,3,4,5]
print("The List is :", List)

List2 = ["Geeks", "For", "Geeks"]
print("\nList containing multiple values: ")
print(List2)


# List operations
print("Length of the list:", len(List))
print("The First Element of the list:", List[:1])
print("The Negative index of the list:", List[:-1])



for i in range(1, 4):
    List.append(i)
print("\nList after Addition of elements from 1-3: ")
print(List)

# Adding Tuples to the List
List.append((5, 6))
print("\nList after Addition of a Tuple: ")
print(List)

# Addition of List to a List
List2 = ['For', 'Geeks']
List.append(List2)
print("\nList after Addition of a List: ")
print(List)
