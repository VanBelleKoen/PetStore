import json

# Fetch the configuration from file
def get_configuration():
    with open("data/configuration.json") as json_file:
        return json.load(json_file)


# Get creature from json file
def fetch_data():
    with open("data/pet_crow.json") as json_file:
        return json.load(json_file)
