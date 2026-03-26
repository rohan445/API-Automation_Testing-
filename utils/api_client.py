from playwright.sync_api import sync_playwright
from config import BASE_URL, HEADERS

class APIClient:
    def __init__(self):
        self.playwright = sync_playwright().start()
        self.context = self.playwright.request.new_context(
            base_url=BASE_URL,
            extra_http_headers=HEADERS
        )

    def get(self, endpoint):
        return self.context.get(endpoint)

    def post(self, endpoint, data):
        return self.context.post(endpoint, data=data)

    def put(self, endpoint, data):
        return self.context.put(endpoint, data=data)

    def delete(self, endpoint):
        return self.context.delete(endpoint)

    def close(self):
        self.playwright.stop()