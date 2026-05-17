from datetime import datetime


def mongo_id_to_date(mongo_id):

    hex_timestamp = mongo_id[:8]

    timestamp = int(hex_timestamp, 16)

    dt = datetime.utcfromtimestamp(timestamp)

    return dt.strftime("%Y-%m-%dT%H:%M:%S.000Z")

print(mongo_id_to_date("6a094b50bcf86cd799439011"))

print(mongo_id_to_date("695344eb1f4a4c1123042128"))

print(mongo_id_to_date("386da62df34123ac54617e56"))

print(mongo_id_to_date("69f571c3d7711807afd3dd55"))

print(mongo_id_to_date("68adce01c0e1144d0a90295a"))