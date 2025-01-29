import heapq
import numpy as np

from model_types.dtos.CellType import CellType

"""
Referencias: https://www.geeksforgeeks.org/a-search-algorithm-in-python/

Se busca que el agente se mueve en direcciones ortogonales (arriba, abajo, izquierda, derecha)
"""


class A_star:

    @staticmethod
    def heuristic(a, b):
        """
        Calcular la distancia entre dos puntos (Manhattan)
        """
        return abs(a[0] - b[0]) + abs(a[1] - b[1])

    @staticmethod
    def find_path(road_network, start, goal, type='person'):
        """
        Encuentra el camino optimo desde start hasta goal dentro de un road_network
        """

        # Lista de nodos abiertos (pendientes de explorar)
        open_set = []
        # Agregar el nodo inicial con heuristica 0
        heapq.heappush(open_set, (0, start))
        # Guardar el nodo del que proviene (registra cómo se llegó a cada nodo)
        came_from = {}
        # Guardar el costo real desde start hasta cada nodo
        g_score  = {start: 0}
        # Guardar el costo estimado total
        f_score = {start: A_star.heuristic(start, goal)}

        # Direcciones ortogonales (arriba, abajo, izquierda, derecha)
        directions = [(0, -1), (0, 1), (-1, 0), (1, 0)]

        if type == 'person':
            available_cells={CellType.SIDEWALK.value, CellType.LANE.value, CellType.INTERSECTION.value, CellType.DESTINITY.value}
        elif type == 'car':
            available_cells={CellType.LANE.value, CellType.INTERSECTION.value, CellType.DESTINITY.value}

        while open_set:
            _, current = heapq.heappop(open_set)

            # Si se llega al destino
            if current == goal:
                return A_star.reconstruct_path(came_from, current)
            
            # Expandir los nodos vecinos
            x, y = current
            for dx, dy in directions:
                # Nueva posición basada en la dirección elegida
                neighbor = (x + dx, y + dy)
                
                # Verificar si la nueva posición está dentro del 'road_network'
                if 0 <= neighbor[0] < road_network.shape[0] and 0 <= neighbor[1] < road_network.shape[1]:
                    # Solo considerar nodos válidos (por ejemplo, si no es un obstáculo)
                    if road_network[neighbor[0], neighbor[1]] in available_cells:  # 0 podría representar una celda libre
                        tentative_g_score = g_score[current] + 1

                        # Si el camino es más corto
                        if neighbor not in g_score or tentative_g_score < g_score[neighbor]:
                            # Guardar el punto de donde proviene
                            came_from[neighbor] = current
                            # Guardar el costo real
                            g_score[neighbor] = tentative_g_score
                            # Guardar el costo total estimado
                            f_score[neighbor] = tentative_g_score + A_star.heuristic(neighbor, goal)
                            heapq.heappush(open_set, (f_score[neighbor], neighbor))

        print("No se encontró camino")
        return []

    @staticmethod
    def reconstruct_path(came_from, current):
        """
        Reconstruir el camino desde el nodo inicial hasta el nodo final
        """
        total_path = [current]
        while current in came_from:
            current = came_from[current]
            total_path.append(current)
        # Invertir el camino
        return total_path[::-1]


# # Crear una red de nodos como un numpy.array
# road_network = np.array([
#     [2, 2, 2],
#     [4, 1, 2],
#     [4, 5, 5]
# ])

# # Definir el punto de inicio y el punto de destino
# start = (0, 0)
# goal = (2, 2)

# # Llamar al método estático
# path = A_star.find_path(road_network, start, goal, 'person')

# print("Camino encontrado:", path)
