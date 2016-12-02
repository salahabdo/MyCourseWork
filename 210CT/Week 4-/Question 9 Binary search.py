def Bsearch (slist, low, high):                                                                       
    listFirst = 0 # first value                                                                         
    listLast = len(slist)-1 #-1 from the list since it starts counting from 0          
    while listFirst < listLast:                                                                              
        mid = (listFirst + listLast)//2 # calculates middle value                           
        if slist[mid] in range (low,high): # checks if the middle value is in range                                     
            return True                                                                                             
        else:                                                                                   
            if slist[mid] < low:
                listFirst = mid +1  
            else:
                listLast = mid -1           
    return False                                                                                
print(Bsearch([5,6,7,8,11,15,20,22,23,24,25,27,28,29],15,20))
print(Bsearch([5,6,7,8,11,15,20,22,23,24,25,27,28,29],30,40))
print(Bsearch([5,6,7,8,11,15,20,22,23,24,25,27,28,29],27,29))
print(Bsearch([5,6,7,8,11,15,20,22,23,24,25,27,28,29],5,29))

# Time complexity O(log n)

'''
user input a list of sorted numbers
first pointer will be at 0
last pointer will be at the length of the sting - 1 since it starts at 0
while 'first' is less than or equal to 'last' run the while loop
middle pointer is 'listFirst' + 'listLast' divided by 2
if the middle value is in range of the low and high value return true since theres a value
else if middle value is greater than the low value then 'listLast' equal middle value -1
else 'listfirst' equal middle value +1
'''
                                                                                                
'''
Pseudocode:
FUNCTION BSEARCH (SLIST, LOW, HIGH):                                                                       
    first <- 0                                                                       
    last <- length slist - 1
    while first <= last                                                                             
        mid <- (first + last) DIV 2 
        if slist[mid] in range to low and high then
            return TRUE                                                                                             
        else                                                                                 
            if slist[mid] not in range to low and high then                                        
                first <- mid + 1
            else
                last <- mid - 1
    return FALSE                                                                     
'''
