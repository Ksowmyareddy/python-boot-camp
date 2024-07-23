#replace the elements in an array with the average of maximum and minimum elements
testcase:0
13 2 67 20 68
68+2=70/2==35
35 35 35 35 35 
'''my_list=list(map(int,input().split()))
min_elememt=my_list[0]
max_element=my_list[0]
for i in range(0,len(my_list)):
     if(my_list[i]<min_element):
        min_element=my_list[i]
     if(my_list[i]>max_element):
        max_element=my_list[i]
avg=(max_element+min_element)//2
 for i in range(len(my_list)):
 my_list[i]=avg
print(my_list)'''
#find the duplicates in an array
#8 7 7 8 5 4 4 8 9
#8 7 4'''
'''l=list(map(int,input().split()))
for i in l:
    if(i in [l]):
        [].appends(i)
print([l])'''
'''sum of  digits
123%10=3
3
123/10=12
n=12
12%10=2
3+2=5
12/10=1
n=1
1%10=1
5+1=6
1/10=0'''
#solution:
'''n=123
sum=0
while n>0:
    r=n%10
    sum=sum+r#----->imp line
    n=n//10
print(sum) 
#r means remainder'''
'''to reduce the size we use while loop
until and unless there is last possibility we use while loop
important qusetions in while loop
#sum of digits
#reverse a number'''
#sum of even digits in a given number
'''n=123456
sum=0
while n>0:
    r=n%10
    if(r%2==0):
        sum=sum+r
    n=n//10
print(sum)'''
#find sum of squares of a digit in a given number'''
'''n=123
sum=0
while n>0:
    r=n%10
    sum=sum+r**2
    n=n//10
print(sum)'''
'''reverse of a number------>imp prblm
123
321
123%10=3
***
12%10=2
***
1%10=1
***
0'''
#solution:
'''n=123
rev=""
while n>0:
    r=n%10
    rev=rev+str(r)
    n=n//10
print(int(rev))'''
# COUNT THE NUMBER OF SPACE IN A STRING
'''str=input()
count=0
for i in(str):
    if i==" ":
        count+=1
print(count)'''
# METHOD2
'''s=input()
print(s.count(" "))'''
