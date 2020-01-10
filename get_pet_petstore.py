import json
import requests
import post_pet_petstore
import common as c


def get_pet():
    data = c.fetch_data()
    config = c.get_configuration()
    for item in data["data"]:
        url = config["url"] + "/" + str(item["id"])

        req_post = requests.get(url=url)
        data_res = json.loads(req_post.content)

    # Asserts that the correct creature has been found
    assert req_post.status_code == 200, "The request failed"
    assert data_res == item, "The values are wrong"


get_pet()
