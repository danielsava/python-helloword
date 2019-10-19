# pip install pymongo

from pymongo import MongoClient


connection = MongoClient('localhost', 27017)

db = connection.ligado

albuns = db.albuns

album = albuns.find_one()

print(album['nome'])






