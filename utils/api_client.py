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
