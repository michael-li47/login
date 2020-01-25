import os.path

class DataBase:
    def __init__(self, filename):
        self.filename = os.path.join('/Users/me/Desktop/nerd_shit/kivy/login_with_DataBase', filename)
        self.users = None
        self.file = None
        self.load()

    def load(self):
        self.file = open(self.filename, "r+")
        self.users = {}
        
        for line in self.file:
            username, name, email, password = line.strip().split(";")
            self.users[username] = (name, email, password)

        self.file.close()

    def get_user(self, username):
        if username in self.users:
            return self.users[username]
        else:
            print("Account does not exist")

    def add_user(self, username, name, email, password):
        if username.strip() in self.users:
            print("Account already exists")
        else:
            self.users[username.strip()] = (name.strip(), email.strip(), password.strip())
            self.save()
    
    def remove_user(self, username):
        if username.strip() in self.users:
            self.users.pop(username.strip())
        else:
            print("Account does not exist")

    def save(self):
        with open(self.filename, "w") as f:
            for user in self.users:
                f.write(user + ";" + self.users[user][0] + ";" + self.users[user][1] + ";" + self.users[user][2] + "\n")

    def validate(self, username, password):
        if username in self.users:
            return password == self.users[username][2]
        else:
            False
        
    
    
