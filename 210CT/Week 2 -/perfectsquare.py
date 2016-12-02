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
print(square(998001))

'''
user inputs a number
the number get stored into a separate variable
while sqr * sqr is greater than x then -1 from sqr
if sqr * sqr is not equal to x then it’s not a perfect square and returns the value to the other function
this function will -1 until sqr is equal to x 
if its equal to x then
check if it’s less than or equal to 2 if it is then its 4
else returns a perfect square less than its parameter.

'''

'''
FUNCTION CHECK(X,SQR)
    if sqr*sqr not = x then
        return check(x-1,sqr)
    else
        if sqr <= 2 then
            return(4)
        else:
            return(sqr*sqr)
            
FUNCTION SQUARE(X)
    sqr <- x
    while sqr*sqr > x
            sqr <- sqr - 1
    if sqr*sqr is not = x then
        return to functionn check(x,sqr)
    else
        if sqr <= 2 then
            return(4)
'''



    
    
