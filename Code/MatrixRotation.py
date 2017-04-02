# Rotate a matrix in place (clockwise)

import numpy as np                             # first create a sample matrix 
a=np.array([[1,2,3],[4,5,6],[7,8,9]])


def matrixRot(matrix):
    row,col=np.shape(matrix)                   # getting the total number of rows & columns of given matrix
    temp=np.empty(shape=[row,col])             # initialize a same dimension empty matrix
    
    for i in range(row):
        for j in range(col):
            temp[i,col-1-j]=matrix[j,i]        # clockwise elements rotation
    return temp

print(a)
print(matrixRot(a))
