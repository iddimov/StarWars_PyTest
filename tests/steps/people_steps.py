from pytest_bdd import given, when, then
import requests
from tests.pages.api_page import ApiPage

@given('the SWAPI API is available')
def api_is_available(base_url):
    response = requests.get(base_url)
    assert response.status_code == 200

@then('the response status should be 200')
def check_response_status(request_person_details):
    assert request_person_details.status_code == 200

@when('I request the details for person with ID {int}')
def request_person_details(int, base_url):
    api_page = ApiPage(base_url)
    response = api_page.get_person(int)

@then('the response should contain the name {string}')
def check_person_name(request_person_details, string):
    assert request_person_details.json()["name"] == string