# -*- coding: utf-8 -*-
"""
Created on Wed Sep 27 12:38:51 2017

@author: Zana Daniel
"""

# importing required libraries
from pymongo import MongoClient
from bson.objectid import ObjectId

# opens a connection to our database
client = MongoClient('localhost', 27017)

# setting the variable 'db' to the connection
db = client.pymongodb

# function that adds a user to the db using the parameters
def createUser(username, name, age, email):
    db.users.insert_one({
            "username": username,
            "name": name,
            "age": age,
            "email": email
    })

    print("\nCreated User:\n", db.users.find_one({"username": username, "name": name, "age": age, "email": email}))

# takes in username from parenthesis to search for in db
def findUserByUserName(username):
    return print("\nFound User:\n", db.users.find_one({"username": username}))

# takes in id from parenthesis to search for in db
def findUserByID(id):
    return print("\nFound User:\n", db.users.find_one({"_id": ObjectId(id)}))

# prints all the documents in users
def findAllUsers():
    for document in db.users.find():
        print("\n", document)


#createUser("zanadaniel", "Zana Daniel", 21, "zanaadaniel@gmail.com")
#findUserByUserName("zanadaniel")
#findUserByID('59cba4cbc04b4936b8281f2c')
#findAllUsers()
