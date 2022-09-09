from unicodedata import name
import pymongo
from bson.objectid import ObjectId
import paginate

try:
    mongo = pymongo.MongoClient(
        host="localhost",
        port=27017,
        serverSelectionTimeoutMS=1000
    )
    db = mongo.company
    mongo.server_info()
except:
    print("ERROR - Cannot connect to db")


def todo_db(name):
    todos_collection = db.todos
    todos_collection.insert_one({'name': name, 'complete': False})


def task_db():
    info = db.todos
    return list(info.find({},
                          {
                              "_id": {"$toString": "$_id"},
                              "name": 1,
                              "complete": 1,
    }
    ))


def test(task_id):
    info = db.todos
    return list(info.find(
        {'_id': ObjectId(task_id)},
        {
            "_id": {"$toString": "$_id"},
            "name": 1,
            "complete": 1,
        }
    ))


def update(task_id, name):
    todos_collection = db.todos
    todo_item = todos_collection.update_one(
        {"_id": ObjectId(task_id)},
        {"$set": {"name": name}}
    )


def delete(task_id):
    todos_collection = db.todos
    todo_item = todos_collection.delete_one(
        {
            "_id": ObjectId(task_id)
        }
    )


def task_count():
    info = db.todos
    return info.count_documents({})


def get_pagination(page_size, page_no):
    info = db.todos
    page_size = int(page_size)
    page_no = int(page_no)
    return list(info.find({},
                          {
                              "_id": {"$toString": "$_id"},
                              "name": 1,
                              "complete": 1,
                              "meta": {
                                  "page": page_no,
                                  "next_page": int(page_no),
                                  "prev_page": int(page_no)
                              }
    }).skip(page_no).limit(page_size))
