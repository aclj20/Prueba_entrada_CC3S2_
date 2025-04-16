# CHANGELOG - Proyecto Trivia con FastAPI, PostgreSQL y Docker

El presente archivo documenta los cambios diarios, avances y mejoras realizados en el desarrollo del juego de trivia. Cada sección representa un día de trabajo y se relaciona con su respectiva rama y commit en Git.

---

## Día 1 -  Configuración inicial del entorno y estructura básica

- Configuración del proyecto: Se creó una carpeta de proyecto llamada `trivia-game-python` y dentro de ella se configuró un entorno virtual con `venv`, donde se instalaron las librerías necesarias

	![[Pasted image 20250415212834.png]]
- Docker y Docker Compose:
	Se creó el archivo docker-compose.yml que levanta los servicios juego, api y db.
	
	juego: Este servicio corre el juego en la consola. Se conecta con la API para pedir preguntas y mandar las respuestas del jugador, espera a que la base de datos y la API estén funcionando antes de arrancar
	
	api: Este servicio se encarga de recibir y responder las peticiones del juego, se conecta con la base de datos para leer las preguntas, está disponible en el puerto 8000.
		![[Pasted image 20250415211032.png]]
		db: Este servicio es la base de datos del juego, aquí se guardan todas las preguntas que se usan, carga un archivo llamado `init.sql` que crea la tabla y mete las preguntas automáticamente.
		![[Pasted image 20250415211447.png]]
- Rama día 01 y primer commit:
	![[Captura de pantalla 2025-04-11 181413.png]]


---

## Día 2 - Implementación de lógica base del juego

- Se creó `trivia.py` con la clase `Question`.
	![[Pasted image 20250415213509.png]]
- Se implementaron pruebas unitarias con `pytest` para `is_correct()`.
	![[Pasted image 20250415213102.png]]
- Rama día 02 
	![[Pasted image 20250415213235.png]]

---

## Día 3 - Desarrollo de la clase Quiz

- Se creó la clase `Quiz` para manejar flujo de preguntas y respuestas.
	![[Captura de pantalla 2025-04-11 193230.png]]
- Rama día 03
	![[Captura de pantalla 2025-04-11 195300.png]]
---

## Día 4 - Manejo de rondas

- Se definió la lógica para las 10 rondas y la terminación del juego.
	![[Pasted image 20250415214540.png]]
- Rama día 04
	![[Pasted image 20250415214325.png]]


---

## Día 5 - Mejoras en la interfaz de usuario

- Se agregaron endpoints en main.py para recuperar preguntas y enviar respuestas.
	![[Pasted image 20250415215239.png]]
- Rama día 05
	![[Pasted image 20250415215026.png]]

---

## Día 6 - Pipeline CI/CD

- Se configuró una acción de GitHub que se ejecuta al hacer push en las ramas `develop` o `main`. 
	![[Pasted image 20250415215638.png]]
	![[Pasted image 20250415215902.png]]
- Rama día 06
	![[Pasted image 20250415220208.png]]

---

## Día 7 - Gestión de configuración, seguridad y pruebas de rendimiento

- Se configuran variables de entorno
	![[Pasted image 20250415220525.png]]
- Pruebas de carga en locustfile.py
	![[Pasted image 20250415221630.png]]
- Rama día 07
	![[Pasted image 20250415220626.png]]

## Trivia 
![[Pasted image 20250415221211.png]]
![[Pasted image 20250415221312.png]]

![[Pasted image 20250415221350.png]]
![[Pasted image 20250415221437.png]]