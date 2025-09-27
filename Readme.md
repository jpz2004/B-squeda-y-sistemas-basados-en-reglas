# Integrantes grupo

- Juan Pablo Zapata Jaramillo
- Hernan Ricardo Loaiza Doncel
- Neder Antonio Hernández Reyes

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
-	A = Terminal Norte
-	B = Estación Central
-	C = Universidad
-	D = Plaza Mayor
-	E = Terminal Sur

Conexiones nodo origen, nodo destino, tiempo en minutos:
- A B 4
- A C 2
- B D 5
- C D 8
- C E 10
- D E 3

### Resultados y pruebas
Ejemplo de ejecución en la terminal:

- > python main.py A E
Ruta encontrada: A -> C -> E
Costo total: 12.0 minutos

- > python main.py B C
Ruta encontrada: B -> A -> C
Costo total: 6.0 minutos

- > python main.py <inicio> <fin>

## Concluciones 

El sistema demuestra cómo un conjunto de reglas y técnicas de búsqueda heurística pueden aplicarse para resolver problemas reales de transporte.
El algoritmo A* permite encontrar rutas más eficientes que con métodos de búsqueda ciega.
La implementación puede ampliarse con más nodos, diferentes heurísticas y criterios como costo económico o nivel de tráfico.


