def count_users(users):
    return len(users)


def get_active_users(users):
    active_users = []
    for user in users:
        if not user["locked"]:
            active_users.append(user)
    return active_users


def find_user(users, username):
    for user in users:
        if user["username"] == username:
            return user
    return None


def get_users_by_role(users, role):
    users_by_role = []
    for user in users:
        if user["role"] == role:
            users_by_role.append(user)
    return users_by_role


def is_valid_user(user):
    if not user["username"] or not user["password"]:
        return False
    return True


def get_eligible_users(users):
    eligible_users = []
    for user in users:
        if not user["locked"] and user["role"] == "customer" and is_valid_user(user):
            eligible_users.append(user)
    return eligible_users


def find_users_without_password(users):
    users_without_password = []
    for user in users:
        if not user["password"]:
            users_without_password.append(user)
    return users_without_password