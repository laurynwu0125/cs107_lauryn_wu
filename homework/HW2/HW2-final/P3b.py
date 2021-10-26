# outer function to accept the inital balance
def make_withdrawal(balance):
    # Validate input
    if init_balance < 0:
        return None

    def withdraw(withdrawAmount):
        balance -= withdrawAmount
        if balance < 0:
            return None
        else:
            return balance

    return withdraw

if __name__ == "__main__":
    # Run this to test your code locally.
    # Explanation for why this does not behave correctly
    print("When a value is assigned to a variable inside a function, it considers that variable to be a local variable of the function. When we try to update the value of balance in the inner withdraw method, python thinks that the variable balance is local to the inner function and bound in that block.")
    init_balance = 2000
    withdrawal_amount = 500
    new_withdrawal_amount = 700
    wd = make_withdrawal(init_balance)
    print(wd)
    print(wd(withdrawal_amount))
    print(wd(new_withdrawal_amount))
