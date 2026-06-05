def is_valid_schema(data):
    valid_roles = {"user", "creator", "moderator", "staff", "admin"}

    if not (
        "username" in data and isinstance(data["username"], str) and
        "posts" in data and isinstance(data["posts"], (int, float)) and not isinstance(data["posts"], bool) and
        "verified" in data and isinstance(data["verified"], bool) and
        "role" in data and isinstance(data["role"], str) and data["role"] in valid_roles and
        "badges" in data and isinstance(data["badges"], list)
    ):
        return False

    if "supporter" in data and not isinstance(data["supporter"], bool):
        return False

    return all(isinstance(badge, str) for badge in data["badges"])

print(is_valid_schema({"username": "gill", "posts": 12, "verified": False, "role": "creator", "supporter": False, "badges": ["early-adopter", "popular"]}))
print(is_valid_schema({"username": "tonya", "posts": 299, "verified": True, "role": "moderator", "supporter": True, "badges": ["streak-master", "veteran"], "followers": 1233}))
print(is_valid_schema({"username": "zara", "posts": 0, "verified": False, "role": "user", "supporter": False, "badges": []}))
print(is_valid_schema({"username": "nicole", "posts": 65, "verified": True, "role": "admin", "supporter": False, "badges": ["first-post", 18]}))
print(is_valid_schema({"username": "tim", "posts": 25, "verified": True, "role": "staff", "supporter": False}))