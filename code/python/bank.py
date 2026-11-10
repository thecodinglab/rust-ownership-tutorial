import threading
import time


class Account:
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance


def print_report(accounts):
    for a in accounts:
        print(f"  {a.owner:<10} {a.balance:>6}")


def transfer(src, dst, amount):
    src.balance -= amount
    dst.balance += amount


def richest(accounts):
    return max(accounts, key=lambda a: a.balance)


def close_empty(accounts):
    for a in accounts:
        if a.balance == 0:
            accounts.remove(a)


def payroll(account):
    for _ in range(1000):
        b = account.balance
        time.sleep(0)
        account.balance = b + 1


def main():
    accounts = [
        Account("alice", 100),
        Account("bob", 50),
        Account("carol", 0),
        Account("dave", 0),
    ]

    print("Opening balances:")
    print_report(accounts)

    transfer(accounts[0], accounts[1], 30)

    top = richest(accounts)
    accounts.append(Account("erin", 500))
    print(f"richest before erin joined: {top.owner}")

    close_empty(accounts)
    print("After closing empty accounts:")
    print_report(accounts)

    joint = Account("joint", 0)
    alice_personal = Account("alice", 100)
    bob_personal = Account("bob", 50)
    alice_wallet = [joint, alice_personal]
    bob_wallet = [joint, bob_personal]
    transfer(alice_wallet[1], alice_wallet[0], 60)
    transfer(bob_wallet[1], bob_wallet[0], 20)
    print("After paying into the joint account:")
    print_report([joint, alice_personal, bob_personal])

    company = Account("company", 0)
    clerks = [threading.Thread(target=payroll, args=(company,)) for _ in range(4)]
    for t in clerks:
        t.start()
    for t in clerks:
        t.join()
    print(f"company balance: {company.balance} (expected 4000)")


main()
