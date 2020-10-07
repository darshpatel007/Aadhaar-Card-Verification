import requests

AADHAR_CARD_NUMBER = input("Enter Aadhar Card Number : ")

API_KEY = "<YOUR_QUICKO_ACCOUNT_API_KEY>"
API_SECRET = "<YOUR_QUICKO_ACCOUNT_API_SECRET>"

# The Following Code Is For Getting Access Token
url = "https://api.quicko.com/authenticate"

payload = {}
headers = {
  'x-api-key': API_KEY,
  'x-api-secret': API_SECRET,
  'x-api-version': '3.1'
}
response = requests.request("POST", url, headers=headers, data = payload).json()
ACCESS_TOKEN = response['access_token']

# The Following Code Is For Aadhar Card Verification
url = "https://api.quicko.com/aadhaar/verify"

payload = "{\r\n    \"aadhaar_number\":\""+str(AADHAR_CARD_NUMBER)+"\"\r\n}"
headers = {
  'Authorization': ACCESS_TOKEN,
  'x-api-key': API_KEY,
  'x-api-version': '3.1'
}

response = requests.request("POST", url, headers=headers, data = payload).json()

# Response In JSON Format
print(response)