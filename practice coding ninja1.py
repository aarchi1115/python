#!/usr/bin/env python
# coding: utf-8

# In[1]:


a=2
b=3
a+b


# In[2]:


a=2
b=5
sum=a+b
print(sum)


# In[3]:


###string and variable
a=5
b=6
sum=a+b
print("sum")
print(sum)


# In[4]:


###type function
a=234
print(type(a))
a="aarchi"
print(type(a))


# In[5]:


###id function
a=123444
print(id(a))
a=a+4
print(id(a))


# In[6]:


###storage function
a=2000
print(id(a))
b=2000
print(id(b))
##if  range is between -5 to 256 then for same numbrs same storage values will show but if it lies ahead storage values differ


# In[7]:


###arithmatic operators
a=20
b=2
sum=a+b
print(a+b)
product=(a*b)
print(product)
difference=(a-b)
print(difference)



# In[11]:



a=10
b=20
a**b


# In[12]:


a=10
b=2
a//b


# In[16]:


###to find simple interest
p=20
r=8
t=2
si=p*r*t//10
print(si)


# In[18]:


###to find circumferece of a circle
r=2
circumference=2*22//7*r
print(circumference)


# In[19]:


###user input addition
a=int(input())
b=int(input())
c=int(input())
sum=a+b+c
print(sum)


# In[20]:


###user input fahreniet into celcius
c=int(input())
conversion=(c+9//5)+32
print(conversion)


# In[22]:


# userinput simple interest
p=int(input())
r=int(input())
t=int(input())
si=p*r*t//100
print(si)


# In[4]:


###to find average marks 
a=3
b=4
c=6
sum=a+b+c
print(sum)
average=sum/3
print(average)


# In[5]:


###exponential power
x=10
n=4
power=x**n
print(power)


# In[8]:


###commom difference in arithematic code
a=1
b=3
c=5
difference=b-a 
print(difference)
difference2=c-b
print(difference2)


# In[13]:


###logical operators
a=20
b=30
a>=b


# In[15]:


###if else
a=10
b=20
if(a<b):
    print("it is correct")
else:
    print("b is correct")


# In[17]:


###whether the entered nuber is even or not
n=int(input())
check=n%2
if(check==0):
    print("n is even")
else:
    print("n is odd")


# ### 

# In[21]:


###greatest of three numbers
m=int(input())
n=int(input())
o=int(input())
if(m=n and m=o):
    print("m is greatest")
elif(n=m and n=o):
    print("n is greatest")
else:
    ("o is greatest")


# In[ ]:


###greatest of three numbers
m=int(input())
n=int(input())
o=int(input())
if(m>=n and m>=o):
    print("m is greatest")
elif(n>=m and n>=o):
    print("n is greatest")
else:
    ("o is greatest")1010


# In[28]:


###color wisw display
a=int(input())
if(0<a<5):
    print("red")
elif(5<a<100):
    print("blue")
else:
    print("yellow")


# In[4]:


####while loop
n=int(input())
i=1
while(i<=n):
    print("aarchi")
    i=i+1
   
    
 


# In[14]:


###print first ten natural numbers
n = int(input())
count = 1
while count <= n  :
    print (count)
    count = count+1
 


# In[23]:


###sum and print till n
n=int(input())
i = 1
sum = 0
while i<=n:                                                                                                                 
    sum = sum + i
    
    
    i = i + 1
print(sum)
    
    


# In[3]:


###enter a number and print the sum of all the even numbers from 1 to n
n=int(input())
sum=0
for i in range(0,n+1):
    if i%2==0:
        sum = sum + i
print(sum)
    


# In[ ]:


###enter a number and check if its primt or not
n  =int(input())
d = 2
flag = False
while d < n:
        n % d ==0
        flag = True
        d = d + 1
    
if flag:
    print("not prime")
else:
    print("prime")
   
    


# In[1]:


###enter a number adn find whether it is prime or not using for loop
n=int(input())
flag=True
for i in range(2,n):
    if n%i==0:
        flag= False
        break
if flag:
    print(n,"is prime")
else:
    print(n,"not prime")



# In[5]:


###enter a number anfd check whether prime or not uding for loop
n=int(input())
flag = True
for i in range(2,n):
    if n%i==0:
        flag = False
        break
if flag:
    print(n,"is prime")
else:
    print(n,"not prime")


# In[2]:


###enter a nuber and check if its prime or not
n=int(input())
flag = True
for i in range(2,n):
    if n%i==0:
        flag = False
        break
if flag:
    print(n,"is prime")
else:
    print(n,"not prime")
    
    


# In[8]:


###enter a number and check its reverse
n=int(input())

reverse=0
while n>0:
    sum=n%10
    reverse=(reverse*10)+sum
    n=n//10
print(reverse)
    
    
    


# In[9]:


###enter a number and check its reverse in for loop
n=str(input())
reverse=0
while n>0:
    sum=n%10
    reverse=(reverse*10)+sum
    n=n//10
print(reverse)


# In[11]:


###enter a number and check if palindromic
n=int(input())
reverse=0
while n>0:
    sum=n%10
    reverse=(reverse*10)+sum
    n=n//10
print(reverse)

if n!=reverse:
    print("palindrome")
else:
    print("not palindrome")


# In[ ]:


####make a calculator
while True:
    n=int(input())
    if n==1:
        a=int(input())
        b=int(input())
        sum=a+b
        print(sum)
    elif n==2:
        a=int(input())
        b=int(input())
        subtract=a-b
        print(subtract)
    elif n==3:
        a=int(input())
        b=int(input())
        product=a*b
        print(product)
    elif n==4:
        a=int(input())
        b=int(input())
        divide=a/b
        print(divide)
    else:
        print("invalid option")


# In[6]:


### to tell only even numbers within the list
li = [1,2,3,4,5,6,7,8,9,10,11,12]
li_new = []
for ele in li:
    if ele%2==0:
        if ele%3==0:
            li_new.append(ele)
print(li_new)


# In[9]:


li_1=[12,13,14,15,32,10,8,7,6]
li_2=[2,3,4,5,6,7,8,9,10,12,13]
li_inter = []
for ele in li_1:
    for ele_2 in li_2:
        if ele==ele_2:
            li_inter.append(ele)
print(li_inter)
        


# In[13]:


li_1=[12,13,14,15,32,10,8,7,6]
li_2=[2,3,4,5,6,7,8,9,10,12,13]
li_inter = [ele for ele in li_1 for ele_2 in li_2 if ele==ele_2]
print(li_inter)


# In[17]:


s = "aastha"
li = [ele for ele in s]
print(li)


# In[18]:


li = ["aastha","aarchi","aastik","ankita"]
li_2 = [[s for s in li]for ele in li]
print(li_2)


# In[2]:


str = input().split()
n,m = input(str[0]) , input(str[1])
li = [[int(j) for j in input().split()] for i in range(n)]
print(li)


# In[5]:


str = 'i','purple','you'
a=str.split[]
new = [[y for y in x]for x in a]
print(new)


# In[25]:


str = "i purple you"
a = str.split()
new = [[y for y in x]for x in a]
print(new)


# In[1]:


names = {'Jan': 5, 'Emi': 3, 'Johny': 7, 'Enaleanor': 2}
list_o_names = []
for name in names:
   	 if names[name] > 5:
     	   list_o_names.append(name)
print(list_o_names)


# In[ ]:


str = input('').split()
n = int(input())
for i in str:
    x = print(i[n],end="")


# In[ ]:


n = input().split()
m = input().split()
m = set(m)
n = set(n)
sum = 0
for i in m,intersection(n):
    new.add(int(i))
    sum+=int(i)
print(new)
print(sum)


# In[ ]:




