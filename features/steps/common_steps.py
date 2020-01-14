from behave import *
import delete_pet_petstore as delete
import post_pet_petstore as post
import get_pet_petstore as get


@given("The database is cleared")
def step_delete(context):
    delete.delete_pet()


@Given("Create a new pet")
def step_post(context):
    post.post_request()


@Then("The new pet can be found")
def step_get(context):
    get.get_pet()
