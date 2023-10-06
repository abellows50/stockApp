import stock
import os

class User:
    def __init__(self,user):
        created = False
        try:
            with open(f"{os.getcwd()}/programFiles/{user}.logf","r") as userFile:
                userData = userFile.readLines()
        except:
            with open(f"{os.getcwd()}/programFiles/template.logf","r") as template:
                with open(f"{os.getcwd()}/programFiles/{user}.logf","w") as userFile:
                    templateData = template.read()
                    userFile.write(templateData)
                    userData = template.readlines()
                    created = True

        bank = userData[0][:-1].split(",")
        stocks = [stockrow.split(",")[0] for stockrow in userData[1:]]

        user.money = int(bank[1])
        user.worth = user.money
        user.stocks = {}
        if not created:
            for stock in stocks:
                stockSearch = stock.makeSearch(stock)
                if stockSearch[1] != 'USD':
                    stockPrice = int(input(f"Your stock {stock} has its price in {stockSearch[1]} please convert {stockSearch[0]} {stockSearch[1]} to USD"))
                else:
                    stockPrice = stockSearch[0]
                user.worth += stockPrice
                user.stocks[stock] = stockPrice
                self.printToUser()
                
    def printToUser(self):                
        print(f"Your Net Worth: {user.worth}")
        print(f"Your Free Money: {user.money}")
        print(f"Your Stock Holdings:")
        for key in user.stocks.keys():
            print(f"{key}:{user.stocks[key]}")

        
        


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
