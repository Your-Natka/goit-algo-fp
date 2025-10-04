import heapq

def dijkstra(graph, start):
    """
    graph: словник у форматі {вершина: {сусід: вага, ...}, ...}
    start: початкова вершина
    повертає словник з найкоротшими відстанями до всіх вершин
    """
    distances = {vertex: float('inf') for vertex in graph}
    distances[start] = 0

    # Пріоритетна черга (min-heap)
    heap = [(0, start)]

    while heap:
        current_distance, current_vertex = heapq.heappop(heap)

        if current_distance > distances[current_vertex]:
            continue

        for neighbor, weight in graph[current_vertex].items():
            distance = current_distance + weight

            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(heap, (distance, neighbor))

    return distances