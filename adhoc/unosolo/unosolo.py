#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# https://github.com/lbarrios/practicas-programacion-competitiva/tree/master/adhoc/unosolo

class board:
    pos_cols = list()
    neg_cols = list()

    def __init__(self, initial_K):
        self.define(0, -initial_K)

    def defined(self, x, y):
        if x < 0:
            x = (-x) - 1
            if x > len(self.neg_cols):
                return False
            else:
                if y > len(self.neg_cols[x]):
                    return False
        else:
            if x > len(self.pos_cols):
                return False
            else:
                if y > len(self.pos_cols[x]):
                    return False
        return True

    def define(self, x, y):
        if x >= 0:
            while (len(self.pos_cols) < x + 1):
                self.pos_cols.append(list())
                print(len(self.pos_cols))
            while (len(self.pos_cols[x]) < y + 1):
                self.pos_cols[x].append(False)
            self.pos_cols[x][y] = True
        else:
            x = (-x) - 1
            while (len(self.neg_cols) < x + 1):
                self.neg_cols.append(list())
            print(x)
            print(len(self.neg_cols))
            while (len(self.neg_cols[x]) < y + 1):
                self.neg_cols[x].append(False)
            self.neg_cols[x][y] = True
        return True

    def undefine(self, x, y):
        # Pre: (x,y) is defined..!!
        if x > 0:
            self.pos_cols[x][y] = False
        else:
            x = (-x) - 1
            self.neg_cols[x][y] = False
        return True

    def RD(self, token_x, token_y):
        if not self.defined(token_x, token_y):
            raise Exception("that token is not defined")
        self.undefine(token_x, token_y)
        self.define(token_x, token_y + 1)
        self.define(token_x, token_y + 2)

    def RL(self, token_x, token_y):
        if not self.defined(token_x, token_y):
            raise Exception("that token is not defined")
        self.undefine(token_x, token_y)
        self.define(token_x - 1, token_y)
        self.define(token_x - 2, token_y)

    def RR(self, token_x, token_y):
        if not self.defined(token_x, token_y):
            raise Exception("that token is not defined")
        self.undefine(token_x, token_y)
        self.define(token_x + 1, token_y)
        self.define(token_x + 2, token_y)


K = int(input())

b = board(K)

print(board)
