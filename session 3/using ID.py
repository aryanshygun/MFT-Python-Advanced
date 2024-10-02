# different ID
var = 123
print(id(var))
var += 23
print(id(var))
# because: this is what happens var(old) = var(new) + 23
# same with str
string = 'abcd'
print(id(string))
string += 'e'
print(id(string))
# ID changes again same as digit
# but for list its different
xlist = ['a','b','c','d']
print(id(xlist))
xlist.append('e')
print(id(xlist))
# id doesnt change. because unlike the other two, we are adding to the same variable
