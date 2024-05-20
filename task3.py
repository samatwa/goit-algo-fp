import heapq

def dijkstra(graph, start):
    # Ініціалізуємо відстані для всіх вершин
    distances = {vertex: float('infinity') for vertex in graph}
    distances[start] = 0
    
    # Ініціалізуємо бінарну купу та додаємо початкову вершину
    pq = [(0, start)]
    
    while pq:
        # Вибираємо вершину з найменшою відстанню
        current_distance, current_vertex = heapq.heappop(pq)
        
        # Якщо ми знайшли коротший шлях, оновлюємо відстань
        if current_distance > distances[current_vertex]:
            continue
        
        # Оновлюємо відстані до сусідніх вершин
        for neighbor, weight in graph[current_vertex].items():
            distance = current_distance + weight
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(pq, (distance, neighbor))
    
    return distances

# Приклад використання
graph = {
    'A': {'B': 1, 'C': 4},
    'B': {'A': 1, 'C': 2, 'D': 5},
    'C': {'A': 4, 'B': 2, 'D': 1},
    'D': {'B': 5, 'C': 1}
}
start_vertex = 'A'
shortest_distances = dijkstra(graph, start_vertex)
print("Shortest distances:", shortest_distances)