import requests
import post_pet_petstore
import common as c


def delete_pet():
    data = c.fetch_data()
    config = c.get_configuration()

    for item in data["data"]:
        url = config["url"] + "/" + str(item["id"])

        req_del = requests.delete(url=url, headers=config["headers"])
        assert req_del.status_code == 200, "The request failed"

        req_get = requests.get(url=url)
        assert req_get.status_code == 404, "The deletion failed server side"


delete_pet()
