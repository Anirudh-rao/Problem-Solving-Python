"""

Given Integers n 
Generate  a inverted pyramid pattern
"""

def inverted_pyramid(n):
    squared = []

    for i in range(1,n+1):
        stars  =  '*' * (2*(n-i+1)-1)
        spaces = ' '*(i-1)
        squared.append(spaces+stars+spaces)
    return squared


result_3 = inverted_pyramid(3)
print(result_3)
result_4 = inverted_pyramid(4)
print(result_4)
result_5 = inverted_pyramid(5)
print(result_5)
