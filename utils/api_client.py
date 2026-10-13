from pytest import param


def get_user_by_id(api_session, api_base_url, user_id, timeout=10):
    url = f"{api_base_url}/users/{user_id}"
    response = api_session.get(url, timeout=timeout)
    response.raise_for_status()
    return response.json()


def get_posts_by_user_id(
    api_session,
    api_base_url,
    user_id,
    timeout=10,
):
    url = f"{api_base_url}/posts"
    params = {
        "userId": user_id
    }

    response = api_session.get(url, params=params, timeout=timeout)
    response.raise_for_status()
    return response.json()


def get_posts_page(
    api_session,
    api_base_url,
    page,
    per_page,
    timeout=10,
):
    url = f"{api_base_url}/posts"    
    params = {
        "_page": page,
        "_per_page": per_page
    }

    if not isinstance(page, int) or page < 1:
        raise ValueError(f"Invalid page: {page}")

    if not isinstance(per_page, int) or per_page < 1 or per_page > 100:
        raise ValueError(f"Invalid per_page: {per_page}")
    
    response = api_session.get(url, params=params, timeout=timeout)
    response.raise_for_status()
    return response.json()


def get_private_profile(
    api_session,
    api_base_url,
    token,
    timeout=10,
):
    url = f"{api_base_url}/profile"
    headers = {
        "Authorization": f"Bearer {token}"
    }

    response = api_session.get(url, headers=headers, timeout=timeout)
    response.raise_for_status()
    return response.json()


class APIClient:
    def __init__(self, session, base_url, default_timeout=10):
        self.session = session
        self.base_url = base_url.rstrip("/")
        self.default_timeout = default_timeout

    def _build_url(self, path):
        return f"{self.base_url}/{path.lstrip('/')}"

    def get(self, path, params=None, headers=None, timeout=None):
        url = self._build_url(path)        
        request_timeout = self.default_timeout if timeout is None else timeout

        response = self.session.get(url, params=params, headers=headers, timeout=request_timeout)
        response.raise_for_status()
        return response

    def get_user_by_id(self, user_id, timeout=None):
        path = f"/users/{user_id}"
        response = self.get(path, timeout=timeout)
        return response.json()

    def get_posts_by_user_id(self, user_id, timeout=None):
        path = "/posts"
        params = {
            "userId": user_id,
        }
        response = self.get(path, params=params, timeout=timeout)
        return response.json()

    def get_private_profile(self, token, timeout=None):
        path = "/profile"
        headers = {
            "Authorization": f"Bearer {token}"
        }
        response = self.get(path, headers=headers, timeout=timeout)
        return response.json()
