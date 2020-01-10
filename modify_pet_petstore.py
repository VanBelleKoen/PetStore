import requests
import json
import post_pet_petstore

#Get new creature request

#Load the jsonfile for the PetId
with open('pet_crow.json') as json_file:
    data = json.load(json_file)

data.update({"status": "dead"})
id = str(data["id"])

url = "https://petstore.swagger.io/v2/pet"
headers = {'Accept':'application/json' }

req_post = requests.post(url = url, params = id, headers = headers, json = data)

assert req_post.status_code == 200, "The request failed"

data_res = json.loads(req_post.content)
assert data_res["status"] == "dead", "The update failed" 

