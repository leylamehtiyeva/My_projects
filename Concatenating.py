"""
Given a two-dimensional array X.
All elements with even indices must be cubed. Then write the elements in reverse order relative to their positions.
At the end, you need to merge the X array with the transformed X and return it to the function output
"""

import numpy as np

X = np.array([[1,2,3,4,5],[1,2,3,4,5]])


def transform(X, a=1):
    A = X.copy()
    res = [a if i % 2 != 0 else el**3 for lst in A for i, el in enumerate(lst)]

    result = np.array(res[::-1]).reshape(X.shape)
    reversed = np.concatenate((X, result), axis=1)

    return reversed


print(transform(X))
