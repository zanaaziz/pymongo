# PyMongo with MongoDB
This is a basic guide to learn how to use Python's PyMongo with a MongoDB database.
In this repo, you will find a single file called PyMongo.py, which simply has different functions communicating with a localhost MongoDB databases.

# First and Foremost
Make sure you have the PyMongo distribution installed and ready to before you begin anything. For example, I am using Spyder (for scientific programming) which comes in a package with Anaconda.
Thus, I had to go to Anaconda.org and search for the PyMongo distribution there.
Also, I'm assuming you actually have MongoDB correctly installed and ready to roll on your machine (if not, go and do it...like yesterday).

At this point, run 'mongod' so that we can begin.

# Importing The Libraries
You can see on line 8 we are importing MongoClient from 'PyMongo' and on line 9 we're importing ObjectId from 'bson'.
In case you're wondering, 'bson' comes with PyMongo and it lets us access the unique object ID's of documents that MongoDB stores as binary JSON type.

```python
from pymongo import MongoClient
from bson.objectid import ObjectId
```

# Opening a Connection To The Database
Now that everything is ready, we first need to establish where to look for a database. This can be local or stored on a server. On line 13 we declare a variable called 'client' which we assign the database URL using MongoClient.
In my case, it is the default localhost at port 27017.

Note: You can also use this format
```
MongoClient('mongodb://localhost:27017/')
```
Next we create a variable called 'db' in which we assign the client followed by the name of the database we want to use or create.
Now we are ready to use the database.

```python
client = MongoClient('localhost', 27017)
```

# Inserting a Document
It's important to note, if we wish to create a new collection, it can be simply done by inserting a document into the named collection we wish to create and that's it. MongoDB will check if it exists and if not, it'll create one for us as expected.
The easiest and most convenient way to do this is by creating a function that takes in the parameters of the values we want to insert into the database. In this case, on line 19, I just used 'username', 'name', 'age' and 'email'.
As you might expect, when this function is called, it'll take in the parameters and pass them into the query we make starting at line 19.
Note: We use 'insert_one' because we're inserting one document. If it is more than one, we would use 'insert_many'. Note: 'insert_one' is simply an object.
I'll discuss what line 27 does in the next section. At the moment, we can successfully insert documents into our database from our Python program!

```python
def createUser(username, name, age, email):
    db.users.insert_one({
            "username": username,
            "name": name,
            "age": age,
            "email": email
    })

    print("\nCreated User:\n", db.users.find_one({"username": username, "name": name, "age": age, "email": email}))
```

# Getting a Document
Okay, so we can insert a document. Now lets get a document from the database and view it. Again, we create a function which takes in a parameter and in this case we want the username that we'll use to search the database for.
The 'find_one' utility lets us search for one document based on the data we tell it to search for. This data goes in an object as well like everything else in MongoDB. We're searching for the key called 'username' and the value will be whatever is passed into the function through the parameter. Of course since we're returning it as a print(), it'll nicely output the result whenever we call it later on.

```python
def findUserByUserName(username):
    return print("\nFound User:\n", db.users.find_one({"username": username}))
```

# Getting Document By ID
MongoDB is amazing, every document that's created instantly receives a unique ID which we can be used to sort through. I touched upon this when discussing the libraries, this unique ID is in BSON type data. That's why we needed to import ObjectId from bson.objectid that comes with PyMongo. Understanding this, the rest is a piece of cake. Everything is the same as finding a username except this time we're using ObjectId, which returns a string version of the ID.

```python
def findUserByID(id):
    return print("\nFound User:\n", db.users.find_one({"_id": ObjectId(id)}))
```

# Getting All Documents
Last but not least, we want a function that returns all the documents in our collection. This is easy in the mongo shell. You just run the find() command and it'll return all documents. Sadly, this doesn't work in Python so we have to bypass it but luckily it's easy to do so. On line 39 we use a simple for loop that iterates through all the documents in the collection and each time it iterates, it prints out the document and boom that's how the cookie crumbles!

```python
def findAllUsers():
    for document in db.users.find():
        print("\n", document)
```

# Last Note
There's a lot more that I could've added here but I think by understanding this, it will be easy to learn how to implement other functions such as querying (editing) documents and so on.
The last three lines contain code ready to go for calling the functions.

```python
#createUser("zanadaniel", "Zana Daniel", 21, "zanaadaniel@gmail.com")
#findUserByUserName("zanadaniel")
#findUserByID('59cba4cbc04b4936b8281f2c')
#findAllUsers()
```

Just un-comment and run.

Feel free to add more to this if you would like to contribute.

I hope you enjoyed and had as much fun as I did!
