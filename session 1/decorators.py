def change_case(func):
    def inner(str):
        x_string = func(str)
        
        if x_string.islower():
            return x_string.upper
        elif x_string.isupper():
            return x_string.lower
    return inner
            

@change_case
def string(str):
    return str

input_str = input("Please enter your string:")
answer = string(input_str)
print(answer())