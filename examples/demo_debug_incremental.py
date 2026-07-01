import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from src.grid_search import load_grid, astar_grid, draw_path


def main():
    grid = load_grid("data/mapa_simple.txt")

    print("Mapa cargado:")
    print("\n".join("".join(row) for row in grid))

    print("\nEjecutando A* con debug=True")
    path = astar_grid(grid, debug=True)

    print("\nCamino final:")
    print(path)
    print(draw_path(grid, path))


if __name__ == "__main__":
    main()
