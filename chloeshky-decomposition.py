# -*- coding: utf-8 -*-
"""
Created on Tue Apr  2 20:39:42 2019

@author: Tylor
"""

import numpy as np

"""
Implementation of Choleshy decomposition
"""

A = np.array([[1, -2j], [2j, 5]])
print("A: ", A)

L = np.linalg.cholesky(A)
print("L: ", L)

Z = np.dot(L, L.T.conj())
print("Z: ", Z)

B = [[1, -2j], [2j, 5]]

M = np.linalg.cholesky(B)
print("M: ", M)

Y = np.linalg.cholesky(np.matrix(B))
print("Y: ", Y)
