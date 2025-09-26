# Introduccion

En este proyecto se desarrolló un sistema inteligente en Python capaz de encontrar la mejor ruta entre dos estaciones del sistema de transporte masivo local. El sistema utiliza una base de conocimiento escrita en reglas lógicas y un algoritmo de búsqueda heurística (A*) para calcular la ruta óptima.

### Objetivo 
Implementar un sistema basado en reglas y técnicas de búsqueda heurística para determinar la mejor ruta entre dos puntos de un sistema de transporte masivo.

### Metodologia
Definición de la base de conocimiento (kb.txt): se crearon reglas que representan las conexiones entre estaciones y sus costos en minutos.
Implementación en Python (main.py): se programó el algoritmo A* que combina el costo real del trayecto y una heurística (estimación en línea recta).
Pruebas del sistema: se ejecutaron diferentes consultas ej. de la estación A a E, de B a C para verificar la efectividad del Sistema.

### Base de conocimiento (kb.txt)

Imaginemos que tu ciudad tiene estas estaciones:
•	A = Terminal Norte
•	B = Estación Central
•	C = Universidad
•	D = Plaza Mayor
•	E = Terminal Sur

Conexiones nodo origen, nodo destino, tiempo en minutos:
A B 5
B C 7
B D 4
C D 3
D E 6
A C 12
C E 10

