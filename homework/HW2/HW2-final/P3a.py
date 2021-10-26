# outer function to accept the inital balance
def make_withdrawal(balance):
    # Validate input
    if init_balance < 0:
        return None

    def withdraw(withdrawAmount):
        newBal = balance - withdrawAmount
        if newBal < 0:
            return None
        else:
            return newBal

    return withdraw

if __name__ == "__main__":
    # Run this to test your code locally.
    init_balance = 2000
    withdrawal_amount = 500
    new_withdrawal_amount = 700
    wd = make_withdrawal(init_balance)
    print(wd)
    print(wd(withdrawal_amount))
    print(wd(new_withdrawal_amount))
    # Explanation for why this does not behave correctly
    print("wd is defined in a block that contains only the inner make_withdrawal function, so its scope includes that block. The definitions of the functions are nested, and the inner function is not called until the outer function is called. When we define wd, wd is partially completed and is treated like a variable. Because the value of wd was not updated, the inital balance remains the same.")
