import requests
import common as c


def delete_pet():
    data = c.fetch_data()
    config = c.get_configuration()

    for item in data["data"]:
        url = config["url"] + "/" + str(item["id"])

        req_del = requests.delete(url=url, headers=config["headers"])
