def sequence(n):
    tempList = []
    subSq = []
    for i in range(len(n)-1): # 'i' represents the index of the list
        if n[i] < n[i + 1]:
            tempList.append(n[i])
        else:
            tempList.append(n[i])
            subSq +=[tempList] # appends the temp list to subSq list to create a sublist
            tempList = []
    tempList.append(n[i+1])
    subSq +=[tempList] 
    return(max(subSq, key=len)) #returns the largest sub sequence within the sublist
print(sequence([1,5,1,6,7,8,1,2,3,4,5,6,7,8]))

'''
Input the 'n' sequence list
for loop run and look at the index instead of the number
if the first index is smaller than the next index
append that number to the the templist
carry on until the index is no longer less than the next index
append that list into the 'sub sequence' list to create a sub list
clear the the temp list and the loop will carry on
loop exits
add the last the value to the list
and append the last sequence to the sub list
now return the max sub sequence in the sublist
'''

    
    
