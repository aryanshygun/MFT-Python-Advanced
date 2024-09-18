class Users:
    user_list = []
    def __init__(self, name):
        self.name = name
        Users.user_list.append(self.name)


user_name = input("Enter your name: (if finished, type 'end')\n")
while True:
    Users(user_name)
    user_name = input()
    if user_name == 'end':
        break

print(' '.join(Users.user_list))
