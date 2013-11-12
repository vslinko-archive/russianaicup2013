import copy

from astar import astar


def search_path(world, start, end):
    cells = copy.deepcopy(world.cells)

    for trooper in world.troopers:
        cells[trooper.x][trooper.y] = 9

    def neighbors(pos):
        for dx, dy in ((-1, 0), (0, -1), (0, 1), (1, 0)):
            x = pos[0] + dx
            y = pos[1] + dy
            if 0 <= x < world.width and 0 <= y < world.height:
                if cells[x][y] == 0:
                    yield (x, y)

    def goal(pos):
        return pos[0] == end[0] and pos[1] == end[1]

    def cost(posA, posB):
        return 1

    def heuristic(pos):
        dy = abs(end[0] - pos[0])
        dx = abs(end[1] - pos[1])
        return dy + dx

    return astar(start, neighbors, goal, 0, cost, heuristic)
