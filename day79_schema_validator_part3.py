def is_valid_schema(data):
    valid_roles = {"user", "creator", "moderator", "staff", "admin"}

    return (
        "username" in data and isinstance(data["username"], str) and
        "posts" in data and isinstance(data["posts"], (int, float)) and
        "verified" in data and isinstance(data["verified"], bool) and
        "role" in data and isinstance(data["role"], str) and
        data["role"] in valid_roles
    )
    
print(is_valid_schema({"username": "henry", "posts": 0, "verified": True, "role": "staff"}))
print(is_valid_schema({"username": "sara", "posts": 45, "verified": False, "role": "creator", "followers": 70}))
print(is_valid_schema({"username": "penelope", "posts": 20, "verified": True, "role": "admin"}))
print(is_valid_schema({"username": "kevin", "posts": 0, "verified": False, "role": "user"}))
print(is_valid_schema({"username": "george", "posts": 15, "verified": True, "role": "moderator"}))
print(is_valid_schema({"username": "david", "posts": 0, "verified": False, "role": "guest"}))
print(is_valid_schema({"username": "wendy", "posts": 10, "verified": True}))
print(is_valid_schema({"username": "fabian", "posts": 1, "verified": True, "role": True}))
print(is_valid_schema({"username": 8, "posts": 1, "verified": True, "role": "user"}))
print(is_valid_schema({"username": "penny", "posts": "10", "verified": True, "role": "staff"}))
print(is_valid_schema({"username": "john", "posts": "1", "verified": "true", "role": "admin"}))