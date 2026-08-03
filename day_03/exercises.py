import json
with open("users.json", "r") as file:
    users = json.load(file)

#Exercise 1: display the number of users in the list.
def count_users(users):
    return len(users)

user_count = count_users(users)
print(f"Number of users: {user_count}")


#Exercise 2: Reuse the get_active_users function from day_02/exo01.py to display the usernames of active users.
def get_active_users(users):
    active_users = []
    for user in users:
        if not user["locked"]:
            active_users.append(user)
    return active_users

active_users = get_active_users(users)
for user in active_users:
    print(user["username"])

#Ticket QA-003:
def load_users(filepath):
    with open(filepath, "r") as jsonfile:
        return json.load(jsonfile)

users = load_users("users.json")
print(f"Loaded {len(users)} users from users.json")


#Exercise 3: Filter users by role and display their usernames.
def get_users_by_role(users, role):
    users_by_role = []
    for user in users:
        if user["role"] == role:
            users_by_role.append(user)
    return users_by_role

admins = get_users_by_role(users, "admin")
customers = get_users_by_role(users, "customer")

for user in admins:
    print(f"Admin : {user['username']}")
for user in customers:
    print(f"Customer: {user['username']}")


#Exercise 4: Verify the invalid users by checking if they have a username and a password.
def is_valid_user(user):
    if not user["username"] or not user["password"]:
        return False
    return True

def get_eligible_users(users):
    eligible_users = []

    for user in users:
        if (
            not user["locked"]
            and user["role"] == "customer"
            and is_valid_user(user)
        ):
            eligible_users.append(user)

    return eligible_users

eligible_users = get_eligible_users(users)

for user in eligible_users:
    print(f"Utilisateur éligible : {user['username']}")

#Challenge: Return users with empty passwords and display their usernames.
def find_users_without_password(users):
    users_without_password = []
    for user in users:
        if not user["password"]:
            users_without_password.append(user)
    return users_without_password

users_without_password = find_users_without_password(users)
for user in users_without_password:
    print(f"User without password: {user['username']}")
    