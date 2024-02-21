"""
Loop Within a Loop
O(n^2): Here the code run for twice the time 
and hence is less time-efficient

"""


def print_items(n):
    for i in range(n):
        for j in range(n):
            print(i,j)
      
        
# DO NOT CHANGE THIS LINE:
print_items(10)