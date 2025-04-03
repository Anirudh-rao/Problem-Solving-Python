"""

Given Integers n 
Generate  a Right angled pattern from 1 to n 
"""

def right_angled_numbers(n):
    squared = []

    for i in range(1,n,1):
        row = str(i)*i
        squared.append(row)

    return squared


result_3 = right_angled_numbers(3)
print(result_3)
result_4 = right_angled_numbers(4)
print(result_4)
result_5 = right_angled_numbers(5)
print(result_5)
