#!/usr/bin/env python
# coding: utf-8

# ### lab 3

# In[1]:


#ques1
counter = 0

while counter < 3:
    print("Muskan")
    counter = counter + 1
else:
    print("Pooja")


# In[2]:


#ques2
num = int(input("Enter a number: "))
for i in range(0,num):
      if(i%2==0): 
        print(i)
    


# In[7]:


#ques3
start = int(input("Enter the start of range: ")) 
end = int(input("Enter the end of range: ")) 
for num in range(start, end + 1): 
    if num % 2 == 0: 
        print(num, end = " ") 


# In[10]:


for letter in 'Python': 
   if letter == 'h':
      pass
      print('This is pass block')
   print('Current Letter :', letter)

print("Good bye!")


# In[3]:


#ques5
str = input("Enter a string: ")
print("Length of the input string is:", len(str))


# In[1]:


#ques6
str = input("Enter the string : ")
total = 0
 
for i in str:
    total = total + 1
 
print("Total Number of Characters in this String = ", total)



# In[2]:


#ques7
var=input("Enter the string:")
ans=var[0:2]+var[-2:]
if(len(var)<2):
    print(ans)
else:
    print(ans)


# In[4]:


#ques8
n=input("Enter the string:")
firstchar=n[0]
newN=n.replace(firstchar,"$")
print(firstchar+newN[1: ])


# In[5]:


#ques9
x=input("Enter the string:")
y=input("Enter the string:")
print(y[0:1]+x[1: ], x[0:1]+y[1: ])


# In[16]:


str1=input("Enter the string:")
if len(str1)>2
if str1[-3]=='ing'
ing=ly
else if != 'ing'
str1[-3]='ing'


# In[ ]:





# In[ ]:




