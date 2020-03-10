import pymongo								# Python needs a MongoDB driver to access the MongoDB database
myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["my_customer"]
mycol = mydb["customers"]
mydict = { "name": "John", "address": "Highway 37" }
x = mycol.insert_one(mydict)
print(myclient.list_database_names())  		# list of your system's databases
print(mydb.list_collection_names())			# list of all collections in your database
dblist = myclient.list_database_names()
if "my_customer" in dblist:
	print("The database exists.")
else:
	print("The database does NOT exists.")