import random
def randomNum(x):
    listNum = list(str(x))# covenerts the input into a list
    d = len(str(x))# stores the length of the list
    for i in range(0,d):
        newNum = random.choice(listNum) # chooses a random number from the list and stores it
        newNum2 = random.choice(listNum) 
        a, b = listNum.index(newNum), listNum.index(newNum2) #selects the random numbers in the list and represnts them as 'a' and 'b'
        listNum[b], listNum[a] = listNum[a], listNum[b] # will swap position 'a' with position 'b'
    return listNum
print(randomNum(123456789))

'''''''''
User inputs a list of number
for loop will run the length amount of 'x'
first pick 1 random number from the list then pick second random number from list
asigns first number and second number postion to a variable, a and b
swaps postion a with postion b
this will loop as long  as the length of 'x'
'''''''''''

