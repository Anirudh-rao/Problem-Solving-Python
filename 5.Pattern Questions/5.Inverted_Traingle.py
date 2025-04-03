"""

Given Integers n 
Generate  a Inverted Right angled pattern from n to 1 
"""

def inverted_angled_pattern(n):
    squared = []

    for i in range(n,0,-1):
        squared.append('*'* i)

    return squared


result_3 = inverted_angled_pattern(3)
print(result_3)
result_4 = inverted_angled_pattern(4)
print(result_4)
result_5 = inverted_angled_pattern(5)
print(result_5)
