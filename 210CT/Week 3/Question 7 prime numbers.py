# x = the testing value to see if its prime
# i = the number you going to divide x by to see if its prime
def prime (x, i = 2):
    if x <= 1:
        return("prime numbers start at 2, this is not a prime number")
    while x > i: # this will only run only if x is greater than i
        if (x % i) == 0: # if x divided by i has no remainder its not prime
            return(x," is not a prime number")
            break
        else:
            return (prime(x, i+1)) # if it does have a remainder it will loop back and divide it by i +1 which is every number less than x
    else:
        return(x," is a prime number")
print(prime(67))
'''
user inputs a number to test and also another number which is less than x but greater than 2 to divide by x to see if its prime
if x is less than 1 or equal to 1 then its not prime
this while loop will only run if x is greater than i
within the while loop the if statement will check if x divided by i has a remainder if it doesnt then its not prime
else we call the function again and change the value of i =+1
this will keep looping until x is no longer greater than i
'''
        
    
           
