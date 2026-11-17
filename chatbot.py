import random
from datetime import datetime

print("Welcome to Basic Chatbot!")

name = input("What is your name? ")

print("Hello", name, "!")

chat_history=[]

while True:
    user = input("You: ").lower()
    if user != "chat history":
        chat_history.append("You: " + user)

    if user == "hello":
        replies = ["Hi!", "Hello!", "Hey! How are you?", "Nice to meet you!"]
        print("Bot:", random.choice(replies))

    elif user == "how are you":
        print("Bot: I am fine! Thank you.")

    elif user == "welcome":
        print("Bot: Thank you!")

    elif user == "what is your name":
        print("Bot: I am your chatbot!")

    elif user=="what is my name":
        print("Bot: Your name is",name)

    elif user == "thanks":
        print("Bot: You're welcome!")

    elif user == "joke":
        jokes = [ "What do you call a bear with no teeth? A gummy bear!",
        "Why did the math book look sad? It had too many problems!",
        "What do you call a sleeping dinosaur? A dino-snore!"
        "Why was the computer cold? It left its Windows open!"]
        print("Bot:", random.choice(jokes))

    elif user == "time":
        now = datetime.now()
        print("Bot: The current time is", now.strftime("%I:%M %p"))

    elif user == "date":
        now = datetime.now()
        print("Bot: Today's date is", now.strftime("%d-%m-%Y"))

    elif user == "help":
        print("Bot: Here are the things you can ask me:")
        print("1. how are you")
        print("2. what is your name")
        print("3. what is my name")
        print("4. joke")
        print("5. time")
        print("6. date")
        print("7. motivate")
        print("8. calculate")
        print("9. compliment")
        print("10. quiz")
        print("11. count words")
        print("12. reverse")
        print("13. riddle")
        print("14. would you rather")
        print("15. chat history")
        print("16. restart")

    elif user == "motivate":
        messages = ["Believe in yourself!",
        "Never give up!",
        "Small steps lead to big achievements!",
        "Every day is a new opportunity!",
        "Keep learning and keep growing!"]
        print("Bot:", random.choice(messages))

    elif user == "calculate":
        num1 = float(input("Enter first number: "))
        operator = input("Enter operator (+, -, *, /): ")
        num2 = float(input("Enter second number: "))

        if operator == "+":
            print("Bot: ", num1 + num2)
        elif operator == "-":
            print("Bot: ", num1 - num2)
        elif operator == "*":
            print("Bot: ", num1 * num2)
        elif operator == "/":
            if num2 != 0:
                print("Bot: ", num1 / num2)
            else:
                print("Bot: Cannot divide by zero!")
        else:
            print("Bot: Invalid operator!")

    elif user == "compliment":
        compliments = ["You are amazing!",
        "You have great potential!",
        "You are doing a wonderful job!",
        "Keep believing in yourself!",
        "Your hard work will pay off!"]
        print("Bot:", random.choice(compliments))

    elif user == "quiz":
        score = 0

        answer = input("Bot: What is the capital of India? ").lower()
        if answer == "new delhi":
            print("Bot: Correct!")
            score += 1
        else:
            print("Bot: Wrong! The answer is New Delhi.")

        answer = input("Bot: How many days are there in a week? ")
        if answer == "7":
            print("Bot: Correct!")
            score += 1
        else:
            print("Bot: Wrong! The answer is 7.")

        answer = input("Bot: What is the largest planet in our solar system? ").lower()
        if answer == "jupiter":
            print("Bot: Correct!")
            score += 1
        else:
            print("Bot: Wrong! The answer is Jupiter.")

        print("Bot: Your score is", score, "/ 3")

    elif user == "count words":
        sentence = input("Bot: Enter a sentence: ")
        words = sentence.split()
        print("Bot: Number of words =", len(words))

    elif user == "reverse":
        text = input("Bot: Enter a word or sentence: ")
        reversed_text = text[::-1]
        print("Bot: Reversed text:", reversed_text)

    elif user == "riddle":
        riddles = {
            "What has hands but cannot clap?": "clock",
            "What has keys but cannot open locks?": "piano",
            "What gets wetter as it dries?": "towel",
            "What has one eye but cannot see?": "needle"
        }

        question = random.choice(list(riddles.keys()))
        print("Bot:", question)

        answer = input("You: ").lower().strip()

        if answer == riddles[question]:
            print("Bot: Correct! Well done!")
        else:
            print("Bot: The correct answer is", riddles[question])

    elif user == "would you rather":
        choices = [
            ("Fly like a bird", "Become invisible"),
            ("Travel to the past", "Travel to the future"),
            ("Live near the beach", "Live near the mountains"),
            ("Have super strength", "Have super speed")
        ]

        choice = random.choice(choices)

        print("Bot: Would you rather:")
        print("1.", choice[0])
        print("2.", choice[1])

        answer = input("Choose 1 or 2: ")

        if answer == "1":
            print("Bot: Interesting choice!")
        elif answer == "2":
            print("Bot: Great choice!")
        else:
            print("Bot: Please choose 1 or 2.")

    elif user == "chat history":
        print("Bot: Previous messages:")
        for message in chat_history:
            print(message)

    elif user == "restart":
        print("Bot: Restarting conversation...")
        chat_history.clear()
        name = input("Bot: What is your name? ")
        print("Bot: Welcome back", name)

    elif user == "bye":
        print("Bot: Goodbye! Have a nice day!")
        break

    else:
        print("Bot: Sorry, I don't understand.")