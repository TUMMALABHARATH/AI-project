def simple_chatbot(user_input):
    user_input = user_input.lower()  # Convert input to lowercase for easier matching

    if "hello" in user_input:
        return "Hello! How can I help you today?"

    elif "how are you" in user_input:
        return "I'm just a chatbot, but I'm here to assist you!"

    elif "goodbye" in user_input:
        return "Goodbye! Have a great day!"

    elif "help" in user_input:
        return "I'm here to help. What do you need assistance with?"

    else:
        return "I'm sorry, I didn't understand that. Can you please rephrase?"

# Main loop for the chatbot
print("Chatbot: Hello! How can I assist you today? (type 'exit' to end)")

while True:
    user_input = input("You: ")
    
    if user_input.lower() == "exit":
        print("Chatbot: Goodbye!")
        break
    
    response = simple_chatbot(user_input)
    print("Chatbot:", response)
