from threading import Thread, Lock


class BankAccount:
    def __init__(self, balance):
        self.__balance = balance
        self.lock = Lock()

    def deposit(self, amount):
        with self.lock:
            self.__balance += amount
            print(f"Deposited {amount}, new balance is {self.__balance}", flush=True)

    def withdraw(self, amount):
        with self.lock:
            if amount <= self.__balance:
                self.__balance -= amount
                print(f"Withdraw {amount}, new balance is {self.__balance}", flush=True)
            else:
                print(f"Failed to withdraw {amount}, current balance is {self.__balance}", flush=True)

    def get_balance(self):
        return self.__balance


class BankTread(Thread):
    def __init__(self, account, deposit_sum=100, withdraw_sum=150, quantity_operation=5, *args, **kwargs):
        super(BankTread, self).__init__(*args, **kwargs)
        self.account = account
        self.deposit_sum = deposit_sum
        self.withdraw_sum = withdraw_sum
        self.quantity_operation = quantity_operation

    def run(self):
        for _ in range(self.quantity_operation):
            self.account.deposit(self.deposit_sum)
        for _ in range(self.quantity_operation):
            self.account.withdraw(self.withdraw_sum)
