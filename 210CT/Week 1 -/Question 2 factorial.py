def factorial(x): 
    factorial = 1
    trail = 0
    for i in range(2,x + 1): #Will calculate the factorial by looping x number of time, x is the user input
        factorial = factorial*i
        while i > 0: #this loop will check if the remainder = 0
            if i % 5 ==0:
                trail += 1
                i = i/5
            else:
                break
    return(" the trailing 0s for: ",factorial, " is " ,trail)
print(factorial(60))
#runtime O(n^2)
'''
factorial is equal to 1
the loop will start at 2 and run what ever x is +1
for every time it loops factorial will be 'factorial' times 'i'
while loop will check if 'i' is greater than 0
if it is it will check if i divided by 5 has a remainder
if it has no remainder trail will increase by 1
then i gets divided by 5 and loops again until 'i' is no longer greater than 0
returns the trailing value
'''


    
    
    



    
    
