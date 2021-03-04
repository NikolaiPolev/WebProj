import json
import urllib.request
f = open('users.json', )
data = json.load(f)
#print(json.dumps(data, indent = 2))
f.close()


class User:
    def __init__(self, data):
        self.id = data['id']
        self.name = data['name']
        self.username = data['username']
        self.email = data['email']
        self.address = data['address']
        self.phone = data['phone']
        self.website = data['website']
        self.company = data['company']
    def getData(self):
        obj = {self.id, self.name}
        return obj

class Users:
    def __init__(self):
        self.users = []

    def fetch_data(self, data):
            for user in data:
                self.users.append(User(user))

    def print_users(self):
        u = []
        for user in self.users:
            u.append(user.getData())
        print(u)

users = Users()

users.fetch_data(data)

users.print_users()