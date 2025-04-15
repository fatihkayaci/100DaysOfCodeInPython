class User:
    def __init__(self, userid, username):
        self.id = userid
        self.username = username
        self.fallowers = 0
        self.fallowing = 0

    def fallow(self, user):
        self.fallowing += 1
        user.fallowers += 1

user_1 = User("001", "Fatih")
user_2 = User("002", "Sıla")

user_1.fallow(user_2)

print(user_1.fallowers)
print(user_1.fallowing)
print(user_2.fallowers)
print(user_2.fallowing)