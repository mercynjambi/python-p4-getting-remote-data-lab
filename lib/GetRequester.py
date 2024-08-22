import requests
import json

class GetRequester:

    def __init__(self, url):
        self.url = url

    def get_response_body(self):
        # Make the GET request
        response = requests.get(self.url)
        # Ensure the response is returned as a string
        return response.content

    def load_json(self):
        # Convert the response body to a Python object
        response_body = self.get_response_body()
        return json.loads(response_body)
