from flask import Flask, request, jsonify
import pymongo

app = Flask(__name__)

# Connect to MongoDB
client = pymongo.MongoClient("mongodb://mongo:27017/")
db = client["nobelprizes"]
collection = db["prizes"]

@app.route("/search/name", methods=["GET"])
def search_by_name():
    name = request.args.get("name")
    query = {"laureates.firstname": {"$regex": name, "$options": "i"}}
    results = collection.find(query)
    return jsonify([res for res in results])

@app.route("/search/category", methods=["GET"])
def search_by_category():
    category = request.args.get("category")
    query = {"category": {"$regex": category, "$options": "i"}}
    results = collection.find(query)
    return jsonify([res for res in results])

@app.route("/search/description", methods=["GET"])
def search_by_description():
    desc = request.args.get("description")
    query = {"laureates.motivation": {"$regex": desc, "$options": "i"}}
    results = collection.find(query)
    return jsonify([res for res in results])

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
