import random

user = input("Please select one of thees options: (1): Rock🪨 (2): Paper📄 (3): Scissors✂️")
bot = random.choice(["Rock🪨", "Paper📄", "Scissors✂️"])

if user == bot:
    print("You selected: ", user, "and the bot selected: ", bot, "It's a tie!")