# main.py
import sys
import heapq

# ===============================
# Cargar la base de conocimiento
# ===============================
def cargar_grafo(archivo):
    grafo = {}
    try:
        with open(archivo, "r") as f:
            for i, linea in enumerate(f, 1):
                try:
                    partes = linea.strip().split()
                    if len(partes) != 3:
                         print(f"Advertencia: Formato incorrecto en línea {i}. Se esperaban 3 valores. Ignorando.")
                         continue
                    origen, destino, costo_str = partes
                    costo = float(costo_str)
                    
                    if costo < 0:
                        print(f"Advertencia: Costo negativo ({costo}) en línea {i}. Ignorando arista.")
                        continue

                    grafo.setdefault(origen, []).append((destino, costo))
                    grafo.setdefault(destino, []).append((origen, costo))  # Grafo bidireccional
                except ValueError:
                    print(f"Error de valor al convertir costo en línea {i}. Asegúrese de que el costo es numérico.")
                    continue
    except FileNotFoundError:
        print(f"Error: El archivo '{archivo}' no fue encontrado.")
        sys.exit(1)
    return grafo

# ===============================
# Algoritmo A* (búsqueda heurística)
# ===============================
def a_star(grafo, inicio, fin, heuristica):
    # (f=g+h, g, contador_desempate, nodo, camino)
    contador = 0 
    cola = [(heuristica.get(inicio, 0), 0, contador, inicio, [inicio])] 
    visitados = set()

    while cola:
        f, g, _, nodo, camino = heapq.heappop(cola) # Descartamos el contador

        if nodo in visitados:
            continue
        visitados.add(nodo)

        if nodo == fin:
            return camino, g  # Ruta encontrada y costo total

        for vecino, costo in grafo.get(nodo, []):
            if vecino not in visitados:
                nuevo_g = g + costo
                nuevo_f = nuevo_g + heuristica.get(vecino, 0) # Usa get para evitar KeyError
                contador += 1
                heapq.heappush(cola, (nuevo_f, nuevo_g, contador, vecino, camino + [vecino]))

    return None, float("inf")

# ===============================
# Programa principal
# ===============================
if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Uso: python main.py <inicio> <fin>")
        sys.exit(1)

    inicio, fin = sys.argv[1], sys.argv[2]
    grafo = cargar_grafo("kb.txt")

    # Heurística estimada (simulada)
    # Se recomienda que h(nodo_final) = 0
    heuristica = {
        "A": 14, "B": 10, "C": 6, "D": 4, "E": 0
    }
    
    # Validaciones de Nodos
    if inicio not in grafo:
        print(f"Error: El nodo de inicio '{inicio}' no existe en el grafo.")
        sys.exit(1)
    if fin not in grafo:
        print(f"Error: El nodo de destino '{fin}' no existe en el grafo.")
        sys.exit(1)

    print(f"Buscando ruta de {inicio} a {fin}...")
    camino, costo = a_star(grafo, inicio, fin, heuristica)

    if camino:
        print("\n--- Resultado ---")
        print("Ruta encontrada:", " -> ".join(camino))
        print("Costo total:", costo, "minutos")
    else:
        print("\n--- Resultado ---")
        print("No se encontró ruta entre", inicio, "y", fin)
