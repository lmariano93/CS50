amount_due = 50

while amount_due > 0:
    print(f"Amount Due: {amount_due}")
    coin = int(input("InsertCoin: "))
    if coin in [25, 10, 5]:
        amount_due -= coin

print(f"Change Owed: {amount_due * -1}")
