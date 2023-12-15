import requests
pixela_endpoint = "https://pixe.la/v1/users"
user_params = {
    "token": "5jfkro404i555",
    "username": "Deni",
    "agreeTermsofService": "yes",
    "notMinor": "yes"
}

response = requests.post(pixela_endpoint, json=user_params)
print(response.text)