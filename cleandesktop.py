
# coding: utf-8

# ### Imports

# In[42]:


import os


# ### Inputs

# In[43]:


desktop_directory = "/Users/peterjmyers/Desktop"
do_not_clean_files_and_folders = ['Documents', 'Temp', 'Inbox', 'Trash', '.DS_Store']


# ### Program

# In[44]:


documents = os.listdir(desktop_directory)
for doc in documents:
    if doc not in do_not_clean_files_and_folders:
        print(doc)
        os.rename("{}/{}".format(desktop_directory, doc), "{}/Temp/{}".format(desktop_directory, doc))
print("Success")
