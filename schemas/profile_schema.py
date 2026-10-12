PROFILE_SCHEMA = {
    "type": "object",
    "properties": {
        "id": {"type": "integer"},
        "username": {"type": "string"},
        "role": {"type": "string"},
    },
    "required": [
        "id",
        "username",
        "role",
    ],
    "additionalProperties": False,
    "$schema": "https://json-schema.org/draft/2020-12/schema",
}

