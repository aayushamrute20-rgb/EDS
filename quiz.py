#question-answer quiz
questions = ("What is the capital of France?",
              "What is the largest planet?", 
              "What is the chemical symbol for water?", 
              "What is the largest mammal?",
              "What is the capital of Japan?")
options = (("A. Paris", "B. London", "C. Rome", "D. Berlin"),
           ("A. Earth", "B. Jupiter", "C. Saturn", "D. Mars"),
           ("A. H2O", "B. CO2", "C. O2", "D. NaCl"),
           ("A. Elephant", "B. Blue Whale", "C. Giraffe", "D. Hippopotamus"),
           ("A. Tokyo", "B. Kyoto", "C. Osaka", "D. Hiroshima"))
answers = ("A", "B", "A", "B", "A")
score = 0
for question, option, answer in zip(questions, options, answers):
    print(question)
    for opt in option:
        print(opt)
    user_answer = input("Enter your answer (A/B/C/D): ").upper()
    if user_answer == answer:
        print("Correct!")
        score += 1
    else:
        print(f"Wrong! The correct answer is {answer}.")
print(f"Your final score is: {(score/len(questions))*100:.2f}%")
