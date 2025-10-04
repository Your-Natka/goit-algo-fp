from dijkstra import dijkstra

def main():
    # Приклад графа
    graph = {
        'A': {'B': 4, 'C': 2},
        'B': {'A': 4, 'C': 1, 'D': 5},
        'C': {'A': 2, 'B': 1, 'D': 8, 'E': 10},
        'D': {'B': 5, 'C': 8, 'E': 2, 'F': 6},
        'E': {'C': 10, 'D': 2, 'F': 2},
        'F': {'D': 6, 'E': 2}
    }

    start = 'A'
    distances = dijkstra(graph, start)
    print(f"Найкоротші відстані від вершини {start}:")
    for vertex, dist in distances.items():
        print(f"{vertex}: {dist}")

if __name__ == "__main__":
    main()