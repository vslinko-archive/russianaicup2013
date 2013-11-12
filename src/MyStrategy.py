from random import getrandbits
from model.ActionType import ActionType
from model.Direction import Direction
from model.Game import Game
from model.Move import Move
from model.Trooper import Trooper
from model.TrooperStance import TrooperStance
from model.World import World


class MyStrategy:
    def move(self, me: Trooper, world: World, game: Game, move: Move):
        if me.action_points < game.standing_move_cost:
            return

        move.action = ActionType.MOVE

        if getrandbits(1):
            if getrandbits(1):
                move.direction = Direction.NORTH
            else:
                move.direction = Direction.SOUTH
        else:
            if getrandbits(1):
                move.direction = Direction.WEST
            else:
                move.direction = Direction.EAST
