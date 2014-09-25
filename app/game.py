# -*- coding: utf-8 -*-
class Game:

    def __init__(self):
        self._scores = [0, 0]

    def score(self):
        calls = [0, 15, 30, 40, 'game']
        isAThie = (self._scores[0] == self._scores[1])
        if isAThie and self._scores[0] >= 3:
            return ['deuce', 'deuce']
        elif self._scores[0] >= 4 or self._scores[1] >= 4:
            callsUp40 = {1: ['ads', ''], -1: ['', 'ads'],
                         2: ['wins!', 'loses'], -2: ['loses', 'wins!'],
                         3: ['wins!', 'loses'], -3: ['loses', 'wins!'],
                         4: ['wins!', 'loses'], -4: ['loses', 'wins!']}
            return callsUp40[self._scores[0] - self._scores[1]]
        else:
            return [calls[self._scores[0]], calls[self._scores[1]]]

    def scores(self, player):
        iPlayer = player - 1
        self._scores[iPlayer] += 1
        return self
