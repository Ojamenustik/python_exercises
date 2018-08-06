
# coding: utf-8

# In[1]:


print("Hi Ania")


# In[4]:


n = 1
while n <= 3:
    print("Hi Ania")
    n+=1


# In[9]:


import time as t
import webbrowser as web

current_time = t.ctime()
print ("start time = " + current_time)
n = 1
while n <= 3:
    t.sleep(2)
    web.open("https://www.google.pl/")
    n+=1


# In[18]:


from string import digits
import os
def rename_files():
    file_list = os.listdir(r"C:\Users\ASUS\Desktop\aniak\aniak\bazy\Nowy folder")
    print(file_list)
    saved_path = os.getcwd()
    print("Current Working Directory: "+saved_path)
    os.chdir(r"C:\Users\ASUS\Desktop\aniak\aniak\bazy\Nowy folder")
    for file_name in file_list:
        remove_digits = str.maketrans('', '', digits)
        new_name = file_name.translate(remove_digits)
        os.rename(file_name, new_name)
    os.chdir(saved_path)
    
rename_files()

