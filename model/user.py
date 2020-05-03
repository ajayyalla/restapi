#!/usr/bin/env python
# coding: utf-8

# In[1]:


import sys
sys.path.append("C:\\Users\\Ajay\\Desktop\\alchemy\\venv\\Lib\\site-packages")


# In[2]:


sys.path.append("C:\\Users\\Ajay\\Desktop\\alchemy")


# In[3]:


from db import db


# In[2]:


import sqlite3
from flask_restful import Resource


# In[13]:


from flask_restful import reqparse


# In[9]:


class UserModel:
    
    __tablename__='users'
    
    id=db.Column(db.Integer,primary_key=True)
    username=db.Column(db.String(80))
    password=db.Column(db.String(80))
    
    
    def __init__(self,_id,username,password):
        self.id=_id
        self.username=username
        self.password=password
    @classmethod    
    def find_username(cls,username):
    
        connection=sqlite3.connect('data16.db')
        cursor=connection.cursor()
        query="select * from users where username=?"
        result=cursor.execute(query,(username,))
        row=result.fetchone()
        if row:
            user=cls(*row)
        else:
            user=None
        
        connection.close()
        return user
    @classmethod
    def find_userid(cls,_id):
        
        connection=sqlite3.connect('data16.db')
        cursor=connection.cursor()
        query="select * from users where id=?"
        result=cursor.execute(query,(_id,))
        row=result.fetchone()
        if row:
            user=cls(*row)
        else:
            user=None
        
        connection.close()
        return user

