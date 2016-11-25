def reverser(data,i):#reverse recursive function
    x = ""
    if len(data)>i+1:
        x = reverser(data,i+1)
    return x+" "+data[i]
def sentence(string):# sentence input and reverse output
    word = string.split(' ')# breaks up the string
    return(reverser(word,0)) #returns teh splited string and 0 to 'reverser'
print(sentence("my name is salah"))
'''
User input a sentence, any sentence
the sentence gets split into separate words into a list
function returns the list of strings
if the length of the sting is greater than i +1 then
'''
