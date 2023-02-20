#!/usr/bin/env python
# coding: utf-8

# In[4]:


print("Введите логин и пароль")
print("Логин: ")
login = input()
print("Пароль: ")
pswd = input()
length = len(pswd)
if (length <= 4):
    print("Пароль слишком короткий")
else:
    print("Добро пожаловать, ", login)


# In[7]:


print("Вы должны закодировать слово в строке из букв. Шаг, который пропускает символ задаете сами")
print("Напишите закодированное слово")
word = input()
word[::2]


# In[26]:


print("Enter the text: ")
word = input()
print("Enter the word that we have to find: ")
key = input()
a = word.find(key)
print("Your word begins from ", a, "index")


# In[17]:


a = []
word = "I, can, split, this, string, to, list, of, words"
a = word.split(", ")
for i in a:
    print(i)


# In[30]:


flag = True
while flag:
    print("Enter the title of the article: ")
    title = input()
    if title.istitle():
        print("Nice title, bro")
        flag = False
    else:
        print("Wait, why your title begins from lower letter? Are you drunk?")


# In[34]:


print("Кодировка: ")
print("Кодирование из ASCII на англ - 1, кодирование с англ в ASCII - 2, ")
choice = int(input())
if choice == 1:
    print("Введите число, которое требуется преобразовать в символ")
    number = int(input())
    print("Число соответствует значению: ", chr(number))
else:
    print("Введите текст, который требуется преобразовать в ASCII код")
    text = input()
    print("Текст соответствует значению: ", ord(text))


# In[37]:


print("Enter the text: ")
text = input()
print("If you forget to turn off CAPS LOCK or do the first letter to upper, we'll fix it autimaticly :) ")
print(text.capitalize())


# In[39]:


print("Enter the text: ")
text = input()
print("You pranked XDD ")
print(text.swapcase())


# In[43]:


print("Enter some text: ")
text = input()
print("Let's do your text a little longer :D ")
print(text.ljust(20, "-"))
print(text.rjust(20, "-"))
print(text.ljust(12, "-") + text.rjust(12, "-"))


# In[20]:


sorted = []
print("Введите цифру и затем букву. Повторите операцию 3 раза")
for i in range(0, 6): 
    notsorted = input()
    sorted.append(notsorted)

for i in range(0, len(sorted), 2):
    min = sorted[i]
    index = i
    for j in range(i+2, len(sorted), 2):
        if min>sorted[j]:
            min = sorted[j]
            index = j
    sorted[index] = sorted[i]
    temp = sorted[index+1]
    sorted[index+1] = sorted[i+1]
    sorted[i+1] = temp
    sorted[i] = min
print(sorted)


# In[23]:


print("Please enter the text: ")
string = input()
countUpper=0
countLower=0
text = string.replace(' ', '')
for i in text:
    if i.isupper():
        countUpper = countUpper + 1
    else:
        countLower = countLower + 1
if countUpper > countLower:
    string = string.upper()
elif countLower > countUpper:
    string = string.lower()
else:
    string = string.lower()
print("Upper: ", countUpper)
print("Lower: ", countLower)
print(string)


# In[24]:


flag = True
while flag:
    num1 = input("Enter the first number: ")
    if num1.isdigit():
        flag = False
    else:
        print("This is not a number!!! BOZO")
flag = True
while flag:
    num2 = input("Enter the second number: ")
    if num2.isdigit():
        flag = False
    else:
        print("This is not a number!!! BOZO")
print("Sum of the numbers: ", int(num1)+int(num2))

