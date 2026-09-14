def get_user_by_id(api_session, api_base_url, user_id):
    url = f"{api_base_url}/users/{user_id}"
    response = api_session.get(url, timeout=10)
    response.raise_for_status()
    return response.json()

