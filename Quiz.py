import random


class Quiz:
    def __init__(self):
        self.questions = [
            {"question": "Is Python an interpreted language?", "answer": "Yes"},
            {"question": "Is 7 a prime number?", "answer": "Yes"},
            {"question": "Is the Earth flat?", "answer": "No"},
            {"question": "Is water made of two atoms?", "answer": "No"},
            {"question": "Is 'banana' a fruit?", "answer": "Yes"}
        ]
        random.shuffle(self.questions)
        self.score = 0

    def start_quiz(self):
        print("Welcome to the Python Quiz Game!\n")
        input("Press Enter to start the quiz...")

        for i, question in enumerate(self.questions, 1):
            print(f"\nQuestion {i}: {question['question']}")
            user_answer = input("Enter 'Yes' or 'No': ").strip().capitalize()
            if user_answer == question['answer']:
                self.score += 1

        print(f"\nQuiz complete! Your final score is: {self.score}/{len(self.questions)}")


if __name__ == "__main__":
    quiz = Quiz()
    quiz.start_quiz()
