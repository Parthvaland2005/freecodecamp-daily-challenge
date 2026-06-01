def is_valid_schema(data):
    return "username" in data and isinstance(data["username"], str)

print(is_valid_schema({"username": "bob"}))          # True
print(is_valid_schema({"username": "jen", "posts": 30}))  # True
print(is_valid_schema({"username": ""}))             # True
print(is_valid_schema({"username": 7}))              # False
print(is_valid_schema({"posts": 25}))                # False