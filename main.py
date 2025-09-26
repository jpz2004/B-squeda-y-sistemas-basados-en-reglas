import sys
import heapq

# base de conocimiento

def cargar_grafo(archivo):
    grafo = {}
    with open(archivo, "r") as f:
        for linea in f:
            origen, destino, costo = linea.strip().split()
            costo = float(costo)
            grafo.setdefault(origen, []).append((destino, costo))
            grafo.setdefault(destino, []).append((origen, costo))  # bidireccional
    return grafo

# Algoritmo A*

def a_star(grafo, inicio, fin, heuristica):
    cola = [(0 + heuristica[inicio], 0, inicio, [inicio])]  
    visitados = set()

    while cola:
        f, g, nodo, camino = heapq.heappop(cola)

        if nodo in visitados:
            continue
        visitados.add(nodo)

        if nodo == fin:
            return camino, g  

        for vecino, costo in grafo.get(nodo, []):
            if vecino not in visitados:
                nuevo_g = g + costo
                nuevo_f = nuevo_g + heuristica[vecino]
                heapq.heappush(cola, (nuevo_f, nuevo_g, vecino, camino + [vecino]))
    return None, float("inf")

# Programa principal

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Uso: python main.py <inicio> <fin>")
        sys.exit(1)

    inicio, fin = sys.argv[1], sys.argv[2]
    grafo = cargar_grafo("kb.txt")

    heuristica = {
        "A": 14,
        "B": 10,
        "C": 6,
        "D": 4,
        "E": 0
    }

    camino, costo = a_star(grafo, inicio, fin, heuristica)

    if camino:
        print("Ruta encontrada:", " -> ".join(camino))
        print("Costo total:", costo, "minutos")
    else:
        print("No se encontró ruta.")
