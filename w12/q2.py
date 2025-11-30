import json
class Account:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.__balance = balance
        self.transaction = []

        # with open("accounts.json", "r+") as file:
        #     json.dump({owner: self.__dict__}, file, indent=4)


        with open("accounts.json", "r") as file:
            data = json.load(file)
            data.update({owner: self.__dict__})
            with open("accounts.json", "w") as file:
                json.dump(data, file, indent=4)
                # print("signed up successfully")


    def deposit(self, amount):
        self.__balance += amount

    def withdraw(self, amount):
        if amount < self.__balance:
            self.__balance -= amount
        else:
            print("Insufficient balance")

    def transfer(self, target_account:"Account", amount):
        self.withdraw(amount)
        target_account.deposit(amount)

ali = Account("Ali", 1000)
reza = Account("Reza", 2000)
print(ali.owner)