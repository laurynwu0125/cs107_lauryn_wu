# outer function to accept the inital balance
def make_withdrawal(balance):
    # Validate input
    if init_balance < 0:
        return None

    def withdraw(withdrawAmount):
        nonlocal balance
        balance -= withdrawAmount
        if balance < 0:
            return None
        else:
            return balance

    return withdraw

if __name__ == "__main__":
    # Run this to test your code locally.
    # Explanation for why this does not behave correctly
    init_balance = 2000
    withdrawal_amount = 500
    new_withdrawal_amount = 700
    wd = make_withdrawal(init_balance)
    print(wd)
    print(wd(withdrawal_amount))
    print(wd(new_withdrawal_amount))
