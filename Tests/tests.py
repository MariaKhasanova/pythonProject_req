import kwargs as kwargs
import requests
import json


status = "avaiable"

res = requests.get( f"https://petstore.swagger.io/v2/pet/findByStatus?status={status}", headers = {'accept': 'application/json'})

print(res.status_code)
print(res.text)
print(res.json())
print(type(res.json()))


info = {
  "id": 0,
  "category": {
    "id": 0,
    "name": "valera"
  },
  "name": "ciao ciao",
  "photoUrls": [
    "valera"
  ],
  "tags": [
    {
      "id": 0,
      "name": "valera"
    }
  ],
  "status": "available"
}
response = requests.post(f"https://petstore.swagger.io/v2/pet", headers={'accept': 'application/json', 'Content-Type': 'application/json'},data=json.dumps(info, ensure_ascii=False))


new_info = {
 "id": 0,
"category": {
    "id": 0,
    "name": "valerik"
  },
  "name": "ciao ciao",
  "photoUrls": [
    "no foto"
  ],
  "tags": [
    {
      "id": 0,
      "name": "valerik"
    }
  ],
  "status": "available"
}

petId = 9223372036854776000
res = requests.put(f"https://petstore.swagger.io/v2/pet", headers={'accept': 'application/json', 'Content-Type': 'application/json'}, data=json.dumps(new_info, ensure_ascii=False))
print(res.status_code)
print(res.json())


res = requests.delete(f"https://petstore.swagger.io/v2/pet", **kwargs)
