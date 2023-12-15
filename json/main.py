import json

website = input("Name of website: ")
email = input("Email: ")
password = input("Password: ")

obj = {
    website: {
        "email": email,
        "password": password
    }
}
try:
    with open('credentials.json') as file:
        data = json.load(file)
except FileNotFoundError:
    with open('credentials.json', 'w') as file:
        json.dump(obj, file, indent=4)
else:
    data.update(obj)
    with open('credentials.json', 'w') as file:
        json.dump(data, file, indent=4)





    