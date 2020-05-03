#!/usr/bin/env python
# coding: utf-8

# In[1]:


import sys
sys.path.append("C:\\Users\\Ajay\\Desktop\\alchemy\\venv\\Lib\\site-packages")


# In[2]:


sys.path.append("C:\\Users\\Ajay\\Desktop\\alchemy")


# In[3]:


from db import db


# In[4]:


class StoreModel(db.Model):
    
    __tablename__='stores'
    
    id=db.Column(db.Integer,primary_key=True)
    name=db.Column(db.String(80))
    
    items=db.relationship('ItemModel',lazy='dynamic')
    
    def __init__(self,name):
        self.name=name
        
        
    def json(self):
        return {'name':self.name,'items':[item.json() for item in self.items.all()]}
     
    @classmethod       
    def find_name(cls,name):
        
        print('query',cls.query.filter_by(name=name).first())
        return cls.query.filter_by(name=name).first()
        
    
    def save_to_db(self):
        db.session.add(self)
        db.session.commit()
    
    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()
       
        

