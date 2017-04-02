# Count the negative elements in an n-dim array

import numpy as np
a=np.array([[1,-2,-3],[0,-.3,23],[1,12,323]])

def countNeg(matrix):
    row,col = np.shape(matrix)
    count=0
    for r,c in range(row,col):
        for c in range(col):
            if matrix[r,c] < 0:
                count +=1
    return count

countNeg(a)
