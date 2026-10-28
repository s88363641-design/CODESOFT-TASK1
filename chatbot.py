
from datetime import datetime

print("===== CODSOFT AI CHATBOT =====")
print("Bot: Hello! I am your AI Chatbot.")
print("Bot: Type 'bye' to exit.")

while True:
    user = input("You: ").lower().strip()

    if user in ["hi", "hello", "hey"]:
        print("Bot: Hello! How can I help you?")

    elif "your name" in user:
        print("Bot: My name is CodSoft AI Bot.")

    elif "how are you" in user:
        print("Bot: I am fine! Thank you.")

    elif "python" in user:
        print("Bot: Python is a programming language.")

    elif "time" in user:
        print("Bot:", datetime.now().strftime("%I:%M %p"))

    elif "date" in user:
        print("Bot:", datetime.now().strftime("%d-%m-%Y"))

    elif "help" in user:
        print("Bot: Ask me about Python, time or date.")

    elif user in ["bye", "exit", "quit"]:
        print("Bot: Goodbye! Have a nice day!")
        break

    else:
        print("Bot: Sorry, I don't understand.")
