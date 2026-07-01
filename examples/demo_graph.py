import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from src.graph_search import bfs, dfs


def main():
    graph = {
        "A": ["B", "C"],
        "B": ["D", "E"],
        "C": ["F"],
        "D": ["G"],
        "E": ["G"],
        "F": ["G"],
        "G": [],
    }

    print("=== Búsqueda en grafo ===")
    print("BFS:", bfs(graph, "A", "G"))
    print("DFS:", dfs(graph, "A", "G"))


if __name__ == "__main__":
    main()
