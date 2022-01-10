wallet = []
history_of_purchases = {}


def manager_menu_fun():
    while True:
        choice = input('Choose menu section: ')
        if choice == '1':
            replenishment_fun()
            break
        elif choice == '2':
            purchase_fun()
            break
        elif choice == '3':
            history_of_purchases_fun()
            break
        elif choice == '4':
            exit_fun()
            break
        else:
            print('Incorrect input, try again!')


def menu_points():
    print('#############')
    print('1 - *Replenishment*')
    print('2 - *Purchase*')
    print('3 - *History of purchases*')
    print('4 - *Exit*\n##########')
    manager_menu_fun()


def replenishment_fun():
    add_money = float(input(f'Enter the deposit amount: '))
    wallet.append(add_money)
    manager_menu_fun()


def purchase_fun():
    add = float(input(f'Enter the price of your purchase: '))
    if add > sum(wallet):
        print('There is not enough money in your account!')
        manager_menu_fun()
    else:
        purchase = input(f'Enter the name of the purchase: ')
        wallet.append(add * -1)
        history_of_purchases[purchase] = add
        print(history_of_purchases)
        print(sum(wallet))


def history_of_purchases_fun():
    for k, v in history_of_purchases:
        print(f'List of purchases:\ntransaction:{k} price {v} btc')
    manager_menu_fun()


def exit_fun():
    print('See you later!')


menu_points()
print(wallet)
print(history_of_purchases)
