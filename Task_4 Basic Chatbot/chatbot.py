# CodeAlpha Internship
# Task 4: Basic Chatbot

def chatbot_response(user_input):
    """
    Generate a response based on the user's message.
    """

    user_input = user_input.lower().strip()

    if user_input in ["hello", "hi", "hey"]:
        return "Hi! How can I help you?"

    elif user_input in ["how are you", "how are you?"]:
        return "I'm fine, thanks! How are you?"

    elif user_input in ["what is your name", "what is your name?"]:
        return "My name is CodeAlpha Bot."

    elif user_input in ["who are you", "who are you?"]:
        return "I am a simple rule-based Python chatbot."

    elif user_input in ["thank you", "thanks"]:
        return "You're welcome!"

    elif user_input in ["bye", "goodbye", "exit", "quit"]:
        return "Goodbye! Have a great day!"

    else:
        return "Sorry, I don't understand that. Please try another message."


def main():
    print("=" * 45)
    print("        Welcome to CodeAlpha Chatbot")
    print("=" * 45)

    print("\nYou can say:")
    print("- hello")
    print("- how are you")
    print("- what is your name")
    print("- who are you")
    print("- thank you")
    print("- bye")

    while True:
        user_input = input("\nYou: ")

        response = chatbot_response(user_input)

        print("Bot:", response)

        # End the conversation
        if user_input.lower().strip() in [
            "bye",
            "goodbye",
            "exit",
            "quit"
        ]:
            break


# Start the chatbot
if __name__ == "__main__":
    main()