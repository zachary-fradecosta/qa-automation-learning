import os

API_ENVIRONMENTS = {
    "test": "https://jsonplaceholder.typicode.com",
}

def get_api_base_url():
    env = os.getenv("QA_ENV", "test")
    if env not in API_ENVIRONMENTS:
        raise ValueError(f"Invalid API environment: {env}")
    return API_ENVIRONMENTS[env]