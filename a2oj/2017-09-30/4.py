#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# http://codeforces.com/problemset/problem/59/A

import string

word = input()

lowercase_count = len([x for x in word if x in string.ascii_lowercase])
uppercase_count = len([x for x in word if x in string.ascii_uppercase])

if lowercase_count>=uppercase_count:
    print(word.lower())
else:
    print(word.upper())
