from classes import BankAccount, BankTread


def main():
    initial_balance = 1000
    account = BankAccount(balance=initial_balance)
    threads = []

    for _ in range(3):
        thread = BankTread(account)
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

    print(f'Final balance is {account.get_balance()}')


if __name__ == "__main__":
    main()
