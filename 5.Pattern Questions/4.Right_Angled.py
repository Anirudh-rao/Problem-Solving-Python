"""

Given Integers n 
Generate  a Right angled pattern from 1 to n 
"""

def right_angled_pattern(n):
    squared = []

    for i in range(n,n+1):
        squared.append('*'* i)

    return squared


result_3 = right_angled_pattern(3)
print(result_3)
result_4 = right_angled_pattern(4)
print(result_4)
result_5 = right_angled_pattern(5)
print(result_5)
