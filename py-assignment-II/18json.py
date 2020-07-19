import json

me = {
    "name": "Binay Thapa",
    "age": 22
}
json_data = json.dumps(me, indent=2)
print(json_data)
print(json.loads(json_data))