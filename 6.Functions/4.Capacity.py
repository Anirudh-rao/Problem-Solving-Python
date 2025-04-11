def Capacity(n, C):

    """
    Given total number of people n and capacity of a lift C
    Find the total number of lifts required to transport the people.

    """
    full_round = n // C
    if n % C != 0:
        return full_round + 1
    else:
        return full_round 


f1 = Capacity(34,5)
print(f1)
f2 = Capacity(104,67)
print(f2)
f3 = Capacity(144,78)
print(f3)