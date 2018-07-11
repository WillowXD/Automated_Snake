#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# pylint: disable=C0103,C0111
import sys
from snake.game import Game, GameConf, GameMode

sys.tracebacklimit=0
dict_solver = {
    "g": "GreedySolver",
    "h": "HamiltonSolver",
    }

dict_mode = {
    "n": GameMode.NORMAL,
    "b": GameMode.BENCHMARK,
}

conf = GameConf()
conf.solver_name = dict_solver["g"]
conf.mode = dict_mode["b"]
print("Solver: %s    Mode: %s" % (conf.solver_name, conf.mode))

Game(conf).run()