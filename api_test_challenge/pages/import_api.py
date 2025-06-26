import requests

class ImportAPi:
    def __init__(self, base_url, token):
        self.base_url = base_url
        self.headers = {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {token}"
        }

    def post_person(self, person_id):
        payload = [{"personId": person_id}]
        response = requests.post(f"{self.base_url}/import", headers=self.headers, json=payload)
        return response