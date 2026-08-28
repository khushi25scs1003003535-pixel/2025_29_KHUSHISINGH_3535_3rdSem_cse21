#you are required to make personal chatbot assistent.
print("Hope you are doing well, Thankyou for meeting me.")
print("welcome to rule based Internshipwala carrer  chatbot")
print("you can ask me basic question, type 'bye'to exit the program")


responses = {
    "hello" : "hello, How can i help you?",
    " how are you? " : "I am vey fine . thank you",
    "who are you?" : "I am a smart ai chatbot",
    "motivate me ": "keep going, every expert is always a beginner,when he is starting. ",
    "happy":"great to hear that",
    "What is internship ?": "An internship is a way to learn and gain practical work experience before starting a full carrer ",

}


def getResponseBot(userquestion):
    userquestion = userquestion.lower()
    for eachkey in responses :
        if eachkey in userquestion:
             return responses[eachkey]
    return "I am not able to tell that yet I am also on learning phase, sorry is ia ruled based data management chatbox. In future you can ask when this is integrated by advance AI intelligence."
while True :
    userinput = input("please ask your question")
    reply = getResponseBot(userinput)
    print("bot response", reply)
    if "bye" in userinput.lower():
        break
    