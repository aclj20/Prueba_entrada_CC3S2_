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

def cargar_preguntas_por_nivel(nivel):
    preguntas = []

    if nivel == "1":  # Redes
        preguntas.extend([
            Question("¿Qué dispositivo enruta paquetes entre redes?", ["Switch", "Router", "Hub", "Bridge"], "Router"),
            Question("¿Qué significa IP?", ["Internet Protocol", "Internal Path", "Interconnect Port", "Input Protocol"], "Internet Protocol"),
            Question("¿Qué protocolo asigna IP dinámicamente?", ["DNS", "DHCP", "HTTP", "FTP"], "DHCP"),
            Question("¿Qué puerto usa HTTP?", ["80", "443", "21", "25"], "80"),
            Question("¿Qué capa del modelo OSI maneja direcciones MAC?", ["Capa de red", "Capa de enlace de datos", "Capa física", "Capa de sesión"], "Capa de enlace de datos"),
            Question("¿Qué hace un switch?", ["Amplifica señal", "Conecta redes", "Filtra y reenvía frames", "Genera IPs"], "Filtra y reenvía frames"),
            Question("¿Qué protocolo traduce nombres de dominio?", ["FTP", "DHCP", "DNS", "SMTP"], "DNS"),
            Question("¿Qué herramienta se usa para ver rutas de red?", ["Ping", "Traceroute", "SSH", "Telnet"], "Traceroute"),
            Question("¿Cuál es una dirección IP válida?", ["256.0.0.1", "192.168.0.1", "123.456.78.9", "10.10.10.300"], "192.168.0.1"),
            Question("¿Cuál es el estándar WiFi más rápido?", ["802.11b", "802.11g", "802.11n", "802.11ax"], "802.11ax"),
        ])

    elif nivel == "2":  # Ciberseguridad
        preguntas.extend([
            Question("¿Qué es un firewall?", ["Un virus", "Una red privada", "Un sistema de defensa", "Un protocolo"], "Un sistema de defensa"),
            Question("¿Qué es un ransomware?", ["Un antivirus", "Un tipo de ataque que cifra datos", "Un exploit de red", "Un router modificado"], "Un tipo de ataque que cifra datos"),
            Question("¿Qué es una VPN?", ["Una red social", "Un tipo de virus", "Red privada virtual", "Protocolo de acceso"], "Red privada virtual"),
            Question("¿Qué es un ataque de fuerza bruta?", ["Hackeo físico", "Probar muchas contraseñas", "Captura de pantalla", "Infección por USB"], "Probar muchas contraseñas"),
            Question("¿Qué hace un antivirus?", ["Rompe claves", "Protege y detecta malware", "Apaga redes", "Controla el WiFi"], "Protege y detecta malware"),
            Question("¿Qué es el phishing?", ["Correos falsos para robar datos", "Análisis de redes", "Fallo de hardware", "Búsqueda de conexiones"], "Correos falsos para robar datos"),
            Question("¿Qué es la autenticación de dos factores?", ["Una contraseña doble", "Validación por dos medios", "Login sin contraseña", "Conexión segura"], "Validación por dos medios"),
            Question("¿Qué es OWASP?", ["Grupo hacker", "Norma de hardware", "Top de vulnerabilidades web", "Servidor web"], "Top de vulnerabilidades web"),
            Question("¿Qué herramienta analiza puertos abiertos?", ["Photoshop", "Putty", "Nmap", "GIMP"], "Nmap"),
            Question("¿Qué puerto usa HTTPS?", ["21", "22", "443", "80"], "443"),
        ])

    elif nivel == "3":  # Computación Cuántica
        preguntas.extend([
            Question("¿Qué es un qubit?", ["Unidad clásica", "Unidad cuántica", "Transistor", "Circuito lógico"], "Unidad cuántica"),
            Question("¿Qué permite la superposición?", ["Medir bits", "Procesar datos", "Estar en varios estados", "Conectar routers"], "Estar en varios estados"),
            Question("¿Qué es el entrelazamiento cuántico?", ["Una red de nodos", "Dos qubits que se afectan mutuamente", "Qubits en secuencia", "Error de medición"], "Dos qubits que se afectan mutuamente"),
            Question("¿Qué lenguaje se usa para programar computadoras cuánticas?", ["Python", "Q#", "Fortran", "Go"], "Q#"),
            Question("¿Qué compañía desarrolló Sycamore?", ["IBM", "Google", "Microsoft", "Amazon"], "Google"),
            Question("¿Qué problema resuelven bien las computadoras cuánticas?", ["Redes", "Factores primos grandes", "Diseño gráfico", "Compresión de video"], "Factores primos grandes"),
            Question("¿Qué es una puerta cuántica Hadamard?", ["Transforma estados clásicos", "Crea superposición", "Divide fotones", "Reinicia el qubit"], "Crea superposición"),
            Question("¿Qué es la decoherencia?", ["Ruido cuántico", "Amplificación cuántica", "Medición simultánea", "Sincronización de qubits"], "Ruido cuántico"),
            Question("¿Qué es Qiskit?", ["Sistema operativo", "Framework de IBM para computación cuántica", "Lenguaje de Google", "Editor de código"], "Framework de IBM para computación cuántica"),
            Question("¿Cuál es el mayor desafío de los computadores cuánticos?", ["Tamaño", "Costo", "Estabilidad de los qubits", "Compatibilidad con Java"], "Estabilidad de los qubits"),
        ])
    
    return preguntas

def run_quiz():
    print("=== Bienvenido al Quiz de Tecnología ===")
    print("Selecciona el nivel de dificultad:")
    print("1. Redes (Fácil)")
    print("2. Ciberseguridad (Intermedio)")
    print("3. Computación Cuántica (Difícil)")

    while True:
        nivel = input("Ingresa el número del nivel: ").strip()
        if nivel in ["1", "2", "3"]:
            break
        print("Nivel inválido. Intenta otra vez.")

    quiz = Quiz()
    preguntas_nivel = cargar_preguntas_por_nivel(nivel)

    for pregunta in preguntas_nivel:
        quiz.add_question(pregunta)

    total_questions = len(quiz.questions)

    for _ in range(total_questions):
        question = quiz.get_next_question()
        print(f"\n{question.description}")
        for idx, option in enumerate(question.options):
            print(f"{idx + 1}. {option}")

        while True:
            answer = input("Tu respuesta: ").strip()
            if not answer.isdigit():
                print("Entrada inválida. Ingresa un número.")
                continue
            selected_index = int(answer) - 1
            if selected_index < 0 or selected_index >= len(question.options):
                print("Opción fuera de rango. Intenta otra vez.")
                continue
            selected_option = question.options[selected_index]
            break

        if question.is_correct(selected_option):
            print("¡Correcto!")
            quiz.correct_answers += 1
        else:
            print(f"Incorrecto. La respuesta correcta es: {question.correct_answer}")
            quiz.incorrect_answers += 1

    print("\n=== Resultados del Quiz ===")
    print(f"Respuestas correctas: {quiz.correct_answers}")
    print(f"Respuestas incorrectas: {quiz.incorrect_answers}")
    print(f"Puntaje final: {quiz.correct_answers}/{total_questions}")

run_quiz()
