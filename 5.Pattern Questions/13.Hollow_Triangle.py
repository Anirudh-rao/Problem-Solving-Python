"""
Generating Hollow Triangle

"""
def HollowTirnagle(n):
    triangle =[]
    for i in range(1,n+1):
        if i == 1:
            triangle.append('*')
        elif i == n:
            triangle.append('*'*n)
        else:
            triangle.append('*' + ' ' * (i-2) + '*')
            
 
    return triangle
result_3 = HollowTirnagle(3)
print(result_3)
result_4 = HollowTirnagle(4)
print(result_4)
result_5 = HollowTirnagle(5)
print(result_5)