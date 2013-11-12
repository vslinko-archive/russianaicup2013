from model.ActionType import ActionType

import pathfinder


def go_to(me, world, move, pos):
    path = pathfinder.search_path(world, (me.x, me.y), pos)

    next_pos = path[0]

    move.action = ActionType.MOVE
    move.x = next_pos[0]
    move.y = next_pos[1]


def follow(me, world, move, unit):
    go_to(me, world, move, (unit.x, unit.y))
