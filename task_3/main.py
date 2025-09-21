from task_3.dijkstra import Graph

if __name__ == "__main__":
    g = Graph()
    g.add_edge('A', 'B', 1)
    g.add_edge('A', 'C', 4)
    g.add_edge('B', 'C', 2)
    g.add_edge('B', 'D', 5)
    g.add_edge('C', 'D', 1)

    start = 'A'
    distances = g.dijkstra(start)
    print(f"Shortest paths from {start}:")
    for vertex, dist in distances.items():
        print(f"{start} -> {vertex}: {dist}")