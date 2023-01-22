
def area(radius: int):
    #return(3.14159 * (radius ^ 2))
    return(3.14159 * (radius * radius))



x = range(100000)
for i in x:
    print(f"radius is:  {i}")
    print (f"area is:  {area(i)}")
    print("")

