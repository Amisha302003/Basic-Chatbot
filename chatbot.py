import random

def greeting(sentence):
    """Check if the user's input is a greeting."""
    for word in sentence.split():
        if word.lower() in GREETING_INPUTS:
            return random.choice(GREETING_RESPONSES)

GREETING_INPUTS = ("hello", "hi", "greetings", "sup", "what's up", "hey", "yo")
GREETING_RESPONSES = ["hi", "hey", "yo", "nods", "hello", "I'm glad! You're talking to me"]


def response(user_response):
    """Generate a response to the user's input."""
    user_response = user_response.lower()

def chatbot():
    """Create a basic chatbot."""
    print("Hello, I'm a basic chatbot!")
    print("What's your name?")
    name = input()

    print("Nice to meet you, " + name + "!")

    while True:
        print("Here are some things I can talk about:")
        print("1. The How are you?")
        print("2. My favorite programming language")
        print("3. The latest movies")
        print("4. Food")
        print("5. What is python?")
        print("6. Today's Whether")
        print("7. How do you spend your free time?")
        print("8. What’s the funniest joke you’ve ever heard?")

        choice = int(input("Please choose a number (1-8): "))
        if choice == 1:
          print("I'm fine. Thanks for asking. What about you?")
          user_input = input()

          if user_input == 'I am good':
            print("ohh that is good to hear")

          elif user_input =='I am not good':
            print("It's okey, everything will be alright!\n Keep Smiling!")

          else:
            print("sorry, I didn.t understand what are you saying")
          
           
        elif choice == 2:
            print("My favorite programming language is Python!")
        elif choice == 3:
            print("I haven't seen any movies lately.")
        elif choice == 4:
            print("I love all kinds of food!")
        elif choice == 5:
            print("Python is an interpreted, object-oriented, high-level programming language with dynamic semantics.")
        elif choice == 6:
           print("The weather is nice today!")
        elif choice == 7:
           print("I'm just a robot. But I can tell you some activity that you can do whenever you are free or bored.")
           print("1. you can read some books")
           print("2. you can listen music")
           print("3. you can do outdoor activities")
           print("4. you can call your friends")
           print("5. you can do some exercise")
        elif choice == 8:
           print("Yes sure! Here it is.")
           print("Akshay - To a neighbour - I want to marry your daughter.")
           print("Neighbour: How much do you earn?")
           print("Akshay: 30 thousand rupees per month.")
           print("Neighbour: I give pocket money of Rs 20 thousand per month to my daughter")
           print("Akshay: I am also telling this by adding the same.....")

          
        else:
          print("Sorry, I don't understand that choice.")
        print("Do you have any other questions or topics you'd like to talk about?")
        answer = input().lower()
        if 'yes' in answer:
            continue
        elif 'no' in answer:
            print("Okay, it was nice talking to you!")
            print("Goodbye! Have a great day!")
            break
        else:
            print("Sorry, I didn't understand your answer.")
            print("Restarting the Bot")
            chatbot()

if __name__ == '__main__':
    chatbot()