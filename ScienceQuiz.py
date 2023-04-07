import time
import pyttsx3
engine = pyttsx3.init()
engine.setProperty('rate',180)
engine.say(' Welcome to the Science Quiz')
print('Scince Quiz')

import random
questions = [
    
    ["What is the symbol of Gold?", "Hg", "Au", "Cl", "Br", '2'],
    ["What is the molecular formula for glucose?", "C6H12O6", "CH4", "H2O", "CO2", '1'],
    ["What is the chemical formula for sulfuric acid?", "H2SO4", "NaCl", "CO2", "CH3COOH", '1'],
    ["What is the pH value of a neutral solution?", "1", "7", "14", "0", '2'],
    ["What is the process of conversion of a solid into a gas directly called?", "Evaporation", "Condensation", "Sublimation", "Freezing", "3"],
    ["Which gas is most abundant in the Earth's atmosphere?", "Oxygen", "Carbon dioxide", "Nitrogen", "Hydrogen", "3"],
    ["What is the process of removing impurities from a liquid by heating and cooling called?", "Decantation", "Distillation", "Filtration", "Crystallization", "2"],
    ["What is the chemical formula for table salt?", "NaCl", "H2O", "CO2", "C6H12O6", "1"],
    ["Which element has the symbol Fe?", "Fluorine", "Iron", "Fermium", "Francium", "2"],
    ["What is the formula for calculating pressure?", "P = mv", "P = mc^2", "P = m/v", "P = F/A", "4"],
    ["What is the balanced chemical equation for photosynthesis?", "6CO2 + 6H2O → C6H12O6 + 6O2", "CH4 + O2 → CO2 + H2O", "2H2O2 → 2H2O + O2", "NaCl + H2O → NaOH + HCl", "1"],
    ["Which gas is known as laughing gas?", "Oxygen", "Carbon dioxide", "Nitrogen", "Nitrous oxide", "4"],
    ["What is the process of a substance changing from a gas to a liquid called?", "Evaporation", "Condensation", "Sublimation", "Freezing", "2"],
    
    ["What is the chemical formula for ammonia?", "NH3", "NaCl", "H2O", "CH3COOH", "1"],
    ["What is the SI unit of electric current?", "Volt", "Ampere", "Ohm", "Watt", "2"],
    ["What is the formula for calculating speed?", "S = mv", "S = mc^2", "S = m/v", "S = d/t", "4"],
    ["What is the formula for calculating work?", "W = mv", "W = mc^2", "W = m/v", "W = Fd", "4"],
]

random.shuffle(questions)  #Choose Question Randomly
asked_questions = []  # Keep track of asked questions
score = 0 #initilize the score
for i in range(10):  # Loop for 10 questions
    print('\nQuestion: ' + str(i+1))

     # Get a random question that hasn't been asked before
    
    available_questions = [q for q in questions if q not in asked_questions]
    random_question = random.choice(available_questions)

    # Extract the question, options, and answer from the selected question

    question = random_question[0]
    options = random_question[1:5]
    answer = random_question[5]

    # Print the selected question and option
    engine.say(question)
    engine.runAndWait()
    print(question)
    engine.say(" Options are")
    engine.runAndWait()
    time.sleep(0.2)
    
    print('options:  ' + ' ,' .join(options) )
    time.sleep(0.2)

     # Get user's answer
    user_answer = input("Enter your Answer(1-4): ")
    if user_answer == answer:
        engine.say(" Bingo , You are correct")
        engine.runAndWait()
        print('Your Answer is Correct'  )
        score = score + 1
    else:
        engine.say(" Sorry , You are Wrong ")
        engine.runAndWait()
        print("Your Answer is Incorrect" )


# Print final score
engine.say("Your final score is " + str(score))
engine.runAndWait()
print("\nYour final score:  " + str(score) + '/10')

Refrence = '\nTHANK YOU' + "DEVELOPED BY UTTAM"     
print(Refrence.center(40))