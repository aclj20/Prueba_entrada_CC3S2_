CREATE TABLE IF NOT EXISTS questions (
    id SERIAL PRIMARY KEY,
    description TEXT NOT NULL,
    options TEXT NOT NULL,
    correct_answer TEXT NOT NULL,
    nivel VARCHAR(20) NOT NULL
);

-- Nivel fácil
INSERT INTO questions (description, options, correct_answer, nivel) VALUES
('¿Qué es una IP?', '["Internet Protocol", "Input Path", "Internal Port", "Internet Package"]', 'Internet Protocol', 'facil'),
('¿Qué hace un switch?', '["Conecta dispositivos", "Filtra virus", "Enruta paquetes", "Otorga IPs"]', 'Conecta dispositivos', 'facil'),
('¿Qué significa DNS?', '["Domain Name System", "Data Network Server", "Digital Name Source", "Device Naming Service"]', 'Domain Name System', 'facil'),
('¿Qué capa del modelo OSI se encarga del direccionamiento lógico?', '["Red", "Física", "Aplicación", "Transporte"]', 'Red', 'facil'),
('¿Qué dispositivo conecta diferentes redes?', '["Router", "Switch", "Hub", "Firewall"]', 'Router', 'facil'),
('¿Qué protocolo utiliza el puerto 80?', '["HTTP", "FTP", "SSH", "SMTP"]', 'HTTP', 'facil'),
('¿Qué tecnología permite redes inalámbricas?', '["WiFi", "Ethernet", "USB", "Bluetooth"]', 'WiFi', 'facil'),
('¿Qué es una dirección MAC?', '["Identificador de red", "Protocolo", "Nombre de dominio", "Código de acceso"]', 'Identificador de red', 'facil'),
('¿Qué protocolo cifra HTTPS?', '["TLS", "TCP", "UDP", "IP"]', 'TLS', 'facil'),
('¿Qué hace un hub?', '["Reenvía datos a todos los puertos", "Filtra paquetes", "Conecta redes", "Gestiona tráfico"]', 'Reenvía datos a todos los puertos', 'facil');

-- Nivel intermedio
INSERT INTO questions (description, options, correct_answer, nivel) VALUES
('¿Qué es un firewall?', '["Antivirus", "Sistema de defensa", "Router", "Exploit"]', 'Sistema de defensa', 'intermedio'),
('¿Qué es un ransomware?', '["Malware que cifra archivos", "Firewall", "Phishing", "Spyware"]', 'Malware que cifra archivos', 'intermedio'),
('¿Qué hace un antivirus?', '["Detecta malware", "Cifra archivos", "Cambia IP", "Conecta redes"]', 'Detecta malware', 'intermedio'),
('¿Qué es phishing?', '["Engaño para obtener datos", "Virus de red", "Cambio de DNS", "Corte de red"]', 'Engaño para obtener datos', 'intermedio'),
('¿Qué es una VPN?', '["Virtual Private Network", "Verificación Pública Nacional", "Red abierta", "Conexión sin cifrado"]', 'Virtual Private Network', 'intermedio'),
('¿Qué hace un exploit?', '["Aprovecha vulnerabilidades", "Elimina virus", "Filtra spam", "Crea backups"]', 'Aprovecha vulnerabilidades', 'intermedio'),
('¿Qué es un ataque DDoS?', '["Saturación de servidores", "Escaneo de puertos", "Inyección SQL", "Suplantación de identidad"]', 'Saturación de servidores', 'intermedio'),
('¿Qué es un honeypot?', '["Sistema señuelo", "Servidor oculto", "Antivirus", "VPN gratuita"]', 'Sistema señuelo', 'intermedio'),
('¿Qué puerto usa SSH?', '["22", "80", "443", "53"]', '22', 'intermedio'),
('¿Qué protocolo usa HTTPS?', '["TLS", "SMTP", "FTP", "UDP"]', 'TLS', 'intermedio');

-- Nivel difícil
INSERT INTO questions (description, options, correct_answer, nivel) VALUES
('¿Qué es un qubit?', '["Unidad cuántica", "Unidad clásica", "Algoritmo", "Sistema óptico"]', 'Unidad cuántica', 'dificil'),
('¿Qué permite la superposición cuántica?', '["Estar en múltiples estados", "Duplicar datos", "Codificar bits", "Reducir errores"]', 'Estar en múltiples estados', 'dificil'),
('¿Qué es el entrelazamiento cuántico?', '["Conexión entre qubits", "Red de seguridad", "Multiplexado", "Canal óptico"]', 'Conexión entre qubits', 'dificil'),
('¿Qué es una puerta cuántica?', '["Operador sobre qubits", "Filtro binario", "Enlace clásico", "Red paralela"]', 'Operador sobre qubits', 'dificil'),
('¿Qué es la decoherencia?', '["Pérdida de información cuántica", "Corte eléctrico", "Interferencia externa", "Error de red"]', 'Pérdida de información cuántica', 'dificil'),
('¿Qué algoritmo cuántico factoriza números?', '["Shor", "RSA", "AES", "Grover"]', 'Shor', 'dificil'),
('¿Qué algoritmo cuántico busca en listas no ordenadas?', '["Grover", "Bubble", "Merge", "Shor"]', 'Grover', 'dificil'),
('¿Qué lenguaje se usa para computación cuántica?', '["Qiskit", "Java", "Go", "Swift"]', 'Qiskit', 'dificil'),
('¿Qué empresa lidera computación cuántica?', '["IBM", "Intel", "Amazon", "Google"]', 'IBM', 'dificil'),
('¿Qué fenómeno cuántico permite caminos múltiples?', '["Interferencia", "Reflexión", "Refracción", "Torsión"]', 'Interferencia', 'dificil');
