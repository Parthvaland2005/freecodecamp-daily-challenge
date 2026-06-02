def is_valid_schema(data):
    return (
        "username" in data and isinstance(data["username"], str) and
        "posts" in data and isinstance(data["posts"], (int, float)) and
        "verified" in data and isinstance(data["verified"], bool)
    )

print(is_valid_schema({"username": "alice", "posts": 10, "verified": False}))  # True
print(is_valid_schema({"username": "carol", "posts": 15, "verified": True, "followers": 25}))  # True
print(is_valid_schema({"username": "frank", "posts": "21", "verified": True}))  # False
print(is_valid_schema({"username": "sam", "posts": 17, "verified": "false"}))  # False
print(is_valid_schema({"username": "bill", "verified": True}))  # False
print(is_valid_schema({"username": "fred", "verified": True}))  # False
print(is_valid_schema({"username": 5, "posts": 10, "verified": True}))  # False