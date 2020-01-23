# Python testing framework

Simple framework written in python using the requests and behave libraries. Both libraries are created to facilitate the work of the tester. I'll explain each library in turn in order to improve understanding on the framework itself.

## Requests

The requests library enables the users to fire Rest API calls using a fairly simple process

``` python
    req = requests.get(
        url=https://petstore.swagger.io/v2/pet/1
    )
```

This simple format does several things in the background, for instance setting the headers is no longer necessary unless the call requires very specific headers to be set. At the moment this testing framework has no manually set headers. Meaning the library is taking care of that for us.

The req part of this piece of code is used to store the response of the get request. This enables the us to assert the response.

``` python
if req.status_code == 200:
    print('Success!')
elif req.status_code == 404:
    print('Not Found.')
```

In this sense requests in python can be compared with RestAssured in java.

## Behave

The behave library is required in order to use Cucumber and Gherkin in python. Both are often requested by business in order to translate user stories into workable code blocks. Allowing the business counterparts to know which scenario's are being tested.

Behave has another advantage. The notion of the context is introduced. This is incredible valuable as it allows the tester to store and use variables in the different Gherkin steps. This facilitate writing more generic test code.

``` python
@Given("The user requests the status")
def get_stat(context):
    context.response = stat.get_status()

@Then('The response code is 200')
def validate_res_code(context, code):
    assert str(context.response.status_code) == 200, "The request has failed"
```

In this code block a request is being done, the result is stored into the context and validated in a different step.

## Installation

Python 3.8 is required in order to use this testing framework. You can download it from the python download page, link below. Do not forget to install pip as well. This is needed to install the different requirements of the framework.

``` BASH
pip install requirements.txt
```

This command will install both Behave and Requests based on the requirements.txt file included in the repository.

## Usage of the cucumber feature files

Only two commands are required to run the tests.

``` BASH
behave -wip

behave --tags=active
```

The wip tag will run the tests tagged as `work in progress` . While the active tag will run all different valid and active tests. These will activate the feature files, which will in turn activate the code.

## requests_toolbelt.utils

In a few python files there will be the following import

``` python
from requests_toolbelt.utils import dump
```

This is used in order to troubleshoot the requests and the actual framework. To make matters easier for everyone this library has been included in the requirements.txt

## Locust

As a load Testing tool locust preforms admirable. Start the tool by typing locust in the terminal and navigate to localhost.8089. There you can set the amount of users and the spawn rate.

## Sources

[Python Download Page](https://www.python.org/downloads/)

[Behave Documents Page](https://behave.readthedocs.io/en/latest/index.html)

[Requests Documents Page](https://2.python-requests.org/en/master/)

[Locust Documents Page](https://docs.locust.io/en/stable/)

