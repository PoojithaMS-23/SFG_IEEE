from pymongo import MongoClient
import certifi

uri = "mongodb+srv://poojithanamu_db_user:poojitha%4023@cluster0.w9yrukr.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"

client = MongoClient(
    uri,
    tls=True,
    tlsCAFile=certifi.where()
)

print("Connected!")
print(client.list_database_names())
