from pymongo import MongoClient

cluster = "mongodb+srv://gustavo:P3n74gr4m4@cluster.ohquw.mongodb.net/?retryWrites=true&w=majority"
client = MongoClient(cluster)

db = client.Python
products = db.Products
