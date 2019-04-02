# -*- coding: utf-8 -*-
"""
Created on Tue Apr  2 15:58:27 2019

@author: Tylor
"""
from pprint import pprint


def hilmat(a, b):
    return [[1 / (i + j + 1) for j in range(b)] for i in range(a)]


pprint(hilmat(4, 4))
