import requests
import json
import common as c

# Get new creature request


def modify_request():
    config = c.get_configuration()
    data = c.fetch_data()
    data.update({"status": "dead"})

    session = requests.session()

    for item in data["data"]:
        item.update({"status": "dead"})
        req_post = session.post(url=config["url"], headers=config["headers"], json=item)

        assert req_post.status_code == 200, "The request failed"

        data_res = json.loads(req_post.content)
        assert data_res["status"] == "dead", "The update failed"
