#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# https://github.com/lbarrios/practicas-programacion-competitiva/tree/master/adhoc/unosolo
from termcolor import colored
import time
import os


def clear_screen():
    _ = os.system("clear")
    # print(chr(27) + "[2J")


class Board:
    _DEBUG = False
    _DEBUG_SPEED = 1
    pos_cols = list()
    neg_cols = list()
    count = 0
    initial_K = 0

    def __init__(self, initial_K):
        self.initial_K = initial_K
        self.define(0, 0)

    def __repr__(self):
        return "%s (%r) %s %s" % (self.__class__, self.initial_K, self.pos_cols, self.neg_cols)

    def __str__(self):
        total_cols = len(self.pos_cols) + len(self.neg_cols)
        max_row = 0
        for col in self.pos_cols:
            max_row = max(max_row, len(col))
        for col in self.neg_cols:
            max_row = max(max_row, len(col))
        ret = "Board(%s x %s), k=%s" % (total_cols, max_row, self.initial_K) + "\n"

        # ret += "neg: %r\npos: %r\n" % (self.neg_cols, self.pos_cols)

        row = 0
        while row < max_row:
            col = -len(self.neg_cols)
            while col < total_cols - len(self.neg_cols):
                if col == 0:
                    ret += "|"
                if row < self.initial_K:
                    ret += colored("O" if self.defined(col, row) else "·", "red")
                else:
                    ret += "O" if self.defined(col, row) else "."
                col += 1
            row += 1
            ret += "\n"
            if row == self.initial_K:
                ret += "".join(["-" for i in range(total_cols + 1)]) + "\n"
        return ret

    def defined(self, x, y):
        if x < 0:
            x = (-x) - 1
            if x >= len(self.neg_cols):
                return False
            else:
                if y >= len(self.neg_cols[x]):
                    return False
            return self.neg_cols[x][y]
        else:
            if x >= len(self.pos_cols):
                return False
            else:
                if y >= len(self.pos_cols[x]):
                    return False
            return self.pos_cols[x][y]

    def define(self, x, y):
        if x >= 0:
            while (len(self.pos_cols) < x + 1):
                self.pos_cols.append(list())
            while (len(self.pos_cols[x]) < y + 1):
                self.pos_cols[x].append(False)
            self.pos_cols[x][y] = True
        else:
            x = (-x) - 1
            while (len(self.neg_cols) < x + 1):
                self.neg_cols.append(list())
            while (len(self.neg_cols[x]) < y + 1):
                self.neg_cols[x].append(False)
            self.neg_cols[x][y] = True
        self.count += 1
        return True

    def undefine(self, x, y):
        # Pre: (x,y) is defined..!!
        if x >= 0:
            self.pos_cols[x][y] = False
        else:
            x = (-x) - 1
            self.neg_cols[x][y] = False
        self.count -= 1
        return True

    def RD(self, x, y):
        if self._DEBUG:
            clear_screen()
            print("RD(%s, %s)" % (x, y))
            print(self)
            time.sleep(self._DEBUG_SPEED)
        if not self.defined(x, y):
            raise Exception("that token (%s, %s) is not defined" % (x, y))
        if self.defined(x, y + 1):
            raise Exception("can't do RD(%s,%s) because (%s, %s) is already defined" % (x, y, x, y + 1))
        if self.defined(x, y + 2):
            raise Exception("can't do RD(%s,%s) because (%s, %s) is already defined" % (x, y, x, y + 2))
        self.undefine(x, y)
        self.define(x, y + 1)
        self.define(x, y + 2)

    def RL(self, x, y):
        if self._DEBUG:
            clear_screen()
            print("RL(%s, %s)" % (x, y))
            print(self)
            time.sleep(self._DEBUG_SPEED)
        if not self.defined(x, y):
            raise Exception("that token (%s, %s) is not defined" % (x, y))
        if self.defined(x - 1, y):
            raise Exception("can't do RL(%s,%s) because (%s, %s) is already defined" % (x, y, x - 1, y))
        if self.defined(x - 2, y):
            raise Exception("can't do RL(%s,%s) because (%s, %s) is already defined" % (x, y, x - 2, y))
        self.undefine(x, y)
        self.define(x - 1, y)
        self.define(x - 2, y)

    def RR(self, x, y):
        if self._DEBUG:
            clear_screen()
            print("RR(%s, %s)" % (x, y))
            print(self)
            time.sleep(self._DEBUG_SPEED)
        if not self.defined(x, y):
            raise Exception("that token (%s, %s) is not defined" % (x, y))
        if self.defined(x + 1, y):
            raise Exception("can't do RR(%s,%s) because (%s, %s) is already defined" % (x, y, x + 1, y))
        if self.defined(x + 2, y):
            raise Exception("can't do RR(%s,%s) because (%s, %s) is already defined" % (x, y, x + 2, y))
        self.undefine(x, y)
        self.define(x + 1, y)
        self.define(x + 2, y)


K = int(input())
b = Board(K)
b._DEBUG = True

if b._DEBUG:
    clear_screen()
    clear_screen()
    clear_screen()
    clear_screen()
    clear_screen()

if K == 1:
    b.RD(0, 0)
    print(b.count)

if K == 2:
    b.define(2, 3)
    b.undefine(2, 3)
    b.RD(0, 0)
    b.RR(0, 2)
    b.RD(0, 1)
    clear_screen()
    print(b)
    print("total: " + str(b.count))

if K == 3:
    b.define(3, 5)
    b.define(-2, 5)
    b.undefine(3, 5)
    b.undefine(-2, 5)
    b.RD(0, 0)
    b.RD(0, 2)
    b.RR(0, 3)
    b.RD(0, 1)
    b.RL(0, 3)
    b.RR(0, 4)
    b.RD(0, 2)
    clear_screen()
    print(b)
    print("total: " + str(b.count))

if K == 4:
    b.define(-4, 9)
    b.define(4, 9)
    b.undefine(-4, 9)
    b.undefine(4, 9)
    b.RD(0, 0)
    b.RD(0, 2)
    b.RR(0, 3)
    b.RD(0, 1)
    b.RL(0, 3)
    b.RD(0, 4)
    b.RD(0, 2)
    b.RD(-2, 3)
    b.RD(-1, 3)
    b.RD(1, 3)
    b.RD(2, 3)
    b.RD(0, 6)
    b.RR(0, 7)
    b.RR(0, 8)
    b.RD(0, 5)
    b.RL(0, 6)
    b.RD(0, 4)
    b.RR(0, 6)
    b.RL(0, 7)
    b.RD(0, 5)
    b.RD(0, 3)
    clear_screen()
    print(b)
    print("total: " + str(b.count))
