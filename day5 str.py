 #strings is a sequence of characters
#strings are immutable we cannot modify after creating
#advantage of string is
#methods of strings
#len()
#islower()
#isupper()
#isalpha()
#isnumeric()
#isalnum()
#isdigit()
#it returns boolean value
#title-->combination of uppercase and lowercase
#swap()--->converting upper to lower and lower to upper
#trim()
#strip--->leaving and taking spaces
#capitalize-->
#converting to uppercase
#converting to lowercase
#defalut input: variable name is input
str=input()
'''print(len(str))        
print(str.islower())
print(str.isupper())
print(str.isalnum())
print(str.isnumeric())
print(str.isalpha())
print(str.title())
print(str.capitalize())
print(str.strip())
print(str.split('y'))
print(str.swapcase())
print(str.replace('y','z'))
print(str.isascii())'''
print(str.isdigit())
#if u want to get ascii number of a character print ord
print(ord('A'))
print(ord('A')+3)
print(ord("<"))
print(chr(60))
#check how many vowels in a string
'''str=input()
cnt=0
v=['a','e','i','o','u']
for i in str:
    if i in v:
        cnt+=1
print(cnt) '''
#to convert lower to upper
'''check=['a','e','i','o','u']
cnt=0
i="hello wOrld"
inp=i.lower()
for i in inp:
    if (i in check):
        cnt+=1
print(cnt) '''  

#consonants count
'''str=input()
cnt=0
v=['a','e','i','o','u']
for i in str:
    if i not in v:
        cnt+=1
print(cnt)''' 
#we use len for space
#we can use list for input in str
vowel="aeiou"
cons="bcdfghjklmnpqrstvwxyz"
cnt=0
cons=0
i="hello wOrld"
inp=i.lower()
for i in inp:
    if (i in vowel):
        cnt+=1
for i in inp:
    if i not in vowel:
        cnt+=1        
print(cnt,cons)
#print all the vowels followed by consonents
vowels="aeiou"
cons="bcdfghjklmnpqrstuvwxyz"
ans=""
i="amazing"
inp=i.lower()
for i in inp:
    if( i in vowels):
        ans+=i
for i in inp:
    if(i in cons):
        ans+=i
print(ans)
#print the unique characters in a string
str=input()
unique=""
for i in str:
    if str.count(i)==1:
        unique+=i
print(unique)
#input is given as hello123
#output is 6
#sum is sum of digits
'''str="hello123"
d="0123456789"
sum=0
for i in str:
    if i in d:
        sum+=int(i)
print(sum)''' 
