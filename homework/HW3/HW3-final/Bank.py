from enum import Enum

class AccountType(Enum):
    SAVINGS = 1
    CHECKING = 2

class BankAccount():
    def __init__(self, owner, accountType: AccountType):
        self.owner = owner
        self.balance = 0
        self.accountType = accountType

    def withdraw(self, amount):
        if amount > self.balance:
            raise Exception("Can't withdraw more money than the balance of the account")
        if amount < 0:
            raise Exception("Can't withdraw a negative amount")
        self.balance = self.balance - amount
        return self.balance

    def deposit(self, amount):
        if amount < 0:
            raise Exception("Can't deposit a negative amount")
        self.balance = self.balance + amount
        return self.balance

    def __str__(self):
        str = "Account owner: " + self.owner + "\nAccount Type: "
        if self.accountType == AccountType.CHECKING:
            return str + "checking"
        return str + "savings"

    def __len__(self):
        return self.balance


class BankUser():
    def __init__(self, owner):
        self.owner = owner
        self.savingsAcc = None
        self.checkingAcc = None

    def addAccount(self, accountType):
        if accountType == AccountType.CHECKING:
            if self.checkingAcc != None:
                raise Exception("Checking account has already been opened")
            else:
                self.checkingAcc = BankAccount(self.owner, accountType)

        if accountType == AccountType.SAVINGS:
            if self.savingsAcc != None:
                raise Exception("Savings account has already been opened")
            else:
                self.savingsAcc = BankAccount(self.owner, accountType)


    def getBalance(self, accountType):
        if accountType == AccountType.CHECKING:
            if self.checkingAcc == None:
                raise Exception("No checking account opened")
            else:
                return self.checkingAcc.__len__()

        if accountType == AccountType.SAVINGS:
            if self.savingsAcc == None:
                raise Exception("No savings account opened")
            else:
                return self.savingsAcc.__len__()


    def deposit(self, accountType, amount):
        if accountType == AccountType.CHECKING:
            if self.checkingAcc == None:
                raise Exception("No checking account opened")
            else:
                self.checkingAcc.deposit(amount)
                return self.checkingAcc.__len__()

        if accountType == AccountType.SAVINGS:
            if self.savingsAcc == None:
                raise Exception("No savings account opened")
            else:
                self.savingsAcc.deposit(amount)
                return self.savingsAcc.__len__()


    def withdraw(self, accountType, amount):
        if accountType == AccountType.CHECKING:
            if self.checkingAcc == None:
                raise Exception("No checking account opened")
            else:
                self.checkingAcc.withdraw(amount)
                return self.checkingAcc.__len__()

        if accountType == AccountType.SAVINGS:
            if self.savingsAcc == None:
                raise Exception("No savings account opened")
            else:
                self.savingsAcc.withdraw(amount)
                return self.savingsAcc.__len__()

    def __str__(self):
        accountInfo = ""
        if self.checkingAcc != None:
            accountInfo += "Checking account balance: " + str(self.checkingAcc.__len__())
        if self.savingsAcc != None:
            accountInfo += "\nSavings account balance: " + str(self.savingsAcc.__len__())

        return accountInfo



def ATMSession(bankUser):

    def Interface():
        while True:
            prompt = input("Enter Option: \n1)Exit \n2)Create Account \n3)Check Balance \n4)Deposit \n5)Withdraw\n")
            num = int(prompt)
            if num == 1:
                exit()
            elif num == 2 or num == 3 or num == 4 or num == 5:
                prompt2 = input("Enter Option: \n1)Checking \n2)Savings\n")
                num2 = int(prompt2)
                if num == 2 and num2 == 1:
                    bankUser.addAccount(AccountType.CHECKING)
                elif num == 2 and num2 == 2:
                    bankUser.addAccount(AccountType.SAVINGS)
                elif num == 3 and num2 == 1:
                    print("Checking Account Balance: ", bankUser.getBalance(AccountType.CHECKING))
                elif num == 3 and num2 == 2:
                    print("Savings Account Balance: ", bankUser.getBalance(AccountType.SAVINGS))
                elif num == 4 or num == 5:
                    prompt3 = input("Enter Integer Amount, Cannot Be Negative:\n")
                    num3 = int(prompt3)
                    if num == 4 and num2 == 1:
                        bankUser.deposit(AccountType.CHECKING, num3)
                    elif num == 4 and num2 == 2:
                        bankUser.deposit(AccountType.SAVINGS, num3)
                    elif num == 5 and num2 == 1:
                        bankUser.withdraw(AccountType.CHECKING, num3)
                    elif num == 5 and num2 == 2:
                        bankUser.withdraw(AccountType.SAVING, num3)
                    else:
                        raise Exception("Invalid input")
                else:
                    raise Exception("Invalid input")
            else:
                raise Exception("Invalid input")

    return Interface

user = BankUser("Lauryn");
interface = ATMSession(user);
interface()
