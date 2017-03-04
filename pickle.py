import pickledb
import base64

db = pickledb.load('codeviolations.db', False)

base64_key = base64.b64encode("apples")
db.set(base64_key, "MORE THINGS")

things = db.getall()

for thing in things:
	print thing +":", db.get(thing)