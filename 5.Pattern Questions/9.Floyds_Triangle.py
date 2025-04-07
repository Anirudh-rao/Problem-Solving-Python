"""
Generate a Floyds traingle for any n:
Ex: n =3
['1','2 3','4 5 6']
"""

def floyds_traingle(n):
    traingle =[]
    current_num = 1
    for i in range(1,n+1):
        row = ' '.join(str(current_num + j) for j in range(i))
        traingle.append(row)
        current_num += i
    return traingle
result_3 = floyds_traingle(3)
print(result_3)
result_4 = floyds_traingle(4)
print(result_4)
result_5 = floyds_traingle(5)
print(result_5)