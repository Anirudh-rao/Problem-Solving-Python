"""
Generate a Right Angled Traingle :

"""

def Right_Angled_Triangle(n):
    triangle =[]
    for i in range(1,n+1):
        spaces = ' ' * (n-i)
        stars = '*' * i
        triangle.append(spaces + stars)
    
    return triangle
result_3 = Right_Angled_Triangle(3)
print(result_3)
result_4 = Right_Angled_Triangle(4)
print(result_4)
result_5 = Right_Angled_Triangle(5)
print(result_5)