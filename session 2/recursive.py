x = 0

def call(x):
    if x > 100:
        return x
    
    if x % 2 == 0:
        return call(x + 2)
    else:
        return call(x + 1)

print(call(x))