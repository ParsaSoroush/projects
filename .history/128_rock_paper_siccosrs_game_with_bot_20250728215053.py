import random

user = input("Please select one of thees options: (1): Rock🪨 (2): Paper📄 (3): Scissors✂️ ")
bot = random.choice(["Rock🪨", "Paper📄", "Scissors✂️"])

if user == bot:
    print("You selected: ", user, "and the bot selected: ", bot, "It's a tie!")
elif user == "Rock🪨" and bot == "Paper📄":
    print("You selected: ", user, "and the bot selected: ", bot, "You lose!")
elif user == "Rock🪨" and bot == "Scissors✂️":
    print("You selected: ", user, "and the bot selected: ", bot, "You win!")
elif user == "Paper📄" and bot == "Rock🪨":
    print("You selected: ", user, "and the bot selected: ", bot, "You win!")
elif user == "Paper📄" and bot == "Scissors✂️":
    print("You selected: ", user, "and the bot selected: ", bot, "You lose!")