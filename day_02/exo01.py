users = [
    {
        "username": "standard_user",
        "password": "secret_sauce",
        "role": "customer",
        "locked": False
    },
    {
        "username": "locked_user",
        "password": "secret_sauce",
        "role": "customer",
        "locked": True
    },
    {
        "username": "admin_user",
        "password": "admin123",
        "role": "admin",
        "locked": False
    },
    {
        "username": "problem_user",
        "password": "secret_sauce",
        "role": "customer",
        "locked": False
    }
]

#Exercise 1: Return the list of active users (not locked) from the users list.
def get_active_users(users):
    active_users = []
    for user in users:
        if not user["locked"]:
            active_users.append(user)
    return active_users

active_users = get_active_users(users)

for user in active_users:
    print(user["username"])


#Exercice 2: Find a user by username.
def find_user(users, username):
    for user in users:
        if user["username"] == username:
            return user
    return None

user = find_user(users, "admin_user")

if user:
    print(user)
else:
    print("Utilisateur non trouvé")


#Exercice 3: Filter by roles
def get_users_by_role(users, role):
    users_by_role = []
    for user in users:
        if user["role"] == role:
            users_by_role.append(user)
    return users_by_role

customers = get_users_by_role(users, "customer")

for user in customers:
    print(user["username"])


#Exercice 4: Data validation: check if all users have an username and a password.
def is_valid_user(user):
    if not user["username"] or not user["password"]:
        return False
    return True

user_valid = True

for user in users:
    if not is_valid_user(user):
        user_valid = False
        break

print(user_valid)


#Ticket QA-002
def get_eligible_users(users):
    eligible_users = []
    for user in users:
        if not user["locked"] and user["role"] == "customer" and is_valid_user(user):
            eligible_users.append(user)
    return eligible_users

eligible_users = get_eligible_users(users)

for user in eligible_users:
    print(f"Utilisateur éligible {user['username']}")



#Challenge
def get_user_statistics(users):
    total_count = len(users)
    active_count = len(get_active_users(users))
    locked_count = total_count - active_count
    admin_count = len(get_users_by_role(users, "admin"))
    customer_count = len(get_users_by_role(users, "customer"))

    return {
        "total": total_count,
        "active": active_count,
        "locked": locked_count,
        "admins": admin_count,
        "customers": customer_count
    }

user_statistics = get_user_statistics(users)
print(user_statistics)   
    