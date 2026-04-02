# Simple Rule-Based Chatbot
# Author: Ashwin Panbude

def chatbot():
    print("Bot: Hi! I'm your simple chatbot. Type 'exit' to end the chat.\n")

    while True:
        user_input = input("You: ").lower()

        if user_input == "exit":
            print("Bot: Goodbye! Have a great day 😊")
            break

        elif "hello" in user_input or "hi" in user_input:
            print("Bot: Hello! How can I help you today?")

        elif "how are you" in user_input:
            print("Bot: I'm just a program, but I'm doing great! Thanks for asking.")

        elif "your name" in user_input:
            print("Bot: I'm a simple chatbot created using Python.")

        elif "help" in user_input:
            print("Bot: I can respond to basic questions like greetings, name, or general queries.")

        elif "bye" in user_input:
            print("Bot: Bye! See you soon 👋")
            break

        else:
            print("Bot: Sorry, I didn't understand that. Can you try something else?")


# Run chatbot
if __name__ == "__main__":
    chatbot()