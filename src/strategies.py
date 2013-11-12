from model.TrooperType import TrooperType

import commands
import filters


def commander(me, world, game, move):
    commands.go_to(me, world, move, (0, 0))


def field_medic(me, world, game, move):
    commander = filters.commander(world)

    if commander:
        commands.follow(me, world, move, commander)


def soldier(me, world, game, move):
    commander = filters.commander(world)

    if commander:
        commands.follow(me, world, move, commander)


def sniper(me, world, game, move):
    commander = filters.commander(world)

    if commander:
        commands.follow(me, world, move, commander)


def scout(me, world, game, move):
    commander = filters.commander(world)

    if commander:
        commands.follow(me, world, move, commander)


strategies_mapping = {
    TrooperType.COMMANDER: commander,
    TrooperType.FIELD_MEDIC: field_medic,
    TrooperType.SOLDIER: soldier,
    TrooperType.SNIPER: sniper,
    TrooperType.SCOUT: scout
}


def select_strategy(me, world, game, move):
    return strategies_mapping[me.type]
