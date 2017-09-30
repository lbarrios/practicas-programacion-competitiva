#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# http://codeforces.com/problemset/problem/9/A

a, b = map(int,input().split())
numerator = 6-(max(a,b)-1)
if numerator==6:
    print("1/1")
elif numerator==5:
    print("5/6")
elif numerator==4:
    print("2/3")
elif numerator==3:
    print("1/2")
elif numerator==2:
    print("1/3")
elif numerator==1:
    print("1/6")