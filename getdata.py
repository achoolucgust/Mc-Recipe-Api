import random
import json

f = open("./recipes.json")
r = f.read()
f.close()
recipes = json.loads(r)

f = open("./lang.json")
r = f.read()
f.close()
lang = json.loads(r) 
