#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# https://github.com/lbarrios/practicas-programacion-competitiva/tree/master/adhoc/unosolo
from termcolor import colored
import time
import os
import sys


def hide_cursor():
    sys.stdout.write("\033[?25l")
    sys.stdout.flush()


def clear_screen():
    # print(chr(27) + "[2J")
    _ = os.system("clear")
    # print("\n"*50)


class Board:
    _DEBUG = False
    _DEBUG_SPEED = 1
    pos_cols = list()
    neg_cols = list()
    count = 0
    initial_K = 0

    bad_tokens = 0

    def all_tokens(self):
        tok = list()
        for x in range(len(self.pos_cols)):
            for y in range(len(self.pos_cols[x])):
                if self.pos_cols[x][y]:
                    tok.append((x, y))
        for x in range(len(self.neg_cols)):
            for y in range(len(self.neg_cols[x])):
                if self.neg_cols[x][y]:
                    tok.append((-x - 1, y))
        return tok

    def solved(self):
        return self.bad_tokens == 0
        for col in self.pos_cols:
            if col[0:self.initial_K].count(True) > 0: return False
        for col in self.neg_cols:
            if col[0:self.initial_K].count(True) > 0: return False
        return True

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
        ret = ""

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
                    ret += "O" if self.defined(col, row) else "·"
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
        if y < self.initial_K:
            self.bad_tokens += 1
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
        if y < self.initial_K:
            self.bad_tokens -= 1
        return True

    def canRD(self, x, y):
        return not self.defined(x, y + 1) and not self.defined(x, y + 2)

    def unRD(self, x, y):
        self.define(x, y)
        self.undefine(x, y + 1)
        self.undefine(x, y + 2)

    def RD(self, x, y):
        if self._DEBUG:
            clear_screen()
            print("RD(%s, %s)" % (x, y))
            print(self)
            sys.stdout.flush()
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

    def canRL(self, x, y):
        return not self.defined(x - 1, y) and not self.defined(x - 2, y)

    def unRL(self, x, y):
        self.define(x, y)
        self.undefine(x - 1, y)
        self.undefine(x - 2, y)

    def RL(self, x, y):
        if self._DEBUG:
            clear_screen()
            print("RL(%s, %s)" % (x, y))
            print(self)
            sys.stdout.flush()
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

    def canRR(self, x, y):
        return not self.defined(x + 1, y) and not self.defined(x + 2, y)

    def unRR(self, x, y):
        # assume that is in a valid rr state
        self.define(x, y)
        self.undefine(x + 1, y)
        self.undefine(x + 2, y)

    def RR(self, x, y):
        if self._DEBUG:
            clear_screen()
            print("RR(%s, %s)" % (x, y))
            print(self)
            sys.stdout.flush()
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
# b._DEBUG = True

if b._DEBUG:
    hide_cursor()
    clear_screen()
    clear_screen()
    clear_screen()
    clear_screen()
    clear_screen()

if b._DEBUG and K == 1:
    b.RD(0, 0)
    print(b.count)

if b._DEBUG and K == 2:
    b.define(2, 3)
    b.undefine(2, 3)
    b.RD(0, 0)
    b.RR(0, 2)
    b.RD(0, 1)
    clear_screen()
    print("total: " + str(b.count))
    print(b)
    time.sleep(3)
    print("")

if b._DEBUG and K == 3:
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
    print("total: " + str(b.count))
    print(b)
    time.sleep(3)
    print("")

if b._DEBUG and K == 4:
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
    print("total: " + str(b.count))
    print(b)
    time.sleep(3)
    print("")

best_solution = 24


def solve(b):
    print(b)
    global best_solution

    if b.count > best_solution:
        return None

    if b.solved():
        best_solution = min(best_solution, b.count)
        print(b)
        print(best_solution)

    pending = list(b.all_tokens())
    for tok in pending:
        # print(b)
        # print("RD", tok)
        if b.canRD(tok[0], tok[1]):
            b.RD(tok[0], tok[1])
            solve(b)
            b.unRD(tok[0], tok[1])

    pending = list(b.all_tokens())
    for tok in pending:
        # print(b)
        # print("RR", tok)
        if b.canRR(tok[0], tok[1]):
            b.RR(tok[0], tok[1])
            solve(b)
            b.unRR(tok[0], tok[1])

    pending = list(b.all_tokens())
    for tok in pending:
        # print(b)
        # print("RL", tok)
        if b.canRL(tok[0], tok[1]):
            b.RL(tok[0], tok[1])
            solve(b)
            b.unRL(tok[0], tok[1])


import sys


def solve1(b):
    global best_solution

    if (2*b.bad_tokens) + b.count > best_solution:
        return None

    if b.solved():
        best_solution = min(best_solution, b.count)
        print(best_solution)

    pending = list(b.all_tokens())
    for tok in pending:
        # print(b)
        # print("RD", tok)
        if b.canRD(tok[0], tok[1]):
            b.RD(tok[0], tok[1])
            solve2(b)
            b.unRD(tok[0], tok[1])

    pending = list(b.all_tokens())
    for tok in pending:
        # print(b)
        # print("RR", tok)
        if b.canRR(tok[0], tok[1]):
            b.RR(tok[0], tok[1])
            solve3(b)
            b.unRR(tok[0], tok[1])

    pending = list(b.all_tokens())
    for tok in pending:
        # print(b)
        # print("RL", tok)
        if b.canRL(tok[0], tok[1]):
            b.RL(tok[0], tok[1])
            solve1(b)
            b.unRL(tok[0], tok[1])


def solve2(b):
    global best_solution

    if (2 * b.bad_tokens) + b.count > best_solution:
        return None

    if b.solved():
        best_solution = min(best_solution, b.count)
        print(best_solution)

    pending = list(b.all_tokens())
    for tok in pending:
        # print(b)
        # print("RR", tok)
        if b.canRR(tok[0], tok[1]):
            b.RR(tok[0], tok[1])
            solve3(b)
            b.unRR(tok[0], tok[1])

    pending = list(b.all_tokens())
    for tok in pending:
        # print(b)
        # print("RL", tok)
        if b.canRL(tok[0], tok[1]):
            b.RL(tok[0], tok[1])
            solve1(b)
            b.unRL(tok[0], tok[1])

    pending = list(b.all_tokens())
    for tok in pending:
        # print(b)
        # print("RD", tok)
        if b.canRD(tok[0], tok[1]):
            b.RD(tok[0], tok[1])
            solve2(b)
            b.unRD(tok[0], tok[1])


def solve3(b):
    global best_solution

    if (2 * b.bad_tokens) + b.count > best_solution:
        return None

    if b.solved():
        best_solution = min(best_solution, b.count)
        print(best_solution)

    pending = list(b.all_tokens())
    for tok in pending:
        # print(b)
        # print("RL", tok)
        if b.canRL(tok[0], tok[1]):
            b.RL(tok[0], tok[1])
            solve1(b)
            b.unRL(tok[0], tok[1])

    pending = list(b.all_tokens())
    for tok in pending:
        # print(b)
        # print("RD", tok)
        if b.canRD(tok[0], tok[1]):
            b.RD(tok[0], tok[1])
            solve2(b)
            b.unRD(tok[0], tok[1])

    pending = list(b.all_tokens())
    for tok in pending:
        # print(b)
        # print("RR", tok)
        if b.canRR(tok[0], tok[1]):
            b.RR(tok[0], tok[1])
            solve3(b)
            b.unRR(tok[0], tok[1])


solve1(b)
print(best_solution)
