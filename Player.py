import numpy as np

class Player(object):
    def __init__(self):
        self.id = -2 ** 31
        self.strategy = 0
        self.match_result = []

    def record_match(self, other, win, match_id):
        res = {"match_id": match_id,
            "self_id": self.id,
            "self_strategy": self.strategy,
            "other_id": other.id,
            "other_strategy": other.strategy,
            "result": win}
        self.match_result.append(res)