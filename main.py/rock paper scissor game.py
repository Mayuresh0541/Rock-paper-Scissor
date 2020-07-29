import random

print("""HII there......
Welcome to ROCK PAPER SCISSOR
In this game you can play various types of combinations like
1. AI vs AI
2. Player vs AI
3. Player vs player

You can find them from menu
for any query type "help" 
Enjoy gaming!!!!!!\n""")

quit_text = 'cancel'
while True:
    print("""press 1 for game modes\npress 2 for help\npress 3 for exit""")
    choice = input("> ")
    if choice == '1' or choice.lower() == 'game modes':
        print("""    1. AI vs AI\n    2. Player vs player\n    3. Player vs AI""")

        game_modes = int(input("> "))
        if game_modes == 1:
            print("    Let's start AI vs AI")
            h1 = random.randint(1, 3)
            h2 = random.randint(1, 3)
            if h1 == 1:
                hand1 = 'rock'
            elif h1 == 2:
                hand1 = 'paper'
            elif h1 == 3:
                hand1 = 'scissor'

            if h2 == 1:
                hand2 = 'rock'
            elif h2 == 2:
                hand2 = 'paper'
            elif h2 == 3:
                hand2 = 'scissor'

            print(f"\tAI1's move : {hand1}")
            print(f"\tAI2's move : {hand2}")

            if (hand1 == 'rock' and hand2 == 'rock') or (hand1 == 'paper' and hand2 == 'paper') or (
                    hand1 == 'scissor' and hand2 == 'scissor'):
                print('\n\t\t"Tie"')

            elif (hand1 == 'rock' and hand2 == 'scissor') or (hand1 == 'scissor' and hand2 == 'paper') or (
                    hand1 == 'paper' and hand2 == 'rock'):
                print('\n\t\t"AI1 Won!!!!!!!"')

            elif (hand1 == 'rock' and hand2 == 'paper') or (hand1 == 'paper' and hand2 == 'scissor') or (
                    hand1 == 'scissor' and hand2 == 'rock'):
                print('\n\t\t"AI2 won!!!!!!!"')

            print("\tDo you want to quit? quit / cancel")
            quit_text = input("> ")
            if quit_text.lower() == 'quit' or quit_text.lower() == 'q':
                print("\n\n         Thanks for playing with us!!!!!\n\n")
                exit()



        elif game_modes == 2:
            print("\tLet's start player vs player")
            p1 = input("\tPlayer 1 name : ")
            p2 = input("\tPlayer 2 name : ")
            print("""\tLet's start the game!!!!\n\tyou can type initials of move like 'r', 'p', 's'""")
            hand1 = input(f"\t{p1}'s choice : ")
            hand2 = input(f"\t{p2}'s choice : ")
            if (hand1 == 'r' and hand2 == 'r') or (hand1 == 'p' and hand2 == 'p') or (
                    hand1 == 's' and hand2 == 's'):
                print('\n\t\t"Tie"')

            elif (hand1 == 'r' and hand2 == 's') or (hand1 == 's' and hand2 == 'p') or (
                    hand1 == 'p' and hand2 == 'r'):
                print(f"\n\t\t\"{p1} Won!!!!!!!\"")

            elif (hand1 == 'r' and hand2 == 'p') or (hand1 == 'p' and hand2 == 's') or (
                    hand1 == 's' and hand2 == 'r'):
                print(f'\n\t\t"{p2} Won!!!!!!!"')

            else:
                print("\tYou haven't given a valid option.........please try again!!!!")

            print("\n\tDo you want to quit? quit / cancel")
            quit_text = input("> ")
            if quit_text.lower() == 'quit' or quit_text.lower() == 'q':
                print("\n\n         Thanks for playing with us!!!!!\n\n")
                exit()


        elif game_modes == 3:
            print("\tLet's start player vs AI")
            p = input("\tEnter player name : ")
            print("\n\tLet's start the game!!!!")
            player = input(f"\t{p}, choose your move : ")
            h2 = random.randint(0, 2)
            if h2 == 0:
                AI = 'rock'
            elif h2 == 1:
                AI = 'paper'
            elif h2 == 2:
                AI = 'scissor'

            print(f"\tAI's move : {AI}")

            if (player.lower() == 'rock' and AI == 'rock') or (player.lower() == 'paper' and AI == 'paper') or (
                    player.lower() == 'scissor' and AI == 'scissor'):
                print('\n\t\t"Tie"')

            elif (player.lower() == 'rock' and AI == 'scissor') or (player.lower() == 'scissor' and AI == 'paper') or (
                    player.lower() == 'paper' and AI == 'rock'):
                print(f"\n\t\t\"Congratulation {p}...........you Won!!!!!!!\"")

            elif (player.lower() == 'rock' and AI == 'paper') or (player.lower() == 'paper' and AI == 'scissor') or (
                    player.lower() == 'scissor' and AI == 'rock'):
                print(f'\n\t\t"OHHH {p}.....you lost.....Better luck next time"')

            else:
                print("\tYou haven't given a valid option.........please try again!!!!")

            print("\n\tDo you want to quit? quit / cancel")
            quit_text = input("> ")
            if quit_text.lower() == 'quit' or quit_text.lower() == 'q':
                print("\n\n         Thanks for playing with us!!!!!\n\n")
                exit()


    elif choice == '2' or choice.lower() == 'help':
        print("""\t\tHii............
        Welcome to help menu.
        For playing the game, every time you have to refer the key notes which we have provided.
        And while starting the game, you have to press the number associated with your choice of action.
        Other details will be provided while playing the game.
        Happy Gaming!!!!!!!
                        - Developer's Team""")

    elif choice == '3' or choice.lower() == 'exit' or choice.lower() == 'quit':
        print("\n\n         Thanks for playing with us!!!!!\n\n")
        exit()

    else:
        print("You have given wrong option......try to restart the game")
        quit()
