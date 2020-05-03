#!/usr/bin/env python
# coding: utf-8

# In[1]:


import sys
sys.path.append("C:\\Users\\Ajay\\Desktop\\alchemy\\venv\\Lib\\site-packages")


# In[2]:


sys.path.append("C:\\Users\\Ajay\\Desktop\\alchemy")


# In[3]:


from model.user import UserModel


# In[4]:


import sqlite3
from flask_restful import Resource


# In[5]:


from flask_restful import reqparse


# In[6]:


class UserRegistration(Resource):
    parser=reqparse.RequestParser()
    parser.add_argument('username',type=str,required=True,help="This field cannot be left blank")
    parser.add_argument('password',type=str,required=True,help="This field cannot be left blank")
    def post(self):
        data=UserRegistration.parser.parse_args()
        if UserModel.find_username(data['username']):
            return {"message":"user already exists"},400
        connection=sqlite3.connect('data16.db')
        c=connection.cursor()
        query='INSERT INTO users VALUES(NULL,?,?)'
        c.execute(query,(data['username'],data['password']))
        connection.commit()
        connection.close()
        
        return {"message":"user created succesfully"},201
        

