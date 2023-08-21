import pymongo
import json
from typing import List

from fastapi import APIRouter

from api import models, schemas

myclient = pymongo.MongoClient("mongodb+srv://mangesh:qetBL9rmcmb2Zo1L@cluster0.0fixzhu.mongodb.net/")
mydb = myclient["mydatabase"]
mycol = mydb["beenverified"]
api_router = APIRouter()


@api_router.get("/")
async def hello(state : str | None = None, city : str | None = None, zip : str | None = None, min_age: str | None = None, max_age : str | None = None):
    query = {}
    if state:
        query["State"] = state
    if city:
        query["City"] = city
    if zip:
        query["Zip"] = zip
    if min_age == None:
        min_age = "0"
    if max_age == None:
        max_age = "500"
    query["Age"] = {"$gt": min_age, "$lt": max_age}
    print(query)
    res = mycol.find_one(query)
    res.pop("_id")
    json_data = json.dumps(res)
    json_without_slash = json.loads(json_data)
#   for i in res:
#     print(i)
    return json_without_slash