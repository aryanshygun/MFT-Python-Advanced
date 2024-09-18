class Users:
    user_list = []
    def __init__(self):
        # self.username = username
        # self.id_number = id_number
        # self.age = age
        
        Users.user_list.append(self.__name__)
        # Users.user_list[username] = [username, id_number, age]

    def get_users():
        users = []
        for i, j in Users.user_list.items():
            users.append(i)
        return f'Here are the users: {users.join(' ')}'
        

ryan = Users()
mehrad = Users()
reza = Users()

# print(Users.get_users())
# print(Users.user_list)
