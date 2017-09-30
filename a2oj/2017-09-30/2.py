#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# http://codeforces.com/problemset/problem/236/A

girl="CHAT WITH HER!"
boy="IGNORE HIM!"

nick = set(input())
if len(nick)%2 == 0:
    print(girl)
else:
    print(boy)