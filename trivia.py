class Question:
    def __init__(self, description, options, correct_answer):
        self.description = description
        self.options = options
        self.correct_answer = correct_answer

    def is_correct(self, answer):
        return self.correct_answer == answer

class Quiz:
    def __init__(self):
        self.questions = []
        self.current_question_index = 0

    def add_question(self, question):
        self.questions.append(question)

    def get_next_question(self):
        if self.current_question_index < len(self.questions):
            question = self.questions[self.current_question_index]
            self.current_question_index += 1
            return question
        return None
    
def run_quiz():
    quiz = Quiz()

    quiz.add_question(Question("¿Número de Departamentos del Perú?", ["24", "25", "26", "27"], "25"))

    while True:
        question = quiz.get_next_question()
        if question is None:
            print("¡Fin!")
            break

        print(f"\n{question.description}")
        for idx, option in enumerate(question.options):
            print(f"{idx + 1}. {option}")

        answer = input("Tu respuesta: ")
        selected_option = question.options[int(answer) - 1]

        if question.is_correct(selected_option):
            print("¡Correcto!")
        else:
            print(f"Incorrecto. La respuesta correcta es: {question.correct_answer}")
