#Let's make an Advance Qiz game, where a player can win up to $1000.
print("Hi there, welcome to our Science Quiz Game")
#Defining the questions, answers and their explanations
quiz = [
  {"question": "1) What is the chemical symbol for gold?",
   "options": ["a. Au", "b. Ag", "c. Cu", "d. Fe"],
   "answer": "a",
   "explanation": "Gold is Au"},
  {"question": "2) What is the density of water?", 
  "options": [ "a. 1.0 g/cm³", "b. 1.1 g/cm³", "c. 1.2 g/cm³", "d. 1.3 g/cm³"],
  "answer": "a",
  "explanation": "The density of water is 1.0 g/cm³}"},
  {"question": "3) Force is measured in what unit?",
   "options": ["a. Newton", "b. Pascal", "c. Joule", "d. Watt"],
   "answer": "a",
   "explanation": "Force is measured in Newtons"},
  {"question": "4) which of these is the exception for metals?",    "options": ["a. Aluminium", "b. Mercury", "c. Lead", "d. Gold"],
   "answer": "b",
   "explanation": "Mercury is liquid in room temperature which is against all other metals"},
  {"question": "5) What is the atomic number of Titanium?",
   "options": ["a. 22", "b. 23", "c. 24", "d. 25"],
   "answer": "c",
   "explanation": "Titanium has an atomic number of 24"},
  {"question": "6) According to electronic theory, Oxidation is known as?",
   "options": ["a. Loss of electrons", "b. Gain of electrons", "c. Loss of protons", "d. Gain of protons"],
   "answer": "a",
   "explanation": "Oxidation is the process of losing electrons"},
]
#Defining the function to run the quiz
def run_quiz(quiz):
  score = 0
  for question in quiz:
    print(question["question"])
    for option in question["options"]:
      print(option)
    answer = input("Enter your answer (a, b, c, or d): ")
    if answer == question["answer"]:
      print()
      print("Correct!")
      score += 1
    else:
      print("Incorrect!")
      print()
      print(question["explanation"])
  print("You scored", score, "out of", len(quiz))
run_quiz(quiz)