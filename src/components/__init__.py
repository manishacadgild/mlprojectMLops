from pymongo.mongo_client import MongoClient
uri = "mongodb+srv://mongodb:mongodb@cluster0.figrh6z.mongodb.net/?retryWrites=true&w=majority"
# Create a new client and connect to the server
client = MongoClient(uri)