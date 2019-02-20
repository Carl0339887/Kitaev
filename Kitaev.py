import numpy as np

N = 7
def get_N():
    return N


[Jx, Jy, Jz] = [1, 1, 1]
def get_J():
    return [Jx, Jy, Jz]

def ux(i):
    return 1


def uy(i):
    return 1


def uz(i):
    return 1


###### define the M matrix ######
def init(N):
    N = int(N)
    return np.zeros([n_cell(N), n_cell(N)])


def n_cell(N):
    N = int(N)
    return N * N


def get_M(N):
    M = init(N)
    ncell = n_cell(N)
    for i in range(ncell):
        M[i, i] = uz(i) * Jz  # intra unit cell i, A->B, z bond

    for i in range(ncell - 1): # the boundary terms will be fixed by pbc
        M[i, i + 1] = ux(i) * Jx  # unit cell i to (i+1), A->B, x bond

    for i in range(ncell - N): # the boundary terms will be fixed by pbc
        M[i, i + N] = uy(i) * Jy  # unit cell i to (i+N), A->B, y bond

    for i in range(N):
        # pbc
        # M[ncell-N+i,i] = uy(ncell-N+i)*Jy # uc 1B->uc (n_cell-N)A
        # M[(i+1)*N-1,i*N] = ux((i+1)*N-1)*Jx # uc 1B-> uc (N)A, uc (N+1)B -> uc (2N)A
        M[(N - 1) * N + i, i] = uy(ncell - N + i) * Jy  # uc ((N-1)*N+i)A -> uc (i)B
        M[(i + 1) * N - 1, i * N] = ux((i + 1) * N - 1) * Jx  # uc (iN)A -> uc ((i-1)N+1)B

    return M


def get_Hamil(N):
    # Hamiltonian in f fermion basis

    M = get_M(N)
    M_T = M.transpose()
    h = M + M_T
    h_T = h.transpose()
    delta = M_T - M
    delta_T = delta.transpose() #  should be dagger actually

    ncell = n_cell(N)
    # print(ncell)
    Hamil = np.zeros([2 * ncell, 2 * ncell])
    for i in range(ncell):
        for j in range(ncell):
            Hamil[i, j] = h[i, j]
            Hamil[i + ncell, j] = delta_T[i, j]
            Hamil[i, j + ncell] = delta[i, j]
            Hamil[i + ncell, j + ncell] = -h_T[i, j]
    return 0.5 * Hamil










