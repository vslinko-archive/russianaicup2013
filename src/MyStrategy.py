from model.Trooper import Trooper
from model.World import World
from model.Game import Game
from model.Move import Move

import strategies


class MyStrategy:
    def move(self, me: Trooper, world: World, game: Game, move: Move):
        strategy = strategies.select_strategy(me, world, game, move)
        strategy(me, world, game, move)
