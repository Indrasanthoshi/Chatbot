import random
from datetime import datetime

# Dictionary containing chatbot responses
responses = {
    "greetings": [
        "Hello! How can I help you?",
        "Hi there! Welcome.",
        "Hey! Nice to meet you."
    ],

    "how are you": [
        "I'm doing great!",
        "I'm fine. Thanks for asking.",
        "Everything is running perfectly."
    ],

    "python": [
        "Python is a popular programming language.",
        "Python is used for AI, Web Development, Automation, and Data Science."
    ],

    "java": [
        "Java is an object-oriented programming language.",
        "Java is widely used for Android and Enterprise applications."
    ],

    "c": [
        "C is a powerful procedural programming language.",
        "C is mainly used for system programming."
    ],

    "ai": [
        "AI stands for Artificial Intelligence.",
        "Artificial Intelligence enables machines to learn from data."
    ],

    "creator": [
        "I was created by a Python developer.",
        "I was developed using Python programming."
    ],

    "name": [
        "My name is RuleBot.",
        "I'm RuleBot, a Rule-Based Chatbot."
    ],

    "thanks": [
        "You're welcome!",
        "Happy to help!",
        "Anytime!"
    ]
}

history = []

print("="*55)
print("        RULE-BASED CHATBOT")
print("="*55)
print("Type 'help' to see commands.")
print("Type 'bye' to exit.\n")

while True:

    user = input("You : ").lower().strip()

    history.append(user)

    if user == "bye":
        print("Bot : Goodbye! Have a wonderful day.")
        break

    elif user == "help":

        print("""
I can answer questions about:

1. Hello / Hi
2. How are you
3. Python
4. Java
5. C Language
6. AI
7. My Name
8. Who created you
9. Date
10. Time
11. Thank You
12. Bye
""")

    elif user in ["hi", "hello", "hey"]:
        print("Bot :", random.choice(responses["greetings"]))

    elif "how are you" in user:
        print("Bot :", random.choice(responses["how are you"]))

    elif "python" in user:
        print("Bot :", random.choice(responses["python"]))

    elif "java" in user:
        print("Bot :", random.choice(responses["java"]))

    elif user == "c" or " c " in user or "c language" in user:
        print("Bot :", random.choice(responses["c"]))

    elif "artificial intelligence" in user or "ai" in user:
        print("Bot :", random.choice(responses["ai"]))

    elif "your name" in user:
        print("Bot :", random.choice(responses["name"]))

    elif "who created you" in user:
        print("Bot :", random.choice(responses["creator"]))

    elif "date" in user:
        print("Bot : Today's Date :", datetime.now().strftime("%d-%m-%Y"))

    elif "time" in user:
        print("Bot : Current Time :", datetime.now().strftime("%I:%M:%S %p"))

    elif "thank" in user:
        print("Bot :", random.choice(responses["thanks"]))

    else:
        print("Bot : Sorry! I don't know the answer.")

print("\n========== CHAT HISTORY ==========")

for i, message in enumerate(history, 1):
    print(f"{i}. {message}")

print("\nThank you for using RuleBot!")