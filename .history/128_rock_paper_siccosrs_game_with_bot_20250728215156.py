import random

user = input("Please select one of thees options: (1): Rock🪨 (2): Paper📄 (3): Scissors✂️ ")
bot = random.choice([1, 2, 3])

if user == bot:
    print("You selected: ", user, "and the bot selected: ", bot, "It's a tie!")
elif user == 1 and bot == 2:
    print("You selected: ", user, "and the bot selected: ", bot, "You lose!")
elif user == 1 and bot == ":
    print("You selected: ", user, "and the bot selected: ", bot, "You win!")
elif user == "Paper📄" and bot == "Rock🪨":
    print("You selected: ", user, "and the bot selected: ", bot, "You win!")
elif user == "Paper📄" and bot == "Scissors✂️":
    print("You selected: ", user, "and the bot selected: ", bot, "You lose!")