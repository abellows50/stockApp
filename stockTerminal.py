import stock
import os

class User:
    def __init__(self,user):
        with open(f"{os.getcwd()}\\programFiles\\{user}.logf","w") as userFile:
            userData = userFile.readLines()


user = input("Username: ")
# with open("programFiles/users.csv") as users:
#     myUsers = user.readlines()
#     myUsers = [u.split(",") for u in myUsers]
#     file = False
#     for auser in myUsers:
#         if auser[0] == user:
#             myPass = input("Password")
#             if myPass == auser[1]:
#                 file = auser[2]
#                 break
#     if not file:
#         myUsers.append("")     
     

theuser = User(user)
stock = stock.makeSearch(input("Stock: "))
print(stock)