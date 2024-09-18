class User:
    xdict = {}
    check = 234
    def __init__(self, username, password) -> None:
        self.username = username
        self.password = password
        self.xdict[username] = password
    
    def getpass(self):
        return self.xdict[self.username]
u1 = User('ryan', '1223')


print(u1.check)
u1.check = 323
print(u1.check)


# print(type(u1.getpass()))

# print(User.check)
