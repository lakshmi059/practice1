from prettytable import PrettyTable

class Quiz:
    def __init__(self, initial_questions=None):
        self.questions = initial_questions if initial_questions else []
        self.score = 0

    def display_question(self, question):
        print(question['question'])
        for i, option in enumerate(question['options'], 1):
            print(f"{i}. {option}")

    def take_quiz(self):
        for question in self.questions:
            self.display_question(question)
            user_answer = input("Enter the number of your answer: ")
            if user_answer.isdigit() and 1 <= int(user_answer) <= len(question['options']):
                user_answer_index = int(user_answer) - 1
                if question['options'][user_answer_index] == question['correct_answer']:
                    print("Correct!\n")
                    self.score += 1
                else:
                    print(f"Wrong! The correct answer is: {question['correct_answer']}\n")
            else:
                print("Invalid input. Skipping this question.\n")

    def display_result(self):
        total_questions = len(self.questions)
        correct_answers = self.score

        x = PrettyTable()
        x.field_names = ["Question", "Your Answer", "Correct Answer"]
        
        for question in self.questions:
            x.add_row([question['question'], "-", question['correct_answer']])

        print(x)
        print(f"\nYou got {correct_answers} out of {total_questions} questions correct.")

    def add_question(self):
        question_text = input("Enter the question: ")
        
        options = []
        for i in range(4):
            option = input(f"Enter option {i+1}: ")
            options.append(option)

        correct_answer = input("Enter the correct answer (1-4): ")

        new_question = {
            'question': question_text,
            'options': options,
            'correct_answer': options[int(correct_answer) - 1]
        }

        self.questions.append(new_question)
        print("Question added successfully.")
if __name__ == "__main__":
    initial_questions = [
        {
            'question': 'What is the capital of india',
            'options': ['Beijing', 'delhi', 'Seoul', 'Bangkok'],
            'correct_answer': 'delhi'
        },
        {
            'question': 'prime minister of india',
            'options': ['modi', 'rahul gandhi', 'siddaramaih', 'nirmala sitharaman'],
            'correct_answer': 'modi'
        },
        {
            'question': 'financial minister of india',
            'options': ['modi', 'rahul gandhi', 'siddaramaih', 'nirmala sitharaman'],
            'correct_answer': 'nirmala sitharaman'
        },
        {
            'question': 'chief minister of karnataka',
            'options': ['modi', 'rahul gandhi', 'siddaramaih', 'nirmala sitharaman'],
            'correct_answer': 'siddaramaih'
        },
        {
            'question': 'What is the capital of karnatka',
            'options': ['Beijing', 'delhi', 'Seoul', 'bangalore'],
            'correct_answer': 'bangalore'
        },


# you can have multiple questions added here

]



    quiz = Quiz(initial_questions)

    while True:
        print("\nMenu:")
        print("1. Take Quiz")
        print("2. Add Question")
        print("3. Display Result")
        print("4. Exit")

        choice = input("Enter your choice (1/2/3/4): ")

        if choice == '1':
            quiz.take_quiz()
        elif choice == '2':
            quiz.add_question()
        elif choice == '3':
            quiz.display_result()
        elif choice == '4':
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a valid option.")
