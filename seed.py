from database import SessionLocal, engine, Base
from models import Question

Base.metadata.create_all(bind=engine)

db = SessionLocal()

questions = [
    # Nivel fácil
    Question(description="¿Qué dispositivo enruta paquetes entre redes?", options=["Switch", "Router", "Hub", "Bridge"], correct_answer="Router", nivel="facil"),
    Question(description="¿Qué significa IP?", options=["Internet Protocol", "Internal Path", "Input Protocol", "Internet Packet"], correct_answer="Internet Protocol", nivel="facil"),
    Question(description="¿Qué hace un switch?", options=["Conecta dispositivos", "Filtra virus", "Enruta paquetes", "Otorga IPs"], correct_answer="Conecta dispositivos", nivel="facil"),
    Question(description="¿Cuál es el puerto estándar para HTTP?", options=["80", "22", "443", "25"], correct_answer="80", nivel="facil"),
    Question(description="¿Qué es DNS?", options=["Traductor de nombres", "Firewall", "Protocolo de correo", "Antivirus"], correct_answer="Traductor de nombres", nivel="facil"),
    Question(description="¿Qué tecnología permite conectarse sin cables?", options=["Ethernet", "WiFi", "USB", "Bluetooth"], correct_answer="WiFi", nivel="facil"),
    Question(description="¿Qué capa del modelo OSI maneja paquetes?", options=["Red", "Aplicación", "Física", "Transporte"], correct_answer="Red", nivel="facil"),
    Question(description="¿Qué es una dirección MAC?", options=["Identificador de red física", "Dominio", "Protocolo", "Mascara de subred"], correct_answer="Identificador de red física", nivel="facil"),
    Question(description="¿Qué protocolo usa HTTPS?", options=["TLS", "FTP", "SSH", "SMTP"], correct_answer="TLS", nivel="facil"),
    Question(description="¿Cuál es el propósito de un router?", options=["Conectar redes distintas", "Repetir señal WiFi", "Filtrar spam", "Almacenar datos"], correct_answer="Conectar redes distintas", nivel="facil"),

    # Nivel intermedio
    Question(description="¿Qué es un firewall?", options=["Sistema de defensa", "Virus", "Router", "Antivirus"], correct_answer="Sistema de defensa", nivel="intermedio"),
    Question(description="¿Qué es un ransomware?", options=["Malware que cifra archivos", "Antivirus", "VPN", "Firewall"], correct_answer="Malware que cifra archivos", nivel="intermedio"),
    Question(description="¿Qué es phishing?", options=["Engaño para obtener datos", "Virus", "Cifrado", "Backup"], correct_answer="Engaño para obtener datos", nivel="intermedio"),
    Question(description="¿Qué significa VPN?", options=["Virtual Private Network", "Verified Protocol Network", "Visible Private Network", "Virtual Public Network"], correct_answer="Virtual Private Network", nivel="intermedio"),
    Question(description="¿Qué hace un antivirus?", options=["Detecta y elimina malware", "Almacena datos", "Filtra red", "Configura IPs"], correct_answer="Detecta y elimina malware", nivel="intermedio"),
    Question(description="¿Qué es un exploit?", options=["Código que aprovecha una vulnerabilidad", "Malware", "VPN", "Backup"], correct_answer="Código que aprovecha una vulnerabilidad", nivel="intermedio"),
    Question(description="¿Qué es un ataque DDoS?", options=["Saturar servidores con peticiones", "Enviar spam", "Cifrar datos", "Escanear puertos"], correct_answer="Saturar servidores con peticiones", nivel="intermedio"),
    Question(description="¿Qué es un honeypot?", options=["Sistema señuelo para atraer atacantes", "Antivirus", "Router", "Malware"], correct_answer="Sistema señuelo para atraer atacantes", nivel="intermedio"),
    Question(description="¿Qué puerto suele usarse para SSH?", options=["22", "80", "443", "25"], correct_answer="22", nivel="intermedio"),
    Question(description="¿Qué protocolo cifra la conexión en HTTPS?", options=["TLS", "FTP", "SMTP", "TCP"], correct_answer="TLS", nivel="intermedio"),

    # Nivel difícil
    Question(description="¿Qué es un qubit?", options=["Unidad cuántica", "Unidad clásica", "Puerta lógica", "Bit óptico"], correct_answer="Unidad cuántica", nivel="dificil"),
    Question(description="¿Qué permite la superposición cuántica?", options=["Estar en varios estados a la vez", "Duplicar información", "Aumentar frecuencia", "Aislar qubits"], correct_answer="Estar en varios estados a la vez", nivel="dificil"),
    Question(description="¿Qué es el entrelazamiento cuántico?", options=["Conexión entre qubits", "División de bits", "Reducción de energía", "Error de medición"], correct_answer="Conexión entre qubits", nivel="dificil"),
    Question(description="¿Qué es una puerta cuántica?", options=["Transformación de estados cuánticos", "Memoria", "Transistor", "Filtro óptico"], correct_answer="Transformación de estados cuánticos", nivel="dificil"),
    Question(description="¿Qué es decoherencia cuántica?", options=["Pérdida de propiedades cuánticas", "Encriptación", "Aceleración térmica", "Estabilidad"], correct_answer="Pérdida de propiedades cuánticas", nivel="dificil"),
    Question(description="¿Qué algoritmo cuántico factoriza grandes números?", options=["Shor", "RSA", "Dijkstra", "Grover"], correct_answer="Shor", nivel="dificil"),
    Question(description="¿Qué algoritmo cuántico acelera búsquedas no ordenadas?", options=["Grover", "AES", "SHA", "Bubble"], correct_answer="Grover", nivel="dificil"),
    Question(description="¿Qué lenguaje se usa para computación cuántica?", options=["Qiskit", "Python", "Bash", "Go"], correct_answer="Qiskit", nivel="dificil"),
    Question(description="¿Qué empresa desarrolló un computador cuántico funcional?", options=["IBM", "AMD", "Oracle", "Cisco"], correct_answer="IBM", nivel="dificil"),
    Question(description="¿Qué fenómeno cuántico permite múltiples caminos posibles?", options=["Interferencia", "Entrelazamiento", "Refracción", "Difracción"], correct_answer="Interferencia", nivel="dificil"),
]

db.add_all(questions)
db.commit()
db.close()
print("✅ Preguntas insertadas correctamente.")
