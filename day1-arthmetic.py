'python programming language,interpreted lang,it contain data types'# (data types)
#int
#float
#boolen
#string
#set
#tuple
#dictonary
# list 
#hello world'
'''print("hello world")
print("swec")'''
#in print stmt there is specific conditions.they are [PRINTING FORMATS]  are
#print -'using print stmt'
#for name storing we use the Syntax--(var1="python")
'''sowmya=input()
print("good mrg",sowmya)
print("hello",sowmya)
#fstring(format string is format of the string) for ex--age=50,name=sowmya
print(f"hello{name} you are {age} years old" )'''
#to check the marks(for more num of marks we use for loop conditions to get code easy)
name=input()
avg=0
sum=0
for i in range (0,5):
    marks=int(input())
    sum+=marks
avg=sum/5
print(f"your name is {name} and your sum is {sum} and your avg is {avg}")
    #conditional stmts-- to check the conditions of the stmt
#if(//try)
#elif(//catch)---(if there is more then two conditions we use elif)
#else(//throw)---(if there is two condition we use else )
name=input()
age= int(input())
if (age>=18):
    print(f"your name is {name}you are eligible for voting")
else:
    print("not eligible")

    #control stmt-- to control the stmt of code
