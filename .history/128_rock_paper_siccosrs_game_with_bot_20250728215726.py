import random

def get_choice_name(choice):
    if choice == 1:
        return "1(Rock🪨)"
    elif choice == 2:
        return "2(Paper📄)"
    elif choice == 3:
        return "3(Scissors✂️)"
    else:
        return str(choice)

user = int(input("Please select one of thees options: (1): Rock🪨 (2): Paper📄 (3): Scissors✂️ "))
bot = random.choice([1, 2, 3])

user_choice = get_choice_name(user)
bot_choice = get_choice_name(bot)

if user == bot:
    print("You selected: ", user_choice, "and the bot selected: ", bot_choice, "It's a tie!")
elif user == 1 and bot == 2:
    print("You selected: ", user_choice, "and the bot selected: ", bot_choice, "You lose!")
elif user == 1 and bot == 3:
    print("You selected: ", user_choice, "and the bot selected: ", bot_choice, "You win!")
elif user == 2 and bot == 1:
    print("You selected: ", user_choice, "and the bot selected: ", bot_choice, "You win!")
elif user == 2 and bot == 3:
    print("You selected: ", user_choice, "and the bot selected: ", bot_choice, "You lose!")
elif user == 3 and bot == 1:
    print("You selected: ", user_choice, "and the bot selected: ", bot_choice, "You lose!")
elif user == 3 and bot == 2:
    print("You selected: ", user_choice, "and the bot selected: ", bot_choice, "You win!")
else:
    print("Invalid input! Please enter 1, 2, or 3.")