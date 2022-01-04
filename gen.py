import random
import string
import time



print("▄████ ▓█████  ███▄    █")
print("██▒ ▀█▒▓█   ▀  ██ ▀█   █")
print("▒██░▄▄▄░▒███   ▓██  ▀█ ██▒")
print("░▓█  ██▓▒▓█  ▄ ▓██▒  ▐▌██▒")
print("░▒▓███▀▒░▒████▒▒██░   ▓██░")
print("░▒   ▒ ░░ ▒░ ░░ ▒░   ▒ ▒")
print("░   ░  ░ ░  ░░ ░░   ░ ▒░")
print("░ ░   ░    ░      ░   ░ ░")
print("made by freemoneyhub")


num = int(input(f' How Many Emails Do You Want To Make?  : '))
length = int(input(' How Many Characters For Emails : '))
backnumbs = int(input(' How Many Numbers Do You Want On The End Of The Emails : '))
with open(f"Email{num}.txt", "w", encoding='utf-8') as file:
    print("Generating Gmails Now")
    time.sleep(2)
    print(f"Generating {num} Gmails With {length} Characters And {backnumbs} Numbers At The End\n")
    time.sleep(2)

    for i in range(num):
        code = "".join(random.choices(
            string.ascii_lowercase,
            k =(length)
        ))

        for i in range(backnumbs):
            goated = "".join(random.choices(
                string.digits,
                k=(backnumbs)
            ))

        file.write(f"{code}{goated}@gmail.com\n")

        print(f'Created : {code}{backnumbs}@gmail.com ')

with open(f"Email{num}.txt") as file:
    for line in file.readlines():
        invite = line.strip("\n")
        time.sleep(3)
        print("Generation Complete Close Tab Now")