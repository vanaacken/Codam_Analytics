import pymongo

client = pymongo.MongoClient("mongodb://localhost:27017/")
# Database Name
db = client["test"]
# Collection Name
col = db["venmo"]
username	= "payment.actor.username"
first_name	= "payment.actor.first_name"
last_name	= "payment.actor.last_name"
target		= "payment.target.user.username"
pp 			= "payment.actor.profile_picture_url"
note		= "note"
os			= "app.name"


user = raw_input('Enter your username please: ')
select = col.find( { username: user }, { username: 1, first_name: 1, last_name: 1, target: 1, note: 1, os: 1, pp: 1 }  )
for data in select:
	print("first name:      " + str(data.get("payment").get("actor").get("first_name")))
	print("last name:       " + str(data.get("payment").get("actor").get("last_name")))
	print("profile picture: " + str(data.get("payment").get("actor").get("profile_picture_url")))
	break
print("\nmade payments to: ")
for data in select:
	payment = ("  [" + str(data.get("payment").get("target").get("user").get("username")) + "]").ljust(30, ' ')
	payment_note = ("for \"" + str(data.get("note")) + "\"").ljust(30, ' ')
	payment_os = "from '" + str(data.get("app").get("name")) + "'"
	print(payment + payment_note + payment_os)
