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



