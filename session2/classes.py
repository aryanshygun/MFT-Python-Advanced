class User:
    # xdict = {}
    count = 0
    def __init__(self, username, password) -> None:
        self.username = username
        self.password = password
        # check = True
        User.count += 1
        # self.xdict[username] = [password, check]
    
    def getpass(self):
        return self.xdict[self.username]
    
u1 = User('ryan', '1223')
u2 = User('arash', '3456')

# User.check = 543
# print(u1.check)
# print (User.check)
# print(type(u1.getpass()))

# print(User.check)
print(u1.count)
print(u2.count)