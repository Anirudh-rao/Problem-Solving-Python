
def print_items(a,b):
#For this case the Big(O) wont be O(n)
# as 'A' and 'B' May be different   
    # for First Function it will be O(a)
    for i in range(a):
        print(i)
    #for the Second Function it will be O(b)
    for i in range(b):
        print(i)
# and Total will be O(a+b)

#In this case it will be O(a*b)
def print_items2(a,b):
    for i in range(n):
        for i in range(n):
            print(i)

