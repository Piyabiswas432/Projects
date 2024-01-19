import nltk
from nltk.chat.util import Chat, reflections


patterns = [
    (r'hi|hello|hey', ['Hi there!', 'Hello!', 'Hey!']),
    (r'how are you', ['I am good, thank you!', 'I\'m doing well. How about you?']),
    (r'what is your name', ['I am a chatbot']),
    (r'quit|exit', ['Goodbye!', 'See you later.']),
]

chatbot = Chat(patterns, reflections)


print("Chatbot: Hi!")
while True:
    user_input = input("You: ")
    response = chatbot.respond(user_input)
    print("Chatbot:", response)

    if user_input.lower() in ['quit', 'exit']:
        break