# Sistema Inteligente de Rutas con A*

Este proyecto implementa un sistema inteligente que, a partir de una base de conocimiento (kb.txt) con reglas lógicas sobre paradas y costos, encuentra la mejor ruta entre dos puntos utilizando el algoritmo A*.

- #### 1. Requisitos

Python 3.7 o superior

Editor de texto o IDE (VSCode, PyCharm, Sublime, etc.)

Consola / terminal (cmd, PowerShell, Terminal macOS/Linux)

No requiere librerías externas: solo módulos estándar de Python (sys, heapq).

- #### 2. Archivos del proyecto

- > main.py → Código principal con el algoritmo A*.

- > kb.txt → Base de conocimiento (lista de conexiones entre nodos con sus costos).

- > README.md / USO.md → Documentación del proyecto.

- #### 3. Formato de la base de conocimiento (kb.txt)

Cada línea define una conexión (arista) entre dos nodos con su costo (tiempo en minutos):

# <ORIGEN> <DESTINO> <COSTO>

Ejemplo:

- A B 4
- A C 2
- B D 5
- C D 1
- D E 3


#### Nombres de nodos: pueden ser letras, números o etiquetas (ej: Est1, ParadaCentral).

#### Costo: número positivo (enteros o decimales).

El grafo es bidireccional (la conexión sirve en ambos sentidos).

- #### 4. Ejecución del programa
Opción 1: Uso con argumentos (modo actual)

En la consola, ubícate en la carpeta del proyecto y ejecuta:

python main.py <inicio> <fin>


Ejemplo:

python main.py A E

Salida esperada:

Buscando ruta de A a E...

--- Resultado ---
Ruta encontrada: A -> C -> D -> E
Costo total: 6.0 minutos


Si olvidas los argumentos, verás:

Uso: python main.py <inicio> <fin>

Opción 2: Modo interactivo (opcional)

Si no quieres pasar argumentos, puedes modificar main.py para que pregunte con input():

if len(sys.argv) == 3:
    inicio, fin = sys.argv[1], sys.argv[2]
else:
    inicio = input("Ingrese la parada inicial: ").strip()
    fin = input("Ingrese la parada meta: ").strip()


Ejemplo de uso:

python main.py
Ingrese la parada inicial: A
Ingrese la parada meta: E

- #### 5. Heurística

El programa incluye un diccionario con valores heurísticos simulados:

heuristica = {"A": 14, "B": 10, "C": 6, "D": 4, "E": 0}


Regla clave: el nodo destino debe tener heurística 0.

Si agregas nodos nuevos, actualiza la heurística manualmente o implementa coordenadas y cálculo automático.

- #### 6. Errores comunes

Archivo no encontrado → Asegúrate de que kb.txt esté en la misma carpeta.

Formato incorrecto → Cada línea debe tener 3 valores (ej: A B 4).

Nodo no existe → Verifica mayúsculas/minúsculas y nombres de nodos.

Costo negativo → Se ignoran aristas con valores negativos.

Mensaje “Uso: python main.py <inicio> <fin>” → Olvidaste pasar los dos argumentos.

- #### 7. Pruebas recomendadas

Ruta existente: python main.py A E → Debe mostrar camino y costo.

Inicio = destino: python main.py A A → Ruta trivial, costo 0.

Nodo inexistente: python main.py Z A → Mensaje de error.

Grafo desconectado: Usa nodos sin conexión → “No se encontró ruta”.

- #### 8. Subir a GitHub
git init
git add main.py kb.txt README.md
git commit -m "Proyecto inicial: sistema de rutas A*"
git branch -M main
git remote add origin https://github.com/TU_USUARIO/sistema_rutas.git
git push -u origin main


Luego, en Settings → Collaborators, agrega al tutor como colaborador.

- #### 9. Conclusión

Este proyecto cumple con:

Representación del conocimiento en forma de grafo (kb.txt).

Uso de estrategias de búsqueda heurística (A*).

Validaciones robustas para nodos y costos.

Documentación clara para ejecución y pruebas.

Ideal para aprendizaje y extensión futura (coordenadas, heurísticas dinámicas, interfaces).
