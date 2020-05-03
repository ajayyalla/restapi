#!/usr/bin/env python
# coding: utf-8

# In[10]:


import sys
sys.path.append("C:\\Users\\Ajay\\Desktop\\alchemy\\venv\\Lib\\site-packages")


# In[11]:


sys.path.append("C:\\Users\\Ajay\\Desktop\\alchemy")


# In[12]:


from flask_restful import Resource,reqparse
from flask_jwt import jwt_required
from flask import jsonify


# In[13]:


from model.store import StoreModel


# In[14]:


class Store(Resource):
    parser=reqparse.RequestParser()
    parser.add_argument('price',type=float,required=True,help="This field cannot be left blank")
    parser.add_argument('store_id',type=int,required=True,help="This field cannot be left blank")
    
    @jwt_required()
    def get(self,name):
        store=StoreModel.find_name(name)
        if store:
            return store.json()
        return {'message':'store not found'},404
            
    def post(self,name):
        store=StoreModel.find_name(name)
        #print('item',item)
        if store:
            return {'message':"the store '{}' already exists".format(name)},400
        
        store=StoreModel(name)
        
        try:
            store.save_to_db()
        except:
            return {'message':'An error occured while creating the store'},500
        
        return store.json(),201
        
            
        
    def delete(self,name):
        store=StoreModel.find_name(name)
        if store:
            store.delete_from_db()
        return {'message':'store deleted'}
    
    
class StoreList(Resource):
    def get(self):
        result=StoreModel.query.all()
        print('result',result)
        stores=[]
        for row in result:
            print(row)
            stores.append(row.json())
            
        return {'stores':stores}


# In[ ]:




