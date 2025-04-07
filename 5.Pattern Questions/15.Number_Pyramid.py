
"""
Generating Number Pyramid

"""
def NumberPyramid(n):
    pyramid =[]
    for i in range(1,n+1):
        spaces = ' ' * (n-i)
        numbers = ' '.join(str(x) for x in range(1,i+1))
        pyramid.append(spaces+numbers+spaces) 
 
    return pyramid
result_3 = NumberPyramid(3)
print(result_3)
result_4 = NumberPyramid(4)
print(result_4)
result_5 = NumberPyramid(5)
print(result_5)