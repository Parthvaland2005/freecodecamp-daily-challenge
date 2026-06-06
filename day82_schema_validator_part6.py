def is_valid_schema(data):
    valid_roles = {"user", "creator", "moderator", "staff", "admin"}

    def valid_user(user):
        if not isinstance(user, dict):
            return False

        if not (
            "username" in user and isinstance(user["username"], str) and
            "posts" in user and isinstance(user["posts"], (int, float)) and not isinstance(user["posts"], bool) and
            "verified" in user and isinstance(user["verified"], bool) and
            "role" in user and isinstance(user["role"], str) and user["role"] in valid_roles and
            "badges" in user and isinstance(user["badges"], list)
        ):
            return False

        if "supporter" in user and not isinstance(user["supporter"], bool):
            return False

        if not all(isinstance(badge, str) for badge in user["badges"]):
            return False

        return True

    if "users" not in data or not isinstance(data["users"], list):
        return False

    return all(valid_user(user) for user in data["users"])


print(is_valid_schema({"users": [{"username": "ron", "posts": 14, "verified": True, "role": "creator", "badges": ["early-adopter"]}, {"username": "cher", "posts": 25, "verified": True, "role": "moderator", "supporter": True, "followers": 20, "badges": ["helper"]}]}))
print(is_valid_schema({"users": []}))
print(is_valid_schema({"users": {"username": "anne", "posts": 0, "verified": False, "role": "user", "supporter": False, "badges": []}}))
print(is_valid_schema({"users": [{"username": "tony", "posts": 10, "verified": True, "role": "creator", "supporter": True, "badges": ["liked", 6]}]}))
print(is_valid_schema({"users": [{"username": "ursula", "posts": 3, "verified": False, "role": "user", "supporter": "false", "badges": ["comeback"]}]}))