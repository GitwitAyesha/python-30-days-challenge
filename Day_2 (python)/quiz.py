# code should be able to display questions to user 
# code should have question related to different subjects
# code should have answers of the question
# code should be able to take answers from user as input
# code should be able to demonstrate if the user gave correct answer or not
# code should be able to tell points of the user 
quiz_questions = {
    "Science": [
        {
            "question": "What planet is known as the Red Planet?",
            "options": ["Earth", "Mars", "Jupiter", "Venus"],
            "correct": "Mars"
        },
        {
            "question": "What is the chemical symbol for water?",
            "options": ["H2O", "O2", "CO2", "H2O2"],
            "correct": "H2O"
        }
    ],
    "Math": [
        {
            "question": "What is the value of π (pi) approximately?",
            "options": ["2.14", "3.14", "4.14", "5.14"],
            "correct": "3.14"
        },
        {
            "question": "Solve: 12 × 8",
            "options": ["96", "88", "108", "100"],
            "correct": "96"
        }
    ],
    "Geography": [
        {
            "question": "Which is the largest ocean on Earth?",
            "options": ["Atlantic Ocean", "Indian Ocean", "Arctic Ocean", "Pacific Ocean"],
            "correct": "Pacific Ocean"
        },
        {
            "question": "Which country has the most population?",
            "options": ["USA", "China", "India", "Brazil"],
            "correct": "China"
        }
    ],
    "History": [
        {
            "question": "Who was the first President of the United States?",
            "options": ["Thomas Jefferson", "Abraham Lincoln", "George Washington", "John Adams"],
            "correct": "George Washington"
        },
        {
            "question": "In which year did World War II end?",
            "options": ["1940", "1945", "1939", "1950"],
            "correct": "1945"
        }
    ],
    "Technology": [
        {
            "question": "Who is known as the father of computers?",
            "options": ["Alan Turing", "Bill Gates", "Charles Babbage", "Steve Jobs"],
            "correct": "Charles Babbage"
        },
        {
            "question": "What does HTML stand for?",
            "options": ["Hyper Trainer Marking Language", "Hyper Text Markup Language", "Hyperlink Text Marking Language", "Hyper Transfer Markup Language"],
            "correct": "Hyper Text Markup Language"
        }
    ]
}
def quiz_game(quiz_questions):
    score = 0  # Initialize user score

    for subject, questions in quiz_questions.items():
        print(f"\n Subject: {subject}")  # Display subject

        for q in questions:
            print(f"\nQ: {q['question']}")  # Display question

            # Display answer options
            for i, opt in enumerate(q["options"], start=1):
                print(f"  {i}) {opt}")

            # Take user input
            while True:
                user_choice = input("Enter your answer (1-4) or type 'exit' to quit: ").strip().lower()
                
                if user_choice == "exit":
                    print(f"\n Exiting the quiz... Your final score: {score}/{sum(len(q) for q in quiz_questions.values())}")
                    return  # Exit the function

                if user_choice.isdigit():
                    user_choice = int(user_choice)
                    if 1 <= user_choice <= 4:
                        break
                    else:
                        print("⚠ Invalid choice. Please enter a number between 1 and 4.")
                else:
                    print(" Invalid input. Please enter a number between 1 and 4 or type 'exit' to quit.")

            # Check if the answer is correct
            if q["options"][user_choice - 1] == q["correct"]:
                print(" Correct!\n")
                score += 1
            else:
                print(f" Incorrect! The correct answer is: {q['correct']}\n")

    # Display final score
    print(f"\n Quiz completed! Your final score: {score}/{sum(len(q) for q in quiz_questions.values())}")

# Run the quiz game
quiz_game(quiz_questions)