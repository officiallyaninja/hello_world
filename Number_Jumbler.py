import random


def shuffle(deck):
    deck2 = []
    while len(deck) > 0:
        num = random.randint(0, len(deck)-1)
        card = deck[num]
        deck2.append(card)
        deck.remove(card)

    return deck2


while True:
    win = False
    moves = 0
    op_list = shuffle(["+", "-", "/", "*"])
    num_list = shuffle([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
    dic_num = {
        "0": num_list[0],
        "1": num_list[1],
        "2": num_list[2],
        "3": num_list[3],
        "4": num_list[4],
        "5": num_list[5],
        "6": num_list[6],
        "7": num_list[7],
        "8": num_list[8],
        "9": num_list[9]
    }
    dic_op = {
        "+": op_list[0],
        "-": op_list[1],
        "/": op_list[2],
        "*": op_list[3]
    }
    print(op_list)
    print(num_list)
    print("in number jumbler, each number from 0-9 and each operation has its value randomized. 0 might now be 5, "
          "and 5 now be 8, plus might mean division.\n"
          "the aim of the game is to figure out what each number and operation means\n")
    print("all commands must be typed into the operation selection\n"
          "\n + - * / do the operation that has been assigned to those symbols.\n"
          " note: division means floor division. and subtraction gives absolute values\n"
          " 5/3 would give 1 with a  remainder of 2, so you only see 1.\n"
          " of course in the game 5 and 3 may not be 5 and 3,"
          "and / may not mean division.\n"
          " also, 1-5 gives 4 not -4\n")
    print("once you think you've figured it out,you may guess,type \'guess\' note:a wrong guess Will lose you the game."
          " and guess what each of the symbols and numbers mean")
    print("Have fun ^_^\n")
    while not win:
        op = input("Enter Operation: ").lower()
    #   guessing
        try:
            op = dic_op[op]
            num1 = dic_num[input("Enter first number")]
            num2 = dic_num[input("Enter second number")]
            if num1 == num2:
                print("both numbers cannot be the same")
                continue

            if op == "+":
                print(num1 + num2)
            elif op == "-":
                print(abs(num1 - num2))
            elif op == "/":
                print(num1 // num2)
            elif op == "*":
                print(num1*num2)
            else:
                print("ERROR")
            moves += 1
        except KeyError:
            if op == "guess":
                win = True
                for (key) in dic_num.keys():
                    guess = input("What value does " + str(key) + " have?: ")

                    print("correct: " + str(dic_num[key]))
                    if guess == str(dic_num[key]):
                        pass
                    else:
                        win = False
                for key in dic_op.keys():
                    guess = input("What value does " + str(key) + " have?: ")
                    print("correct: " + str(dic_op[key]))
                    if guess == str(dic_op[key]):
                        pass
                    else:
                        win = False
                if win:
                    print("HURRAY YOU WON! all in  only " + str(moves) + " moves")
                else:
                    print("one or more of those was wrong, sorry")
                    win = True

            else:
                print("ERROR: please select only numbers between 0-9 and/or  valid operator commands")
        except ZeroDivisionError:
            print("UNDEFINED")

    x = input("Would you like to play again? [y/n]")
    if x == "y":
        pass
    else:
        break
