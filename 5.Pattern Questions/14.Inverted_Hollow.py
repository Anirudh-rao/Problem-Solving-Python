
"""
Generating Inverted Hollow Triangle

"""
def InvertedHollowTirnagle(n):
    triangle =[]
    for i in range(n,0,-1):
        if i == 1:
            triangle.append('*'*n)
        elif i == n:
            triangle.append('*')
        else:
            spaces = ' ' * (i-2)
            triangle.append('*' + spaces + '*')
            
 
    return triangle
result_3 = InvertedHollowTirnagle(3)
print(result_3)
result_4 = InvertedHollowTirnagle(4)
print(result_4)
result_5 = InvertedHollowTirnagle(5)
print(result_5)