#!/usr/bin/env python
# coding: utf-8

# In[16]:


import sqlite3


# In[17]:


import sys
sys.path.append("C:\\Users\\Ajay\\Desktop\\alchemy\\model")


# In[18]:


from model.user import UserModel


# In[19]:


def authentication(username,password):
    user=UserModel.find_username(username)
    if user and user.password==password:
        return user
    else:
        return {'message':"error"}


# In[20]:


def identity(payload):
    print('pp',payload)
    user_id=payload['identity']
    print('user_id',user_id)
    return UserModel.find_userid(user_id)

