
# coding: utf-8

# In[ ]:


for i in range (6):

   if i==2:
       continue
   elif i==4:
       continue
   print(i)


# In[ ]:


for i in range(100):
   if i%2==1:
       print(i)


# In[ ]:


i=1
while i<21:
   if i%15==0:
       print(i)
       break
   i+=1


# In[ ]:


list1 = [[5, 7, -7, "abc"], [2, 4, True, 3], [4, 6, 7, 7], [2, 4, 1, True]]
for i in range(len(list1)):
   for j in range(len(list1[i])):
       a = list1[i][j]
       if a == 3:
           break
       print(list1[i][j])
   if a == 3:
       break

