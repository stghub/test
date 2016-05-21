#! /usr/bin/python

# -*- coding: utf-8 -*-



if __name__ == "__main__":

    import random

    f = open('3E26EEEB.pnach', 'w')

    f.write("comment=ACFF Random Cheats\n\n")


    for _8bl in [
0x0192F550,0x0192F551,0x0192F552,0x0192F553,0x0192F554,0x0192F555,0x0192F556,0x0192F557,0x0192F558,0x0192F559,0x0192F55A,0x0192F55B,0x0192F55C,0x0192F55D,0x0192F55E,0x0192F55F,
0x0192FC00,0x0192FC01,0x0192FC02,0x0192FC03,0x0192FC04,0x0192FC05,0x0192FC06,0x0192FC07,0x0192FC08,0x0192FC09,0x0192FC0A,0x0192FC0B,0x0192FC0C,0x0192FC0D,0x0192FC0E,0x0192FC0F
]:

        _8br = random.randint(0x00,0xFF)

        _8bl = '%X' % _8bl
        _8br = '%X' % _8br
        _8bl = _8bl.zfill(8)

        _8br = _8br.zfill(8)

        f.write("patch=1,EE," + _8bl + ",extended," + _8br + "\n")
    f.close()