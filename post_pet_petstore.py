import requests
import json
import common as c


def post_request():
    config = c.get_configuration()
    data = c.fetch_data()

    session = requests.session()

    for item in data["data"]:
        req = session.post(url=config["url"], headers=config["headers"], json=item)

        assert req.status_code == 200, "The request failed"
        assert (
            json.loads(req.content)["id"] == item["id"]
        ), "The returned value is wrong (id)"
        assert json.loads(req.content) == item, "The returned json is wrong"


post_request()
