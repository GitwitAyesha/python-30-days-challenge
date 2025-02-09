import tkinter as tk
from tkinter import messagebox

quiz_questions = {
    "Science": [
        {"question": "What planet is known as the Red Planet?", "options": ["Earth", "Mars", "Jupiter", "Venus"], "correct": "Mars"},
        {"question": "What is the chemical symbol for water?", "options": ["H2O", "O2", "CO2", "H2O2"], "correct": "H2O"}
    ],
    "Math": [
        {"question": "What is the value of π (pi) approximately?", "options": ["2.14", "3.14", "4.14", "5.14"], "correct": "3.14"},
        {"question": "Solve: 12 × 8", "options": ["96", "88", "108", "100"], "correct": "96"}
    ]
}

class QuizApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Quiz Game")
        self.score = 0
        self.current_subject = list(quiz_questions.keys())[0]
        self.current_question_index = 0
        
        self.question_label = tk.Label(root, text="", font=("Arial", 14), wraplength=400)
        self.question_label.pack(pady=10)
        
        self.option_buttons = []
        for i in range(4):
            btn = tk.Button(root, text="", font=("Arial", 12), width=30, command=lambda i=i: self.check_answer(i))
            btn.pack(pady=5)
            self.option_buttons.append(btn)
        
        self.score_label = tk.Label(root, text=f"Score: {self.score}", font=("Arial", 12))
        self.score_label.pack(pady=10)
        
        self.next_button = tk.Button(root, text="Next", command=self.next_question, font=("Arial", 12))
        self.next_button.pack(pady=5)
        
        self.exit_button = tk.Button(root, text="Exit", command=root.quit, font=("Arial", 12), bg="red", fg="white")
        self.exit_button.pack(pady=5)
        
        self.load_question()
    
    def load_question(self):
        subject_questions = quiz_questions[self.current_subject]
        if self.current_question_index < len(subject_questions):
            q = subject_questions[self.current_question_index]
            self.question_label.config(text=q['question'])
            for i, option in enumerate(q['options']):
                self.option_buttons[i].config(text=option)
        else:
            self.next_subject()
    
    def check_answer(self, index):
        q = quiz_questions[self.current_subject][self.current_question_index]
        if q['options'][index] == q['correct']:
            self.score += 1
            messagebox.showinfo("Correct!", "You got it right!")
        else:
            messagebox.showinfo("Incorrect!", f"The correct answer was: {q['correct']}")
        self.score_label.config(text=f"Score: {self.score}")
        self.current_question_index += 1
        self.load_question()
    
    def next_question(self):
        self.current_question_index += 1
        self.load_question()
    
    def next_subject(self):
        subjects = list(quiz_questions.keys())
        current_index = subjects.index(self.current_subject)
        if current_index + 1 < len(subjects):
            self.current_subject = subjects[current_index + 1]
            self.current_question_index = 0
            self.load_question()
        else:
            messagebox.showinfo("Quiz Finished", f"Your final score: {self.score}")
            self.root.quit()

root = tk.Tk()
app = QuizApp(root)
root.mainloop()
