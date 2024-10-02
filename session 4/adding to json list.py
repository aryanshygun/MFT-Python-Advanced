import json
def add_user():

    with open('data_list.json', 'r') as infile:
        all_data = json.load(infile)

    while True:
        username = input("enter username:")
        password = input("enter password:")
        email = input("enter email:")
        all_data.append({"username": username, "password": password, "email": email})
        choice = input("Continue? [y/n]")
        if choice == 'n':
            break

    with open('data_list.json', 'w') as outfile:
        json.dump(all_data, outfile, indent=4)

def find_user(email):
    with open("data_list.json", 'r') as infile:
        database = json.load(infile)

    for i in database:
        if i['email'] == email:
            return i['username']

print(find_user('rezaii@gmail.com'))

