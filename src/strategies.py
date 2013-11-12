from model.TrooperType import TrooperType


def commander(me, world, game, move):
    pass


def field_medic(me, world, game, move):
    pass


def soldier(me, world, game, move):
    pass


def sniper(me, world, game, move):
    pass


def scout(me, world, game, move):
    pass


strategies_mapping = {
    TrooperType.COMMANDER: commander,
    TrooperType.FIELD_MEDIC: field_medic,
    TrooperType.SOLDIER: soldier,
    TrooperType.SNIPER: sniper,
    TrooperType.SCOUT: scout
}


def select_strategy(me, world, game, move):
    return strategies_mapping[me.type]
