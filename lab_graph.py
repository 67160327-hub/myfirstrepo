import matplotlib.pyplot as plt
import networkx as nx
from collections import deque
import time

class graph_structure:
    def __init__(self):
        self.graph = {}

    def add_edge(self, node, neighbor):
        if node not in self.graph:
            self.graph[node] = []
        if neighbor not in self.graph:
            self.graph[neighbor] = []
        self.graph[node].append(neighbor)
        self.graph[neighbor].append(node)

    def show_graph(self):
        print("\n--- Graph Structure ---")
        for node, neighbors in self.graph.items():
            print(f"{node} -> {neighbors}")

    def plot_graph(self, highlight_nodes=None, title="Graph Structure"):
        G = nx.Graph()
        for node, neighbors in self.graph.items():
            for neighbor in neighbors:
                G.add_edge(node, neighbor)

        pos = nx.spring_layout(G, seed=42)

        node_colors = []
        for n in G.nodes:
            if highlight_nodes and n in highlight_nodes:
                node_colors.append('lightcoral')  # สีของ node ที่ถูกเยี่ยมชม
            else:
                node_colors.append('skyblue')

        plt.figure(figsize=(6, 4))
        nx.draw(
            G, pos,
            with_labels=True,
            node_color=node_colors,
            node_size=1200,
            font_size=12,
            font_weight='bold',
            edge_color='gray'
        )
        plt.title(title)
        plt.show()

    def bfs(self, start):
        print("\n--- Breadth-First Search ---")
        visited = []
        queue = deque([start])

        while queue:
            node = queue.popleft()
            if node not in visited:
                visited.append(node)
                print("Visited:", node)
                self.plot_graph(highlight_nodes=visited, title=f"BFS Visiting: {node}")
                time.sleep(0.5)
                for neighbor in self.graph[node]:
                    if neighbor not in visited:
                        queue.append(neighbor)

        print("BFS Order:", visited)
        return visited

    def dfs(self, start):
        print("\n--- Depth-First Search ---")
        visited = []
        stack = [start]

        while stack:
            node = stack.pop()
            if node not in visited:
                visited.append(node)
                print("Visited:", node)
                self.plot_graph(highlight_nodes=visited, title=f"DFS Visiting: {node}")
                time.sleep(0.5)
                for neighbor in reversed(self.graph[node]):
                    if neighbor not in visited:
                        stack.append(neighbor)

        print("DFS Order:", visited)
        return visited


# ---------- เริ่มโปรแกรมหลัก ----------
if __name__ == '__main__':
    g = graph_structure()
    g.add_edge('A', 'B')
    g.add_edge('A', 'C')
    g.add_edge('B', 'D')
    g.add_edge('C', 'E')
    g.add_edge('D', 'F')

    g.show_graph()
    g.plot_graph(title="Initial Graph")

    g.bfs('A')
    g.dfs('A')
