import requests
import pymongo

# Fetch Nobel Prize data from API
url = "https://api.nobelprize.org/v1/prize.json"
response = requests.get(url)
data = response.json()

# Connect to MongoDB
client = pymongo.MongoClient("mongodb://mongo:27017/")
db = client["nobelprizes"]
collection = db["prizes"]

# Insert the data into MongoDB
collection.drop()  # Remove old data if re-running the script
collection.insert_many(data["prizes"])

print("Data loaded into MongoDB successfully!")
