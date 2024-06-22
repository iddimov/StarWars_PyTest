import requests

class ApiPage:
    def __init__(self, base_url):
        self.base_url = base_url

    def get_person(self, person_id):
        response = requests.get(f"{self.base_url}/people/{person_id}/")
        return response
