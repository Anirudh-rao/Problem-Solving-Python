"""
Create a Function that
 returns the Sqaured pattern of '*' of side n as list of strings

Parameter
n(int): The size of the square

Returns :
List : A list of strings where each string represntts a row of the square

"""

def generate_square(n):
    squared = []

    for i in range(n):
        squared.append('*' * n)

    return squared


result_3 = generate_square(3)
print(result_3)
result_4 = generate_square(4)
print(result_4)
result_5 = generate_square(5)
print(result_5)
