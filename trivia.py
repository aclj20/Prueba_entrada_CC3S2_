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
        self.correct_answers = 0
        self.incorrect_answers = 0

    def add_question(self, question):
        self.questions.append(question)

    def get_next_question(self):
        if self.current_question_index < len(self.questions):
            question = self.questions[self.current_question_index]
            self.current_question_index += 1
            return question
        return None

    def answer_question(self, question, answer):
        if question.is_correct(answer):
            self.correct_answers += 1
            return True
        else:
            self.incorrect_answers += 1
            return False
    
def run_quiz():
    quiz = Quiz()

    #10 Preguntas
    quiz.add_question(Question("¿Número de Departamentos del Perú?", ["24", "25", "26", "27"], "25"))
    quiz.add_question(Question("¿Capital del Perú?", ["Lima", "Cusco", "Arequipa", "Trujillo"], "Lima"))
    quiz.add_question(Question("¿Río más largo del mundo?", ["Nilo", "Amazonas", "Yangtsé", "Misisipi"], "Amazonas"))
    quiz.add_question(Question("¿Elemento químico del oro?", ["Au", "Ag", "Fe", "Pb"], "Au"))
    quiz.add_question(Question("¿Año de la independencia del Perú?", ["1820", "1821", "1822", "1824"], "1821"))
    quiz.add_question(Question("¿Quién pintó la Mona Lisa?", ["Van Gogh", "Da Vinci", "Picasso", "Dalí"], "Da Vinci"))
    quiz.add_question(Question("¿Número de regiones naturales del Perú?", ["2", "3", "4", "5"], "3"))
    quiz.add_question(Question("¿Planeta más grande del sistema solar?", ["Tierra", "Júpiter", "Saturno", "Urano"], "Júpiter"))
    quiz.add_question(Question("¿Animal más rápido del mundo?", ["Guepardo", "Águila", "León", "Tiburón"], "Guepardo"))
    quiz.add_question(Question("¿Fundador del Imperio Inca?", ["Atahualpa", "Pachacútec", "Manco Cápac", "Huáscar"], "Manco Cápac"))

    total_questions = len(question)

    #Recorremos todas las preguntas
    for _ in range(total_questions):
        question = quiz.get_next_question()
        #Si no hay más preguntas, salimos del bucle
        if question is None:
            print("¡Fin!")
            break
        
        #Si hay más preguntamos, mostramos la descripción
        print(f"\n{question.description}")
        #Mostramos las opciones
        for idx, option in enumerate(question.options):
            print(f"{idx + 1}. {option}")

        answer = input("Tu respuesta: ")

        #Guardamos la opción elegida
        selected_option = question.options[int(answer) - 1]

        #Verficamos si la respuesta es correcta o no
        if question.is_correct(selected_option):
            correct_answers += 1
        else:
            print(f"Incorrecto. La respuesta correcta es: {question.correct_answer}")

    print(f"\nTu puntaje final es {correct_answers}/{total_questions}.")