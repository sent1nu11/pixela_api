import requests

pixela_endpoint = "https://pixe.la/v1/users"


USERNAME = "tufbot2"
TOKEN = "pqwerisf"

graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}
#
# result = requests.post(url=pixela_endpoint, json=user_params)
#
# print(result.text)

graph_params = {
    "id": "graph1",
    "name": "Minutes Learning",
    "unit": "minutes",
    "type": "int",
    "color": "sora"
}

headers = {
    "X-USER-TOKEN": TOKEN
}

# response = requests.post(url=graph_endpoint, json=graph_params, headers=headers)
# print(response.text)

pixel_creation_endpoint = f"{graph_endpoint}/graph1"

pixel_data = {
    "date": "20200531",
    "quantity": "300"
}

response = requests.post(url=pixel_creation_endpoint, json=pixel_data, headers=headers)

print(response.text)