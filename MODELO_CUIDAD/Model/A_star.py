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
    def find_path(road_network, start, goal, agent_type):
        """
        Encuentra el camino optimo desde start hasta goal dentro de un road_network
        """
        if not (0 <= start[0] < road_network.shape[0] and 0 <= start[1] < road_network.shape[1]):
            return []
        
        if not (0 <= goal[0] < road_network.shape[0] and 0 <= goal[1] < road_network.shape[1]):
            return []

        if agent_type not in {'person', 'car'}:
            return []
        
        available_cells = {
            'person': {CellType.SIDEWALK.value, CellType.LANE.value, CellType.INTERSECTION.value, CellType.DESTINITY.value},
            'car': {CellType.LANE.value, CellType.INTERSECTION.value, CellType.DESTINITY.value}
        }[agent_type]

        
        # Nodos visitados
        closed_set = set()
        # Nodos por visitar
        open_set = [(0, start)]

        came_from = {}
        # Costo desde el inicio hasta el nodo actual
        g_score = {start: 0}
        # Direcciones ortogonales (arriba, abajo, izquierda, derecha)
        directions = [(0, -1), (0, 1), (-1, 0), (1, 0)]


        while open_set:
            _, current = heapq.heappop(open_set)

            # Si se llega al destino
            if current == goal:
                return A_star.reconstruct_path(came_from, current)
            
            # Marcar el nodo actual como visitado
            closed_set.add(current)
            
            # Expandir los nodos vecinos
            x, y = current
            for dx, dy in directions:
                # Nueva posición basada en la dirección elegida
                neighbor = (x + dx, y + dy)
                
                if (0 <= neighbor[0] < road_network.shape[0] and
                            0 <= neighbor[1] < road_network.shape[1] and
                            road_network[neighbor[0], neighbor[1]] in available_cells and
                            neighbor not in closed_set):

                        tentative_g_score = g_score[current] + 1

                        if neighbor not in g_score or tentative_g_score < g_score[neighbor]:
                            came_from[neighbor] = current
                            g_score[neighbor] = tentative_g_score
                            heapq.heappush(open_set, (tentative_g_score + A_star.heuristic(neighbor, goal), neighbor))


        # No se encontró camino
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

