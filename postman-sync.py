import requests
import json

POSTMAN_API_KEY=''

#remote postman url
url = "https://www.postman.com/collections/abcd1234567890"

# local postman collection
UUID="7654321-a12b3c4d-321a-21eb-a8a6-2bbac3gh6543"

payload={}
headers = {
    'Accept': 'application/json'
}

response = requests.request("GET", url, headers=headers, data=payload)

# print(response.text)

url = "https://api.getpostman.com/collections/"+UUID

payload = json.dumps({"collection":json.loads(response.text)})

headers = {
  'x-api-key': POSTMAN_API_KEY,
  'Content-Type': 'application/json'
}

response = requests.request("PUT", url, headers=headers, data=payload)

print(response.text)
