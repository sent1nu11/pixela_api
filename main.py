import requests

pixela_endpoint = "https://pixe.la/v1/users"

USERNAME = "tufbot"
TOKEN = "password"

user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}

result = requests.post(url=pixela_endpoint, json=user_params)

print(result.text)
