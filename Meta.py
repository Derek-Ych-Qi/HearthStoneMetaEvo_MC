import numpy as np

class Meta(object):
    def __init__(self, n_strategy):
        self.n_strategy = n_strategy
        self._init_winrate()

    def _init_winrate(self):
        winrate = np.eye(self.n_strategy) * 0.5
        for ri in range(N_CLASS):
            for ci in range(ri):
                winrate[ri, ci] = np.random.random()

        for ri in range(self.n_strategy):
            for ci in range(ri + 1, N_CLASS):
                winrate[ri, ci] = 1 - winrate[ci, ri]
        
        self.winrate = winrate

    def get_winrate(stgy_atk, stgy_def):
        assert stgy_atk < self.n_strategy and stgy_def < self.n_strategy, "Strategy out of bound %d, attacking: %d, defending: %d" % (self.n_strategy, self.stgy_atk, self.stgy_def)
        return self.winrate[stgy_atk][stgy_def]



