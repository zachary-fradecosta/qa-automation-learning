import json

def load_users(filepath):
    with open(filepath, "r", encoding="utf-8") as json_file:
        return json.load(json_file)

