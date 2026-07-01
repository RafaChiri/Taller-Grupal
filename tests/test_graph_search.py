from src.graph_search import bfs, dfs


def test_bfs_finds_short_path():
    graph = {
        "A": ["B", "C"],
        "B": ["D"],
        "C": ["G"],
        "D": ["G"],
        "G": [],
    }

    path = bfs(graph, "A", "G")
    assert path == ["A", "C", "G"]


def test_dfs_finds_a_path():
    graph = {
        "A": ["B", "C"],
        "B": ["D"],
        "C": ["G"],
        "D": ["G"],
        "G": [],
    }

    path = dfs(graph, "A", "G")
    assert path[0] == "A"
    assert path[-1] == "G"
