def removeVowel(s,done=""):
    vowels = ['a', 'e', 'i', 'o', 'u']
    if len(s)> 0:
        if s[0] in vowels:
            return removeVowel(s[1:],done) # skips the letter
        else:
            return removeVowel(s[1:],done+s[0]) # adds the letter to done
    else:
        return done
print(removeVowel("supercalifragilisticexpialidocious"))

'''
input a string
if the length of string is greater than 0 then check
if the first index of the list is in the list vowels
if not skip the letter
if it is add the letter to done which is an empty string
now check the second letter until the length of s is no longer greater than 0
which then will return done which is the string without any vowels
'''

