#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri May 25 11:35:48 2018

@author: snigdha
"""

import numpy as np

dicty = {}
dicty["Heidi"] = 1
dicty["is"] = 2
dicty["my"] = 3
dicty["name"] = 4


sen = "Heidiismyname"

s = []
i = 0
j = 1
while(j <= len(sen)):
    if sen[i:j] in dicty:
        k = j
        origstr = sen[i:j]
        print("origstr",origstr)
        newj = 0
        maxlen = 0
        stri = ""
        while(j <= len(sen)):
            if(sen[i:j] in dicty):
                if(len(sen[i:j]) > maxlen):
                    print("stri",sen[i:j])
                    maxlen = len(sen[i:j])
                    stri = sen[i:j]
                    newj = j
            j = j + 1
        if(origstr == stri):
            s.append(origstr)
            j = k + 1
            i = i + len(origstr)
        else:
            s.append(stri)
            j = newj + 1
            i = i + len(stri)

    else:
        j = j + 1
  