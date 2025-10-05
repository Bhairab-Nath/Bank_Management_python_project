import json
import random
import string
from pathlib import Path



class Bank:

    database = 'data.json'
    data = []

    try:
        if Path(database).exists():
            with open(database) as fs:
                data = json.loads(fs.read())


        else:
            print("No such file exists!")

    except Exception as err:
        print(f"An Error has occured! {err}")


    @classmethod
    def __update(cls):
        with open(cls.database,'w') as fs:
            fs.write(json.dumps(cls.data, indent = 4))


    @classmethod
    def __accountgenerate(cls):
        alpha = random.choices(string.ascii_letters, k = 3)
        num = random.choices(string.digits, k = 6)
        spch = random.choices("!@#%^&*$", k = 1)
        id = alpha + num + spch
        random.shuffle(id)
        return "".join(id)


    def createaccount(self):
        info = {
            "name": input("Enter your name: "),
            "age": int(input("Enter your age: ")),
            "email": input("Enter your email: "),
            "pin": int(input("Enter a 4 digit pin-code: ")),
            "accountNo.": Bank.__accountgenerate(),
            "balance": 0
        }

        if info['age'] < 18 or len(str(info['pin'])) != 4:
            print("Sorry! you cannot create an account!\nCheck your age or pin code! ")
        
        else:
            print("Account has been Created Successfully!")
            for i in info:
                print(f"{i} : {info[i]}")
            
            print("Please, note down your account number!")

            Bank.data.append(info)
            Bank.__update()

    def depositmoney(self):
        accnumber = input("Enter your account number: ")
        pin = int(input("Enter your pin-code: "))

        userdata = [i for i in Bank.data if i['accountNo.'] == accnumber and i['pin'] == pin]
        

        if not userdata:
            print("No data found!")
        
        else:
            amount = int(input("How much you want to deposit? : "))
            if amount < 500 or amount > 100000:
                print("Sorry! This amount is not acceptable.")
            
            else:
                userdata[0]['balance'] += amount
                Bank.__update()
                print("Amount Deposited successfully!")

    def withdrawmoney(self):
        accnumber = input("Enter your account number: ")
        pin = int(input("Enter your pin-code: "))

        userdata = [i for i in Bank.data if i['accountNo.'] == accnumber and i['pin'] == pin]

        if not userdata:
            print("No data found!")
        
        else:
            amount = int(input("How much you want to withdraw? : "))
            if userdata[0]['balance'] < amount:
                print("Do not have that much money!")
            
            else:
                userdata[0]['balance'] -= amount
                Bank.__update()
                print("Amount has been withdrawn successfully!")

    def showdetails(self):

        accnumber = input("Enter your account number: ")
        pin = int(input("Enter your pin-code: "))

        userdata = [i for i in Bank.data if i['accountNo.'] == accnumber and i['pin'] == pin]        

        print("\nYour Details are:\n")
        for i in userdata[0]:
            print(f"{i} : {userdata[0][i]}")
        
    def updatedetails(self):

        accnumber = input("Enter your account number: ")
        pin = int(input("Enter your pin-code: "))

        userdata = [i for i in Bank.data if i['accountNo.'] == accnumber and i['pin'] == pin]

        if not userdata:
            print("No data found!")
        
        else:
            print("Note: You cannot change age, account number, balance: ")
            print("\nFill the details for change or leave it empty for no change: ")

            newdata = {
                "name" : input("Provide new name or press enter to skip: "),
                "email" : input("Provide new email or press enter to skip: "),
                "pin" : input("Provide new pin or press enter to skip: ")

            }

            if newdata['name'] == "":
                newdata['name'] = userdata[0]['name']

            if newdata['email'] == "":
                newdata['email'] = userdata[0]['email']
                
            if newdata['pin'] == "":
                newdata['pin'] = userdata[0]['pin']
            
            newdata['age'] = userdata[0]['age']
            newdata['accountNo.'] = userdata[0]['accountNo.']
            newdata['balance'] = userdata[0]['balance']

            if type(newdata['pin']) == str:
                newdata['pin'] = int(newdata['pin'])

            for i in newdata:
                if newdata[i] == userdata[0][i]:
                    continue
                else:
                    userdata[0][i] = newdata[i]
            
            Bank.__update()
            print("Details Updated Successfully!")

    def deleteaccount(self):

        accnumber = input("Enter your account number: ")
        pin = int(input("Enter your pin-code: "))

        userdata = [i for i in Bank.data if i['accountNo.'] == accnumber and i['pin'] == pin]
    
        if not userdata:
            print("No data found!")
        
        else:
            check = input("Press y if you actually want to delete account or press n for no:  ")
            if check == 'y' or check == 'Y':
                index = Bank.data.index(userdata[0])
                Bank.data.pop(index)
                print("Account Deleted Successfully!")
                Bank.__update()
            
            else:
                print("Failed to delete!")


user = Bank()


print("Create an account: press 1 ")
print("Deposit Money to Bank: press 2 ")
print("Withdraw Money: press 3 ")
print("View Details: press 4 ")
print("Update Details: press 5")
print("Delete Account: press 6")

check  = int(input("How can I help you? "))

if check == 1:
    user.createaccount()

if check == 2:
    user.depositmoney()

if check == 3:
    user.withdrawmoney()

if check == 4:
    user.showdetails()

if check == 5:
    user.updatedetails()

if check == 6:
    user.deleteaccount()




