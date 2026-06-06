import datetime
import time

name = input("Welcome , Enter your name:")
presentHour = datetime.datetime.now().hour

if 5 <= presentHour <= 11:
    print("Good Morning,", name)
elif 11 <= presentHour <= 17:
    print("Good Afternoon,", name)
elif 17 <= presentHour <= 20:
    print("Good Evening,", name)
else:
    print("Good Night,", name)
    
print("Namaste! Welcome to your chatBot")
print("You can ask me basic question Type 'bye' to exit from the Bot")

responses = {
    "hello" : " Hi, welcome. How can I help you?",
    "how are you" : " I am very fine. Thank you",
    "who are you" : " I am smart chatbot",
    "motivate me" : " Keep going. Every bug of your project make you a better developer",
    "happy" : " Great to hear that",
    "what is functions" : "Block of reusable code",
    "what is python" : "Python is a high-level, easy-to-learn programming language used for web development, data analysis, artificial intelligence, automation, and many other applications.\nIt is known for its simple and readable syntax.",
    "Who built the Taj Mahal" : "The Taj Mahal was commissioned by Shah Jahan, the Mughal emperor, in memory of his wife Mumtaz Mahal.\nIt was built between 1632 and 1653 by thousands of artisans and workers.",
    "Who created you" : "I was created by a Python developer.",
    "What can you do" : "I can answer questions, provide information, and help with simple tasks.",
    "What is AI" : "AI, or Artificial Intelligence, is technology that enables machines to perform tasks that normally require human intelligence.",
    "What is a chatbot" : "A chatbot is a software program that can communicate with users through text or voice.",
    "What is the capital of India" : "The capital of India is New Delhi.",
    "What is the largest planet in our solar system" : "The largest planet in our solar system is Jupiter.",
    "Who invented the telephone" : "The telephone is commonly credited to Alexander Graham Bell.",
    "What is water made of" : "Water is made of hydrogen and oxygen (H₂O).",
    "Why is the sky blue" : "The sky appears blue because Earth's atmosphere scatters blue light more than other colors.",
    "What is gravity" : "Gravity is the force that attracts objects toward each other.",
    "Tell me a joke" : "Why did the programmer quit his job? Because he didn't get arrays!",
    "What is your favorite color" : "I don't have personal preferences, but I think all colors are interesting.",
    "bye" : "bye",
}

def getResponseOfBot(userQuestion):
    userQuestion = userQuestion.lower()
    for key in responses.keys():
        if key.lower() in userQuestion:
            return responses[key]
    
    return "I am not able to tell that yet, Mai jald hi yeh sikh lunga."

while True:
    userInput = input("Please ask your question:")
    reply = getResponseOfBot(userInput)
    print("Bot Response:", reply)
    
    if "bye" in userInput.lower():
        print("Goodbye! Have a great day!")
        break