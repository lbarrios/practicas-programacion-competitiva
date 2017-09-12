#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# http://www.spoj.com/problems/TAP2016F/

string = ""


def ponerDR():
    global string, DD, DR, RR, RD
    dr = DR.pop()
    string += dr


def ponerDD():
    global string, DD, DR, RR, RD
    dd = DD.pop()
    string += dd
    while len(RD) > 0:
        ponerRD()
    ponerRR()


def ponerRD():
    global string, DD, DR, RR, RD
    if len(RD) > 0:
        rd = RD.pop()
        string += rd


def ponerRR():
    global string, DD, DR, RR, RD
    if len(RR) > 0:
        rr = RR.pop()
        string += rr


def resolver(F):
    global string, DD, DR, RR, RD
    string = ""
    DD, DR, RR, RD = [], [], [], []

    for f in range(F):
        name = "".join([x for x in input() if x == 'R' or x == 'D'])
        if len(name) > 0:
            reverseName = name[::-1]
            firstD, firstR = name.find("D"), name.find("R")
            reverseFirstD, reverseFirstR = reverseName.find("D"), reverseName.find("R")
            lastD = len(name) - reverseFirstD - 1 if firstD >= 0 else firstD
            lastR = len(name) - reverseFirstR - 1 if firstR >= 0 else firstR
            if firstD >= 0 or firstR >= 0:
                if firstD >= 0:
                    if firstR >= 0:
                        if firstD < firstR:
                            if lastD > lastR:
                                DD.append(name)
                            else:
                                DR.append(name)
                        else:
                            if lastD > lastR:
                                RD.append(name)
                            else:
                                RR.append(name)
                    else:
                        DD.append(name)
                else:
                    RR.append(name)

    while len(DR) > 0:
        ponerDR()

    while len(DD) > 0:
        ponerDD()

    while len(RD) > 0:
        ponerRD()

    while len(RR) > 0:
        ponerRR()

    print(string.count("DR"))


while True:
    try:
        F = int(input())
        resolver(F)
    except EOFError:
        break
