from model.TrooperType import TrooperType


def first(iterable, default=None):
    if iterable:
        for item in iterable:
            return item
    return default


def commander(world):
    def _filter(trooper):
        return trooper.type == TrooperType.COMMANDER

    return first(filter(_filter, world.troopers))
