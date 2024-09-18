def outer_outer_authentication(stored_data):
    def outer_authentication(func):
        def inner_authentication(u, p):
            username, password = func(u, p)
            if username == stored_data["username"] and password == stored_data["password"]:
                return "Welcome to your profile!"
            else:
                return "Failed to your profile!"
        return inner_authentication
    return outer_authentication

userId = input( 'enter your id')
userKey = input('enter your key')
stored_data = {"username" : "admin", "password" : "secret"}

@outer_outer_authentication(stored_data)
def get_data(username, password):
    return username, password

result = get_data(userId, userKey)
print(result)

# def outer_outer_authentication(stored_data):
#     def outer_authentication(func):
#         def inner_authentication(u, p):
#             username, password = func(u, p)
#             if username in stored_data and stored_data[username]["password"] == password:
#                 return "Welcome to your profile!"
#             else:
#                 return "Failed to access your profile!"
#         return inner_authentication
#     return outer_authentication

# userId = input('Enter your ID: ')
# userKey = input('Enter your key: ')
# stored_data = {
#     "admin": {
#         "password": "secret"
#     },
#     "john_doe": {
#         "password": "123"
#     }
# }

# @outer_outer_authentication(stored_data)
# def get_data(username, password):
#     return username, password

# result = get_data(userId, userKey)

# print(result)