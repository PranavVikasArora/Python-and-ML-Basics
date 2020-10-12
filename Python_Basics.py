#!/usr/bin/env python
# coding: utf-8

# In[1]:


#Strings
score = "HelloWorld"
print(score[0])
#Indexing in Python starts from 0


# In[2]:


print(score[2:6])
#Prints from 2 to 5, last value not printed


# In[3]:


print(score[2:])
#Prints from index position 2 to the end of string


# In[4]:


#list - Contains elements inside it called items
mylist = ['hulk',3.87,'spiderman',4]
print(mylist)


# In[6]:


print(mylist[1:3])
#indexing again from 0 and vales 1 and 2 only printed last value ignored


# In[8]:


#Tuple -Collection of objects like list, but this is immutable
mytuple = ('text',4.8)
print(mytuple)


# In[9]:


#Dictionary - Unordered collection of data values, used to store data values like a map, contains key value pairs
mydict = {'name':'superman','age':40}
print(mydict)


# In[10]:


#Conditional Statements - If,elif,else
bill = int(input("enter amount of bill"))
if (bill<=500):
    print("Small party")
elif (bill>500 & bill<=1000):
    print("medium party")
else:
    print("grand party")


# In[11]:


#While-
score = 0
while(score<=20):
    print(score)
    score = score+1


# In[13]:


#For loop-
for i in "Helloworld":
    print("The letter is :", i)
    


# In[17]:


marvel = ['thor','iron man', 'hulk', 'captain america']
for char in marvel:
    print(char)


# In[18]:


#Average of numbers in a list-
listsize = int(input("enter list size"))
mylist = []
for i in range(0,listsize):
    mynum = int(input("Enter list element"))
    mylist.append(mynum)
average = sum(mylist)/listsize
print(average)


# In[20]:


#Pallindrome -
num = int(input())
temp = num
rev = 0
while num>0:
    digit= num%10
    rev = rev*10+digit
    num= num/10
if(temp== rev):
    print("Pallindrome")
else:
    print("Not Pallindrome")


# In[23]:


#Identity Matrix
matsize = int(input("Enter size of identity matrix"))
for i in range(0,matsize):
    for j in range(0,matsize):
        if(i==j):
            print("1",sep=' ',end='')
#By default print ends with new line but end  = '' tells python to continue in same line and sep ='' adds a whitespace
        else:
            print("0",sep=' ',end='')


# In[33]:


#Second largest element in list
listsize = int(input("enter size of list"))
mylist=[]
for i in range(0,listsize):
    listelement = int(input("Enter list element"))
    mylist.append(listelement)
mylist.sort()
print(mylist[listsize-2])

    
    


# In[36]:


#Merging list
list1 = [1,2,3,4]
list2 = [4,5.6,7]
listmerger = list1+list2
print(listmerger)

