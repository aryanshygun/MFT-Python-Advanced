class Users:
    def __init__(self, name, age):
        self.name = name
        self.__age = age

    def get_name(self):
        return self.name

    def get_age(self):
        return self.__age

u1 = Users('ryan', 20)

