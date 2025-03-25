#Create a Python program that simulates a simple chatbot. 
# The chatbot will respond to user inputs with pre-defined answers, mimicking a basic conversation.
responses = {
    "hi": "Hi there! How can I assist you today?",
    "hello": "Hi there! How can I assist you today?",
    "how are you": "I'm just a program, but I'm functioning as expected! How about you?",
    "bye": "Goodbye! Have a great day!",
    "default": "I'm sorry, I don't understand that. Can you rephrase?"
}
def get_responce(user_input):
    for key in responses:
        if key in user_input.lower():
            return responses[key]
    return responses["default"]
    
print("Welcome to the Chatbot! Type 'bye' to Exit")
while True:
    user_input =input("YOU : ")
    if "bye" in user_input.lower():
        print("Chatbot : "+responses["bye"])
        break
    chat=get_responce(user_input)
    print("Chatbot : "+chat)