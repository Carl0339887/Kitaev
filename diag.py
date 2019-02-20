import Kitaev as ktv
import numpy as np

N = ktv.get_N()
Hamil = ktv.get_Hamil(N)
# print(Hamil)

import numpy.linalg as linalg
w,v = linalg.eigh(Hamil) # Already sorted, first half of w's are negative.

#    print w, v
#    print '\n\n'
"""
    
    U = np.zeros([2*N**2,2*N**2])
    D = np.zeros([2*N**2,2*N**2])
    for i in range(len(w)):
        D[i,i] = w[i]
        for j in range(len(w)):
            U[i,j] = v[i,j]
    
    H = np.matmul(D, U.transpose())
    H = np.matmul(U, H)
    # print H - Hamil
    print np.matmul(H,U) - np.matmul(U,D)
"""


def occup1(v):
    occupation = 0.0
    for i in range(N**2):
        # The first N^2 eigenvalues are negative
        for j in range(2 * N**2):
            occupation += v[i,j] * np.conjugate(v[i,j])

    return occupation




print occup1(v)




