#!/usr/bin/env python
# coding: utf-8

# In[1]:


import sys
sys.path.append("C:\\Users\\Ajay\\Desktop\\alchemy\\venv\\Lib\\site-packages")


# In[2]:


sys.path.append("C:\\Users\\Ajay\\Desktop\\alchemy")


# In[3]:


from flask_restful import Resource,reqparse
from flask_jwt import jwt_required
from flask import jsonify


# In[4]:


from model.items import ItemModel


# In[5]:


class Item(Resource):
    parser=reqparse.RequestParser()
    parser.add_argument('price',type=float,required=True,help="This field cannot be left blank")
    parser.add_argument('store_id',type=int,required=True,help="every item needs a store_id")
    
    @jwt_required()
    def get(self,name):
        item=ItemModel.find_name(name)
        print('item',item)
        if item:
            
            return item.json()
        else:
            return {'message':'item not found'},404
  
            
    def post(self,name):
        item=ItemModel.find_name(name)
        print('item',item)
        if item:
            return {'message':"the item '{}' already exists".format(name)},400
        
        data=Item.parser.parse_args()
        
        item=ItemModel(name,data['price'],data['store_id'])
        print('item',item)
        
        try:
            item.save_to_db()
        except:
            return {"message":"An error occures inserting the item."},500
        
        return item.json(),201
            
    def put(self,name):
        data=Item.parser.parse_args()
        
        item=ItemModel.find_name(name)
        
        if item is None:
            
            item=ItemModel(name,data['price'],data['store_id'])
            
        else:
            item.price=data['price']
            item.store_id=data['store_id']
        
        item.save_to_db()
        
        return item.json()
            
        
    def delete(self,name):
        item=ItemModel.find_name(name)
        if item:
            item.delete_from_db()
        return {'message':'item deleted'}
    
    
class ItemList(Resource):
    def get(self):
        result=ItemModel.query
        print('result',result)
        items=[]
        for row in result:
            print(row)
            items.append(row.json())
            
        return {'items':items}


# In[ ]:




