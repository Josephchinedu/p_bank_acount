class PremblyBank:
    def __init__(self, account_number: str, initial_balance: float) -> None:
        self.account_number = account_number
        self.balance = initial_balance

    def deposit(self, amount):
        self.balance += amount

        return {"message": "Deposit successful"}

    def withdraw(self, amount):
        if amount <= 0:
            return {"message": "Invalid amount. Amount should be greater than 0."}

        elif self.balance < amount:
            return {"message": "Insufficient funds"}

        self.balance -= amount

        return {"message": "Withdrawal successful"}

    def check_balance(self):
        return {"message": f"Your balance is {self.amount_formatter(self.balance)}"}

    def amount_formatter(self, amount):
        return "N{:,.2f}".format(amount)


class Helper:
    @staticmethod
    def validate_digit(input_string):
        if str(input_string).isnumeric():
            return True
        return False


if __name__ == "__main__":
    account_number = input("Enter your account number: ")
    initial_balance = input("Enter your initial balance: ")

    utility = Helper()

    if utility.validate_digit(initial_balance) == False:
        print("Invalid initial balance. Please try again. please enter a number")
        exit()

    if (len(account_number) != 10) or (utility.validate_digit(account_number) == False):
        print(
            "Invalid account number. Please try again. check the length of your account number or valid account number"
        )
        exit()

    # bank
    bank = PremblyBank(account_number, float(initial_balance))

    while True:
        print("\n\nWelcome to Prembly Bank")
        print("1. Deposit")
        print("2. Withdraw")
        print("3. Check Balance")
        print("4. Exit")

        user_choice = input("Enter your choice: ")

        if user_choice == "1":
            amount = input("Enter amount to deposit: ")
            if utility.validate_digit(amount) == False:
                print("Invalid amount. Please try again.")
                exit()

            amount = float(amount)
            print(bank.deposit(amount)["message"])

        elif user_choice == "2":
            amount = input("Enter amount to withdraw: ")
            if utility.validate_digit(amount) == False:
                print("Invalid amount. Please try again.")
                exit()

            amount = float(amount)
            print(bank.withdraw(amount)["message"])

        elif user_choice == "3":
            print(bank.check_balance()["message"])

        elif user_choice == "4":
            print("Thank you for banking with us.")
            break

        else:
            print("Invalid choice. Please try again.")
