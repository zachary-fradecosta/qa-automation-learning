user = {
    "username": "Paul",
    "locked": True
}

def is_locked(user):
    if user["locked"]:
        print("Utilisateur verrouillé")
    else:
        print("Utilisateur actif")

is_locked(user)
