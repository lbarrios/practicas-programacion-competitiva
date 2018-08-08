#!/usr/bin/env python3
# -*- coding: utf-8 -*-

n, m, q = map(int, input().split())
wus = list(map(int, input().split()))


class Tree:
    def __init__(self):
        self._0 = None
        self._1 = None
        self.count = 0
        self.data = 0

    def add_node(self, s, pos):
        if self.count == 0:
            self._0 = Tree()
            self._1 = Tree()
        self.count += 1

        if pos == len(s):
            self.data += 1
        else:
            if s[pos] == "0":
                self._0.add_node(s, pos + 1)
            else:
                self._1.add_node(s, pos + 1)

    def query(self, s, pos, k, acum):
        if self.count == 0:
            return 0
        if acum > k:
            return 0
        if pos == len(s):
            return self.data
        if s[pos] == "0":
            #print(self._0.query(s, pos + 1, k, acum + wus[pos]), self._1.query(s, pos + 1, k, acum))
            return self._0.query(s, pos + 1, k, acum + wus[pos]) + self._1.query(s, pos + 1, k, acum)
        else:
            #print(self._0.query(s, pos + 1, k, acum), self._1.query(s, pos + 1, k, acum + wus[pos]))
            return self._0.query(s, pos + 1, k, acum) + self._1.query(s, pos + 1, k, acum + wus[pos])

    def print(self):
        print(self.count)


for i in range(m):
    S.add_node(input(), 0)

for i in range(q):
    s, k = input().split();
    k = int(k)
    print(S.query(s, 0, k, 0))
