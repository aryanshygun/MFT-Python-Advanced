def change_case(func):
    def inner(str):
        x = func(str)
        
        if x.islower():
            return x.upper
        elif x.isupper():
            return x.lower
    return inner
            

@change_case
def string(str):
    return str

input_str = input("Please enter your string:")
answer = string(input_str)
print(answer())