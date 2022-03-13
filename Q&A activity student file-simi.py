#!/usr/bin/env python
# coding: utf-8

# ## 1. Complete the following code to find the area of an equilateral triangle. Output should be as displayed

# In[4]:


import math
side = float(input("Enter the side of the equilateral triangle: "))
area = ((math.sqrt(3))/4)*pow(side,2)
print(round(area,3))


# ## 2. Write a program to count the number of each characters in a string

# In[9]:


InputStr=input("Enter the string :\n")
dictStr={}
for i in InputStr:
    if i not in dictStr:
        dictStr[i]=1
    else:
        dictStr[i]=dictStr[i]+1
        

for key, value in dictStr.items():
    print(f'{key} ={value}')
    


# ## 3. Write a program to find the area and perimeter of a rectangle using functions

# In[11]:


def area(l,b):
    return l*b
def perimeter(l,b):
    return (2*(l+b))

l=float(input("Enter length of rectangle:\n" ))
b=float(input("Enter bredth of rectangle: \n"))
print("Area=",round(area(l,b),3))
print("Perimeter=",round(perimeter(l,b),3))


# ## 4. Write a program to print the fibonacci series till a specified number

# In[16]:


n= int(input("enter the Number you want to see fibnocci series : \n"))
first= 0
second= 1
count = 0
while count < n:
   print(first)
   third = first + second
   first = second
   second= third
   count+=1


# ## 5. Complete the following code to find the minimum of 3 number using conditional statements. Output should be as displayed

# In[20]:


a,b,c = input("Enter three numbers followed by  : ").split()

print("First number :",a)
print("Second number :",b)
print("Third number :",c)
if(a==b==c):
    print("Entered numbers are equal!!!")
elif (a<b and  a<c):
    print(a," is smallest")
elif(b<c and  b<c):
    print(b," is smallest")
else:
    print(c," is smallest")


# ## 6. Write a program to print star pyramind. The number of rows should be taken as input from the user

# In[23]:


num=int(input("Enter number of rows"))
tot=num-1
for row in range(0,num):
    for space in range(0,tot):
        print(end=" ")
    tot=tot-1
    for col in range(0,row+1):
        print("* ",end="")
    print("\n")
    
   


# ## 7. Complete the following code to convert hour into seconds. Output should be as displayed

# In[27]:


def to_seconds(t):
    t=t*60*60
    return t
time_in_hours = float(input("Enter time in hours"))
print(time_in_hours ," Hour is equal to" ,to_seconds(time_in_hours) ," Seconds")


# ## 8. Write a program to print multiplication table as below

# In[32]:


def mulTable(n):
    for i in range(1,10):
        print(i,"*",n,"=",i*n)
        
num=int(input("Enter a number to find the multiplication table:\n"))
mulTable(num)        


# ## 9. Write a program to take your 5 favorite food as list and print each as 'I like Biriyani'

# In[38]:



favouite_food_list=input("Enter 5 favourite food:").split()
for i in favouite_food_list:
 print ("'I like",i,"' ")


# In[ ]:




