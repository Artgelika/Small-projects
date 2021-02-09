import random
random.seed(5)

def menu():
    print("1. Create an account")
    print("2. Log into account")
    print("0. Exit")


def making_random_number(leng):
    rand_list = ""
    for _ in range(leng):
        rand_list += str(random.randint(0,9))
    return rand_list


def create_card(): # generate new card number and pin
    card_number = ""
    card_number += "400000"
    card_number += making_random_number(10)
    pin_number = making_random_number(4)
    return card_number, pin_number

cardNum, pinNum = create_card()
cardNum = int(cardNum)
pinNum = int(pinNum)
# print("CARD: {} PIN: {}".format(cardNum, pinNum))

def print_created_card():
    print("Your card has been created\nYour card number:")
    print(cardNum)
    print("Your card PIN:")
    print(pinNum)


def log_in():
    # cardNum, pinNum = create_card()
    # eprint("Card number: {}, pin number: {}".format(cardNum, pinNum))
    print("Enter your card number:")
    cardNumber = int(input())
    print("Enter your PIN:")
    pinNumber = int(input())
    if (cardNumber != int(cardNum) or pinNumber != int(pinNum)):
        print("Wrong card number or PIN!")
    else:
        print("You have successfully logged in!")
        logged_in()


def logged_in():
    print("1. Balance")
    print("2. Log out")
    print("0. Exit")
    while True:
        klik = int(input())
        if klik == 1:
            amount = 0
            print("Balance: {}".format(amount))
        elif klik == 2:
            print("You have successfully logged out!")
            working()
        elif klik == 0:
            print("Bye!")
            break

def working():
    menu() # ok
    while True:
        chance = int(input())
        if chance == 1:
            create_card()
            print_created_card()
        elif chance == 2:
            log_in()
        elif chance == 0:
            print("Bye")
            break

working()