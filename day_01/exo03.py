user = {
    "username": "standard_user",
    "password": "secret_sauce",
    "locked": False
}

print(user["username"])
print(user["password"])
user["locked"] = True
user["role"] = "Admin"
print(user)

