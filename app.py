#!/usr/bin/env python
# coding: utf-8

# In[1]:


import sys
sys.path.append("C:\\Users\\Ajay\\Desktop\\alchemy\\venv\\Lib\\site-packages")


# In[2]:


from flask_restful import Resource,Api,reqparse


# In[3]:


from flask import Flask,request,jsonify


# In[4]:


from flask_jwt import JWT,jwt_required


# In[5]:


from security import authentication,identity


# In[6]:


from resources.user import UserRegistration


# In[7]:


from resources.items import Item,ItemList


# In[8]:


from resources.store import Store,StoreList


# In[9]:


app=Flask(__name__)


# In[10]:


app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///dataaa.db'


# In[11]:


app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False


# In[12]:


app.secret_key='jose'


# In[13]:


jwt=JWT(app,authentication,identity)


# In[14]:


api=Api(app)


# In[15]:


@app.before_first_request
def create_tables():
    db.create_all()


# In[16]:


api.add_resource(Store,'/store/<string:name>')


# In[17]:


api.add_resource(StoreList,'/stores')


# In[18]:


api.add_resource(Item,'/item/<string:name>')


# In[19]:


api.add_resource(ItemList,'/items')


# In[20]:


api.add_resource(UserRegistration,'/registration')


# In[ ]:


if __name__=="__main__":
    from db import db
    db.init_app(app)
    
    
    app.run(port=5500)


# In[ ]:




