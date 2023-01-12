import requests

BASE = "http://127.0.0.1:5000/"

"""
if not working.. open cmd > python > from main import db ->db.create_all()
"""
# r_add_bulbasaur = requests.put(BASE + "pokemon/bulbasaur", {"name": "bulbasaur", "species" : "grass", "height" : 120, "weight": 24})
# response2 = requests.put(BASE + "pokemon/100", {"name": "cat", "species" : "normal", "height" : 70, "weight": 27})
# print(response2.json())
# response3 = requests.put(BASE + "pokemon/2", {"name": "pikachu", "species" : "normal", "height" : 70, "weight": 27})
# print(response3.json())

# response3 = requests.put(BASE + "pokemon/3", {"name": "mew", "species" : "normal", "height" : 70, "weight": 27})
# print(response3.json())

# response5 = requests.put(BASE + "pokemon/123", {"name": "mewtew", "species" : "normal", "height" : 70, "weight": 27})
# print(response5.json())

response158 = requests.post(BASE + "pokemon/158", {"name": "geodude", "species" : "rock", "height" : 70, "weight": 27})
print(response158.json())

#test non valid pokemon entry get
response_test_get = requests.get(BASE + "pokemon/200")
print(response_test_get.json())

#test valid pokemon entry get
response_test_get_valid = requests.get(BASE + "pokemon/3")
print(response_test_get_valid.json())


response_test_delete = requests.delete(BASE + "pokemon/158")
print(response_test_delete)

#test patch
response_test_patch = requests.patch(BASE + "pokemon/2", {"species" : "electric"})
print(response_test_patch.json())

#get after updating
response_test_get_after_update = requests.get(BASE + "pokemon/2")
print(response_test_get_after_update.json())