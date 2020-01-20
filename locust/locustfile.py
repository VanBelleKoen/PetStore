from locust import HttpLocust, TaskSet, task, between
import json


def jsonData():
    with open("./data/pet_locust.json") as json_file:
        return json.load(json_file)


def fetch(l):
    l.client.get("/44")


def create(l):
    data = jsonData()
    l.client.post("/", json=data)


class UserBehavior(TaskSet):
    @task(1)
    def create_fetch(self):
        create(self)
        fetch(self)


class WebsiteUser(HttpLocust):
    host = "https://petstore.swagger.io/v2/pet"
    task_set = UserBehavior
    wait_time = between(5.0, 9.0)
