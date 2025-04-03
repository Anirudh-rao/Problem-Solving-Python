"""

Given Integers n 
Generate  a pyramid pattern
with 1 star followed by 3 stars and so on increasing by 2 per row until 2n-1
"""

def pyramid(n):
    squared = []

    for i in range(1,n+1):
        stars = '*' * (2*i+1)
        spaces =  '*' * (n-i)
        squared.append(spaces +  stars + spaces)

    return squared


result_3 = pyramid(3)
print(result_3)
result_4 = pyramid(4)
print(result_4)
result_5 = pyramid(5)
print(result_5)
