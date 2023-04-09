import random


print("----- First Hero -----")
name1 = input("Please type your hero's name: ")
while True:
    if name1 == "":
        print("You did not enter a name.")
        print("----- First Hero -----")
        name1 = input("Please type your hero's name:")
    elif name1 != "":
        break
print("----- Second Hero -----")
name2 = input("Please type your hero's name: ")
while True:
    if name2 == "":
        print("You did not enter a name.")
        print("----- Second Hero -----")
        name2 = input("Please type your hero's name:")
    elif name2 == name1:
        print(f"{name1} is taken, please choose another name!")
        print("----- Second Hero -----")
        name2 = input("Please write Your hero's name:")
    elif name1 != "":
        break

randomnamess = [name1, name2]
randomname = random.choice(randomnamess)
randomnamess.remove(randomname)
bb=randomnamess
aa=randomname
print(f"Coin toss result: {bb} starts first!")

def choicename():
    healthrate1 = 100
    healthrate2 = 100
    name1hp = 50
    name2hp = 50
    while True:
            print(f"--------------- {bb} Attacks !! ---------------")
            print(f"{bb}                                                      "
                  f"       {aa} ", "\n", f"HP[{healthrate1}]:", name1hp * "|", f"  HP[{healthrate2}]:",
                  name2hp * "|")
            M = int(input("Choose your attack magnitude between 1 and 50:"))
            while True:
                if M > 50 or M < 1:
                    print("The attack magnitude must be between 1 and 50. ")
                    M = int(input("Choose your attack magnitude between 1 and 50:"))
                else:
                    break
            random.random()
            if random.random() > float((100 - M) / 100):

                print(f"{aa} hits {M} damage!!")
                print(f"{bb}                                                      "
                      f"       {aa} ", "\n", f"HP[{healthrate1}]:", name1hp * "|", f"  HP[{healthrate2 - M}]:",
                      "|" * int(name2hp - float(name2hp) * float(float(M / 2) / name2hp)))
                healthrate2 = healthrate2 - M
                name2hp = int(name2hp - float(name2hp) * float(float(M / 2) / name2hp))

                if healthrate2 < 1:
                    print("#" * 67, "\n", "#" * 27, f"{bb} Wins!!", "#" * 27, "\n", "#" * 67)
                    break
            else:
                print(f"Ooopsy! {bb} missed the attack!")
                print(f"{bb}                                                      "
                      f"       {aa} ", "\n", f"HP[{healthrate1}]:", name1hp * "|", f"  HP[{healthrate2}]:",
                      name2hp * "|")


            print(f"--------------- {aa} Attacks !! ---------------")
            print(f"{aa}                                                      "
                  f"      {bb} ", "\n", f"HP[{healthrate2}]:", name2hp * "|", f"  HP[{healthrate1}]:", name1hp * "|")
            M = int(input("Choose your attack magnitude between 1 and 50:"))
            while True:
                if M > 50 or M < 1:
                    print("The attack magnitude must be between 1 and 50. ")
                    M = int(input("Choose your attack magnitude between 1 and 50:"))
                else:
                    break
            random.random()
            if random.random() > float((100 - M) / 100):
                print(f"{bb} hits {M} damage!!")
                print(f"{aa}                                                      "    f"       {bb} ", "\n",
                      f"  HP[{healthrate2}]:", name2hp * "|", f"HP[{healthrate1 - M}]:",
                      "|" * int(name1hp - float(name1hp) * float(float(M / 2) / name1hp)))
                healthrate1 = healthrate1 - M
                name1hp = int(name1hp - float(name1hp) * float(float(M / 2) / name1hp))

                if healthrate1 < 1:
                    print("#" * 67, "\n", "#" * 27, f"{aa} Wins!!", "#" * 27, "\n", "#" * 67)
                    break
            else:
                print(f"Ooopsy! {aa} missed the attack!")
                print(f"{bb}                                                      "
                      f"       {aa} ", "\n", f"HP[{healthrate1}]:", name1hp * "|", f"  HP[{healthrate2}]:",
                      name2hp * "|")

def againgame():
    again = input("Do you want to play another round (Yes or No)? :")
    while True:
        if again != "No" and again != "Yes":
            again = input("Do you want to play another round (Yes or No)? :")
        elif again == "Yes":
            choicename()
            break
        else:
            print("Thanks for playing! See you again")
            break


choicename()
againgame()


