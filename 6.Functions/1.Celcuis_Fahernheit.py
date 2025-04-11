def celcuis_to_franheit(C):

    """
    Convert temperature from celcius to fahernheit
    """
    Fahernheit = (9/5 * C) + 32 
    return Fahernheit


f1 = celcuis_to_franheit(34.5)
print(f1)
f2 = celcuis_to_franheit(104.5)
print(f2)
f3 = celcuis_to_franheit(144.5)
print(f3)