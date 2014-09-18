# -*- coding: utf-8 -*-
class Match:

    def __init__(self, player1, player2, pacted_sets):
        self.p1 = player1
        self.p2 = player2
        self.won = [0, 0]
        self.sets = pacted_sets
        self.set = ""
        self.c = 0
        self.d = [0, 0]
        self.s1 = [0, 0, 0, 0, 0]
        self.s2 = [0, 0, 0, 0, 0]

    def score(self):
        return "{0} plays with {1} | 0-0".format(self.p1, self.p2)

    def won_set(self, w, s, s1, s2):
        self.set = s
        if(self.c < self.sets):
            if(self.p1 == w):
                self.won[0] = self.won[0] + 1
                self.s1[self.c] = s1
                self.s2[self.c] = s2
                self.d[0] = int(s1) - int(s2)
            if(self.p2 == w):
                self.won[1] = self.won[1] + 1
                self.s1[self.c] = s2
                self.s2[self.c] = s1
                self.d[1] = int(s2) - int(s1)
            self.c += 1
        else:
            self.resultados(self)

    def resultados(self):
        if(self.won[1] < self.won[0]):
            return "{0} defeated {1} | {2}".format(self.p1, self.p2, self.imprimir(self.p1))
        elif(self.won[0] < self.won[1]):
            return "{0} defeated {1} | {2}".format(self.p2, self.p1, self.imprimir(self.p2))

    def imprimir(self, w):
        sal = ""
        x = 0
        for x in range(self.c):
            if(w == self.p1):
                sal += str(self.s1[x]) + "-" + str(self.s2[x])
            else:
                sal += str(self.s2[x]) + "-" + str(self.s1[x])
            if(x < self.c - 1):
                sal += ", "
        return sal
