 
# Function to get response from the chatbot 
def get_response(user_query): 
    # Define some basic responses 
    responses = { 
        "hi": "Hello! How can I assist you today?", 
        "how are you": "I'm just a chatbot, but thanks for asking! How can I help you?", 
        "bye": "Goodbye! Have a great day!", 
        "screen": "The screen warranty is only 6 months.", 
        "battery": "The battery warranty is 1 year.", 
        "camera": "The camera warranty is 6 months.", 
        "ram": "The RAM warranty is 1 year.", 
        "sim": "The SIM card warranty is not provided." 
    } 
 
    # Check if user query exists in responses 
    if user_query in responses: 
        return responses[user_query] 
    else: 
        # Check if the user query contains specific keywords 
        if "screen" in user_query: 
            return "The screen warranty is only 6 months." 
        elif "battery" in user_query: 
            return "The battery warranty is 1 year." 
        elif "camera" in user_query: 
            return "The camera warranty is 6 months." 
        elif "ram" in user_query: 
            return "The RAM warranty is 1 year." 
        elif "sim" in user_query: 
            return "The SIM card warranty is not provided." 
        else: 
            return "Sorry, I didn't understand your query. Could you please rephrase?" 
 
# Main function 
def main(): 
    print("Welcome to Customer Care Chatbot") 
    print("You can start chatting. Type 'bye' to exit.") 
 
    while True: 
        user_query = input("User: ") 
 
        if user_query == "bye": 
            print("Chatbot: Goodbye! Have a great day!") 
            break 
 
        response = get_response(user_query) 
        print("Chatbot:", response) 
 
# Run the main function 
if __name__ == "__main__": 
    main() 