from Bank import BankUser
from Bank import BankAccount
from Bank import AccountType


def test_account_str_and_len(): #this test function should print the bank account's str and len function
    account = BankAccount("Lauryn", AccountType.SAVINGS);
    try:
        print(account.__str__())
        print("Account __len__: ", str(account.__len__()))
    except Exception as e:
        print(e); #print the message for the Exception

def test_add_account(): #this test function should print the user's bank info after adding accounts
    user = BankUser("Joe");
    user.addAccount(AccountType.SAVINGS);
    user.addAccount(AccountType.CHECKING);
    try:
        print(user.__str__())
    except Exception as e:
        print(e); #print the message for the Exception

def test_deposit(): #this test function should print the user's bank info after depositing
    user = BankUser("Joe");
    user.addAccount(AccountType.SAVINGS);
    user.addAccount(AccountType.CHECKING);
    user.deposit(AccountType.SAVINGS, 900);
    user.deposit(AccountType.CHECKING, 80);
    try:
        print(user.__str__())
    except Exception as e:
        print(e); #print the message for the Exception

def test_get_balance(): #this test function should print the user's balance
    user = BankUser("Joe");
    user.addAccount(AccountType.SAVINGS);
    user.deposit(AccountType.SAVINGS, 10);
    try:
        print("Balance: ", user.getBalance(AccountType.SAVINGS))
    except Exception as e:
        print(e); #print the message for the Exception

def test_withdraw(): #this test function should print the user's balance after withdrawing
    user = BankUser("Joe");
    user.addAccount(AccountType.SAVINGS);
    user.deposit(AccountType.SAVINGS, 1000);
    try:
        print("Balance before withdrawal: ", user.getBalance(AccountType.SAVINGS))
        user.withdraw(AccountType.SAVINGS, 20);
        print("Balance after withdrawal: ", user.getBalance(AccountType.SAVINGS))
    except Exception as e:
        print(e); #print the message for the Exception

def test_over_withdrawal(): #this test function should throw an Exception or Error
    user = BankUser("Joe");
    user.addAccount(AccountType.SAVINGS);
    user.deposit(AccountType.SAVINGS, 10);
    try:
        user.withdraw(AccountType.SAVINGS, 1000); #this will cause an Exception or Error
    except Exception as e:
        print(e); #print the message for the Exception

def test_negative_withdrawal(): #this test function should throw an Exception or Error
    user = BankUser("Joe");
    user.addAccount(AccountType.CHECKING);
    try:
        user.withdraw(AccountType.CHECKING, -100); #this will cause an Exception or Error
    except Exception as e:
        print(e); #print the message for the Exception

def test_negative_deposit(): #this test function should throw an Exception or Error
    user = BankUser("Joe");
    user.addAccount(AccountType.CHECKING);
    try:
        user.deposit(AccountType.CHECKING, -100); #this will cause an Exception or Error
    except Exception as e:
        print(e); #print the message for the Exception

test_account_str_and_len();
test_add_account();
test_deposit();
test_get_balance();
test_withdraw();
test_over_withdrawal();
test_negative_withdrawal();
test_negative_deposit();
