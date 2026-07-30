users = [
    {
        "username": "standard_user",
        "password": "secret_sauce",
        "locked": False
    },
    {
        "username": "locked_user",
        "password": "secret_sauce",
        "locked": True
    },
    {
        "username": "problem_user",
        "password": "secret_sauce",
        "locked": False
    }
]

def connection_status(users):
    for user in users:
        if user["locked"]:
            print(f"Connexion refusée : {user['username']}")
        else:
            print(f"Connexion possible : {user['username']}")

connection_status(users)

def count_locked_users(users):
    locked_users = 0
    for user in users:
        if user["locked"]:
            locked_users += 1
    return locked_users

locked_users = count_locked_users(users)
print(f"Nombre d'utilisateurs verrouillés : {locked_users}")

        