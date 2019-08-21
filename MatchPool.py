import numpy as np
from Meta import *
from Player import *

class MatchPool(object):
    def __init__(self, meta, players):
        self.meta = meta
        self.players = players
        self.n_players = len(self.players)
        self.half_pool = np.floor(self.n_players / 2)
        self.total_match = 0

    def matchOneRound(self):
        np.shuffle(self.players)
        for (p1, p2) in zip(self.players[:half_pool], self.players[-half_pool:]):
            p1_winrate = self.meta.get_winrate(p1.strategy, p2.strategy)
            if np.random.random() < p1_winrate:
                # p1 wins
                p1.record_match(p2, 1, self.total_match)
                p2.record_match(p1, 0, self.total_match)
            else:
                # p2 wins
                p1.record_match(p2, 0, self.total_match)
                p2.record_match(p1, 1, self.total_match)
            self.total_match += 1
        