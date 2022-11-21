# 2 dimentional array

twoDArray = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(twoDArray[0][0])

# try and exception
try:
    print(0/0)
except ZeroDivisionError:
    print("you can't divide by zero")
except:
    print("something went wrong")

arra = [
    {
        name: "john",
        age: 20
    },
    {
        name: "jane",
        age: 21
    }
]
for i in arra:
    print(i["name"])

# Develop window application which will accept user matric number, name, lastname, and a score, form the user 