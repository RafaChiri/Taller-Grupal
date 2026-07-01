import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from src.grid_search import load_grid, bfs_grid, dfs_grid, astar_grid, draw_path, path_is_valid


def show_result(name, grid, path):
    print(f"\n=== {name} ===")
    print("Encontró camino:", "Sí" if path else "No")
    print("Longitud del camino:", len(path) if path else 0)
    print("Camino válido:", path_is_valid(grid, path) if path else False)
    if path:
        print(draw_path(grid, path))


def main():
    grid = load_grid("data/mapa_obstaculos.txt")

    bfs_path = bfs_grid(grid)
    dfs_path = dfs_grid(grid)
    astar_path = astar_grid(grid)

    show_result("BFS", grid, bfs_path)
    show_result("DFS", grid, dfs_path)
    show_result("A*", grid, astar_path)

    print("\nTabla comparativa")
    print("Algoritmo | ¿Encontró camino? | Longitud del camino | Observación")
    print(f"BFS       | {'Sí' if bfs_path else 'No'} | {len(bfs_path)} | Suele encontrar el camino más corto en costos iguales")
    print(f"DFS       | {'Sí' if dfs_path else 'No'} | {len(dfs_path)} | Puede encontrar un camino, pero no necesariamente el más corto")
    print(f"A*        | {'Sí' if astar_path else 'No'} | {len(astar_path)} | Usa heurística Manhattan para dirigirse hacia la meta")


if __name__ == "__main__":
    main()
