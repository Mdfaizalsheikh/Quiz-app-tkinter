import tkinter as tk
from tkinter import messagebox


quiz_data = [
    {
        "question": "What is the capital of France?",
        "options": ["Berlin", "Madrid", "Paris", "Rome"],
        "answer": "Paris"
    },
    {
        "question": "Which planet is known as the Red Planet?",
        "options": ["Earth", "Mars", "Jupiter", "Saturn"],
        "answer": "Mars"
    },
    {
        "question": "What is the largest ocean on Earth?",
        "options": ["Atlantic Ocean", "Indian Ocean", "Arctic Ocean", "Pacific Ocean"],
        "answer": "Pacific Ocean"
    }
]

class QuizApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Quiz Application")
        self.root.geometry("500x300")

        self.question_index = 0
        self.score = 0

        self.question_label = tk.Label(root, text="", font=("Helvetica", 16))
        self.question_label.pack(pady=20)

        self.option_var = tk.StringVar()

        self.options_frame = tk.Frame(root)
        self.options_frame.pack(pady=20)

        self.option_buttons = []
        for _ in range(4):
            button = tk.Radiobutton(
                self.options_frame,
                text="",
                variable=self.option_var,
                font=("Helvetica", 14),
                value=""
            )
            button.pack(anchor="w", pady=5)
            self.option_buttons.append(button)

        self.next_button = tk.Button(root, text="Next", command=self.next_question)
        self.next_button.pack(pady=20)

        self.load_question()

    def load_question(self):
        if self.question_index < len(quiz_data):
            current_question = quiz_data[self.question_index]
            self.question_label.config(text=current_question["question"])
            self.option_var.set("")
            for i, option in enumerate(current_question["options"]):
                self.option_buttons[i].config(text=option, value=option)
        else:
            self.show_score()

    def next_question(self):
        selected_option = self.option_var.get()
        if selected_option:
            current_question = quiz_data[self.question_index]
            if selected_option == current_question["answer"]:
                self.score += 1
            self.question_index += 1
            self.load_question()
        else:
            messagebox.showwarning("Warning", "Please select an option!")

    def show_score(self):
        messagebox.showinfo("Quiz Completed", f"Your score is: {self.score}/{len(quiz_data)}")
        self.root.quit()

if __name__ == "__main__":
    root = tk.Tk()
    app = QuizApp(root)
    root.mainloop()
