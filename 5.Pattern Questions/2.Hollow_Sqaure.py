"""
Given an Integer.Provide a Hollow square pattern NxN
made up of charecter '*'
It needs to have '*' on the border and spaces ' '

"""

def hollow_square(n):
    squared = []
    if n == 1:
        return['*']
    squared.append('*' * n)

    for i in range(n-2):
        squared.append('*' + ' ' * (n-2) + '*')
    squared.append('*'*n)
    return squared


result_3 = hollow_square(3)
print(result_3)
result_4 = hollow_square(4)
print(result_4)
result_5 = hollow_square(5)
print(result_5)
