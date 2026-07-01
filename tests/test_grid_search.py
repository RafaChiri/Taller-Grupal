from src.grid_search import bfs_grid, dfs_grid, astar_grid, path_is_valid, find_position, neighbors


def sample_grid():
    return [
        list("S..."),
        list(".##."),
        list("...."),
        list("...G"),
    ]


def test_find_position():
    grid = sample_grid()
    assert find_position(grid, "S") == (0, 0)
    assert find_position(grid, "G") == (3, 3)


def test_neighbors_avoid_obstacles():
    grid = sample_grid()
    result = neighbors(grid, (0, 1))
    assert (1, 1) not in result


def test_bfs_grid_valid_path():
    grid = sample_grid()
    path = bfs_grid(grid)
    assert path_is_valid(grid, path)


def test_dfs_grid_valid_path():
    grid = sample_grid()
    path = dfs_grid(grid)
    assert path_is_valid(grid, path)


def test_astar_grid_valid_path():
    grid = sample_grid()
    path = astar_grid(grid)
    assert path_is_valid(grid, path)
