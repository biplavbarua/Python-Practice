'''To find adjoint
Compute the inverse of the matrix.
Transpose it.
Multiplies it by the determinant to get the adjoint.
'''

import numpy as np

def adjoint_matrix(A):
    return np.linalg.inv(A).T * np.linalg.det(A)

#numpy.linalg provides functions for performing linear algebra operations

#Example matrix
mat = np.array([[2, 3],[4, 5]])

adjoint_mat = adjoint_matrix(mat)
print("Adjoint of the matrix: \n", adjoint_mat)