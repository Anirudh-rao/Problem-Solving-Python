"""

Given Integers M and N where 1<=n and m<=100
Grenerate a Rectangular Pattern M*N 

"""

def reactangle_square(n,m):
    squared = []

    for i in range(n):
        squared.append('*' * m)

    return squared


result_3 = reactangle_square(3,4)
print(result_3)
result_4 = reactangle_square(4,5)
print(result_4)
result_5 = reactangle_square(5,6)
print(result_5)
