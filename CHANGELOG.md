# CHANGELOG - Proyecto Trivia con FastAPI, PostgreSQL y Docker

El presente archivo documenta los cambios diarios, avances y mejoras realizados en el desarrollo del juego de trivia. Cada sección representa un día de trabajo y se relaciona con su respectiva rama y commit en Git.

---

## Día 1 - Configuración inicial del entorno y estructura básica

- Configuración del proyecto: Se creó una carpeta de proyecto llamada trivia-game-python y dentro de ella se configuró un entorno virtual con venv, donde se instalaron las librerías necesarias.

![entorno](./img/Pasted%20image%2020250415212834.png)

- Docker y Docker Compose: Se creó el archivo docker-compose.yml que levanta los servicios juego, api y db.

*juego*: Este servicio corre el juego en la consola. Se conecta con la API para pedir preguntas y mandar las respuestas del jugador, espera a que la base de datos y la API estén funcionando antes de arrancar.

*api*: Este servicio se encarga de recibir y responder las peticiones del juego, se conecta con la base de datos para leer las preguntas, está disponible en el puerto 8000.

![api](./img/Pasted%20image%2020250415211032.png)

*db*: Este servicio es la base de datos del juego, aquí se guardan todas las preguntas que se usan, carga un archivo llamado init.sql que crea la tabla y mete las preguntas automáticamente.

![db](./img/Pasted%20image%2020250415211447.png)

- Rama día 01 y primer commit:

![commit día 1](./img/Captura%20de%20pantalla%202025-04-11%20181413.png)

---

## Día 2 - Implementación de lógica base del juego

- Se creó trivia.py con la clase Question.

![trivia base](./img/Pasted%20image%2020250415213509.png)

- Se implementaron pruebas unitarias con pytest para is_correct().

![pruebas 1](./img/Pasted%20image%2020250415213102.png)

- Rama día 02

![rama día 2](./img/Pasted%20image%2020250415213235.png)

---

## Día 3 - Desarrollo de la clase Quiz

- Se creó la clase Quiz para manejar flujo de preguntas y respuestas.

![quiz](./img/Captura%20de%20pantalla%202025-04-11%20193230.png)

- Rama día 03

![rama día 3](./img/Captura%20de%20pantalla%202025-04-11%20195300.png)

---

## Día 4 - Manejo de rondas

- Se definió la lógica para las 10 rondas y la terminación del juego.

![rondas](./img/Pasted%20image%2020250415214540.png)

- Rama día 04

![rama día 4](./img/Pasted%20image%2020250415214325.png)

---

## Día 5 - Mejoras en la interfaz de usuario

- Se agregaron endpoints en main.py para recuperar preguntas y enviar respuestas.

![endpoints](./img/Pasted%20image%2020250415215239.png)

- Rama día 05

![rama día 5](./img/Pasted%20image%2020250415215026.png)

---

## Día 6 - Pipeline CI/CD

- Se configuró una acción de GitHub que se ejecuta al hacer push en las ramas develop o main.

![pipeline 1](./img/Pasted%20image%2020250415215638.png)
![pipeline 2](./img/Pasted%20image%2020250415215902.png)

- Rama día 06

![rama día 6](./img/Pasted%20image%2020250415220208.png)

---

## Día 7 - Gestión de configuración, seguridad y pruebas de rendimiento

- Se configuran variables de entorno

![env](./img/Pasted%20image%2020250415220525.png)

- Pruebas de carga en locustfile.py

![locust](./img/Pasted%20image%2020250415221630.png)

- Rama día 07

![rama día 7](./img/Pasted%20image%2020250415220626.png)

---

## Trivia - Consola y prueba de ejecución

![juego consola 1](./img/Pasted%20image%2020250415221211.png)
![juego consola 2](./img/Pasted%20image%2020250415221312.png)
![juego consola 3](./img/Pasted%20image%2020250415221350.png)
![juego consola 4](./img/Pasted%20image%2020250415221437.png)