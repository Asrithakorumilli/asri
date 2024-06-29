import re

def chatbot_response(user_input):
    # Define rules and responses
    rules = {
        r'hello|hi|hey': "Hello! How can I assist you?",
        r'how are you': "I'm just a chatbot, but thanks for asking!",
        r'what is your name': "I'm just a chatbot. You can call me ChatGPT.",
        r'bye|goodbye': "Goodbye! Have a great day!",
        r'(.*)': "I'm sorry, I didn't understand that."
    }
    
    # Check user input against rules
    for pattern, response in rules.items():
        if re.search(pattern, user_input, re.IGNORECASE):
            return response

# Main function to run the chatbot
def main():
    print("Welcome to the chatbot! Type 'bye' to exit.")
    while True:
        user_input = input("You: ")
        if user_input.lower() == 'bye':
            print(chatbot_response(user_input))
            break
        print("Chatbot:", chatbot_response(user_input))

if __name__ == "__main__":
    main()
