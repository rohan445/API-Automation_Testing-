import os
import requests


class APIClient:
    """Simple HTTP API client used by tests."""

    def __init__(self, base_url=None, **kwargs):
        self.base_url = base_url or os.getenv("API_BASE_URL", "http://localhost")
        self.session = requests.Session()
        for key, value in kwargs.items():
            setattr(self.session, key, value)

    def _url(self, path: str):
        if path.startswith("http://") or path.startswith("https://"):
            return path
        return self.base_url.rstrip("/") + "/" + path.lstrip("/")

    def get(self, path, **kwargs):
        return self.session.get(self._url(path), **kwargs)

    def post(self, path, **kwargs):
        return self.session.post(self._url(path), **kwargs)

    def put(self, path, **kwargs):
        return self.session.put(self._url(path), **kwargs)

    def delete(self, path, **kwargs):
        return self.session.delete(self._url(path), **kwargs)

    def close(self):
        self.session.close()
