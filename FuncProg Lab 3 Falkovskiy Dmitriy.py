#!/usr/bin/env python
# coding: utf-8

# In[13]:


print("What i need to print?")
message = input()
print("How many times i need to print it?")
a = int(input())
for i in range(0,a):
 print(message)


# 

# In[23]:


list = []
for i in range(0,4):
    a = input()
    list.append(a)
print(list)


# In[28]:


import random
print("Введите число а")
a = int(input())
print("Введите число b")
b = int(input())
random1 = random.randint(a, b)
print(f"Случайное число от а до b: {random1}")


# In[125]:


import random
list1 = []
print("Случайное число с одной границей ") 
number1 = random.randrange(30) 
print("Случайное число: ", number1)
print("последовательность чисел до случайного, включая его само")
for i in range(0,number1):
    list1.append(i+1)
print(list1)
number2 = random.randrange(10, 30) 
print("Случайное число в диапазоне: ", number2)
number3 = random.randrange(25, 201, 5) 
print("Случайное число в диапазоне, которое делится на 5: ", number3)


# In[94]:


random.random()


# In[127]:


names = ["Дмитрий", "Алишер", "Маргарита"]
enumNames = enumerate(names)
print(list(enumNames))
# [(0, 'John'), (1, 'Jane'), (2, 'Doe')]


# In[130]:


a = int(input())
b = int(input())
print("numbers from a to b: ")
for i in range(a,b + 1, +1):
    print(i)


# In[116]:


a = int(input()) 
b = int(input()) 
print("numbers from a to b: ") 
if(a < b): 
    for i in range(a,b+1, +1): 
        print(i) 
else: 
    for i in range (a, b - 1, -1): 
        print(i) 


# In[122]:


a = int(input()) 
b = int(input())
print("numbers from a to b:")
for i in range (a - (a + 1) % 2, b - b % 2, -2): 
    print(i) 


# In[124]:


print("Введите длину числовой последовательности: ")
n = int(input())
sum = 0
for i in range(1, n + 1, +1):
    sum += i
print("Введите последовательность, пропустив одно число: ")
for i in range(n - 1):
    sum -= int(input())
print(sum)


# In[ ]:




