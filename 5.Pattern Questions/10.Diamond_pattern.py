"""
Generate a Dimamond Pattern  n:

"""

def diamond(n):
    diamond =[]

    for i in range(1,n+1):
        stars = '*' * (2*i-1)
        spaces = ' '*(n-i)
        diamond.append(spaces + stars + spaces)

    for i in range(n-1,0,-1):
        stars = '*' * (2*i-1)
        spaces = ' '*(n-i)
        diamond.append(spaces + stars + spaces)
    return diamond
result_3 = diamond(3)
print(result_3)
result_4 = diamond(4)
print(result_4)
result_5 = diamond(5)
print(result_5)