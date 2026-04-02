# Simple Rule-Based Chatbot
#Author: Ashwin Panbude

def chatboat():
    print("Bot: Hi! I,m a sinmple chatbot. Type 'Exixt' to end the chat.\n")
   
    while True:
        user_input = input ("You: ").lower()

        if user_input == "exit":
            print("Bot: Goodbye! how can I help you today?")
            break
        elif "hello" in user_input or "hi" in user_input:
            print("Bot: Hello! How can I assist you today?")

        elif "how are you" in user_input:
            print("Bot: I'm just a program, but I,m doing great! Thanks for asking.")
        
        elif "your name" in user_input:
            print("Bot: I can help you with basic question like greetings, name, or general queries.")
        
        elif "bye" in user_input:
            print("Bot: Bye! See you soon 👋")
            break
        else:
            print("Bot: Sorry, I didn't Understand that. can you  try something else?")