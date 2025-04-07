"""
Generate Sunglass given N:

"""

def SunGlass(n):
    sunglass =[]
    for i in range(n):
        stars = '*' * (2*(n-i)-1)
        space = ' ' * i
        sunglass.append(space + stars + space)
    for i in range(n-1):
        stars = '*' * (2*(i+1)+1)
        spaces = ' '*(n-i-2)
        sunglass.append(spaces+stars+spaces)    
    return sunglass
result_3 = SunGlass(3)
print(result_3)
result_4 = SunGlass(4)
print(result_4)
result_5 = SunGlass(5)
print(result_5)