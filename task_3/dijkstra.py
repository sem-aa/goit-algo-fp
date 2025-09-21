import heapq

class Graph:
    def __init__(self):
        self.adj_list = {}  # dictionary: vertex -> [(neighbor, weight), ...]

    def add_edge(self, u, v, weight):
        # undirected graph
        if u not in self.adj_list:
            self.adj_list[u] = []
        if v not in self.adj_list:
            self.adj_list[v] = []
        self.adj_list[u].append((v, weight))
        self.adj_list[v].append((u, weight))

    def dijkstra(self, start):
        # dictionary to store distances
        distances = {vertex: float('inf') for vertex in self.adj_list}
        distances[start] = 0

        # priority queue (binary heap)
        priority_queue = [(0, start)]  # (distance, vertex)

        while priority_queue:
            current_distance, current_vertex = heapq.heappop(priority_queue)

            # skip if a better path has already been found
            if current_distance > distances[current_vertex]:
                continue

            # iterate through all neighbors
            for neighbor, weight in self.adj_list[current_vertex]:
                distance = current_distance + weight

                # if a shorter path is found
                if distance < distances[neighbor]:
                    distances[neighbor] = distance
                    heapq.heappush(priority_queue, (distance, neighbor))

        return distances