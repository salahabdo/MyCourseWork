def check(x,sqr):
    if sqr*sqr != x:
        return(check(x-1,sqr))
    else:
        if sqr <= 2:
            return(4)
        else:
            return(sqr*sqr)
def square(x):
    sqr = x
    while sqr*sqr > x:
            sqr = sqr - 1
    if sqr*sqr != x: # this if statement was nested inside the while
        return(check(x,sqr))
    else:
        if sqr <= 2:
            return(4)
        else:
            return((sqr-1)*(sqr-1))
print(square(26))







    
    
