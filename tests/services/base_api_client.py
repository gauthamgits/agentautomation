import requests

class BaseAPIClient:
    def __init__(self, base_url: str, token: str = None):
        self.base_url = base_url
        self.session = requests.Session()
        if token:
            self.session.headers.update({"Authorization": f"Bearer {token}"})
        self.session.headers.update({"Content-Type": "application/json"})

    def get(self, path: str, **kwargs):
        response = self.session.get(f"{self.base_url}{path}", **kwargs)
        response.raise_for_status()
        return response.json()

    def post(self, path: str, payload: dict, **kwargs):
        response = self.session.post(f"{self.base_url}{path}", json=payload, **kwargs)
        response.raise_for_status()
        return response.json()