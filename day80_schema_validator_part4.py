def is_valid_schema(data):
    valid_roles = {"user", "creator", "moderator", "staff", "admin"}

    if not (
        "username" in data and isinstance(data["username"], str) and
        "posts" in data and isinstance(data["posts"], (int, float)) and not isinstance(data["posts"], bool) and
        "verified" in data and isinstance(data["verified"], bool) and
        "role" in data and isinstance(data["role"], str) and
        data["role"] in valid_roles
    ):
        return False

    if "supporter" in data and not isinstance(data["supporter"], bool):
        return False

    return True

print(is_valid_schema({"username": "vivian", "posts": 1, "verified": False, "role": "user", "supporter": True}))
print(is_valid_schema({"username": "rudolph", "posts": 15, "verified": True, "role": "creator"}))
print(is_valid_schema({"username": "hernandez", "posts": 35, "verified": True, "role": "moderator", "supporter": False, "followers": 55}))
print(is_valid_schema({"username": "julia", "posts": 50, "verified": True, "role": "admin", "supporter": "true"}))
print(is_valid_schema({"username": "bernard", "posts": 0, "verified": True, "role": "friend", "supporter": True}))
print(is_valid_schema({"username": "felix", "posts": 40, "verified": "yes", "role": "staff", "supporter": False}))
print(is_valid_schema({"username": "jimmy", "posts": True, "verified": False, "role": "creator", "supporter": True}))
print(is_valid_schema({"username": True, "posts": 30, "verified": True, "role": "moderator", "supporter": False}))