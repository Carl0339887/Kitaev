import Kitaev as ktv
import numpy as np


# N by N unit cells
N = ktv.get_N()

# Jx, Jy, Jz
[Jx, Jy, Jz] = ktv.get_J()


# real space basis
n1 = np.array([+0.5, 0.5 * np.sqrt(3)])
n2 = np.array([-0.5, 0.5 * np.sqrt(3)])

# momentum space basis
m1 = np.array([+2*np.pi / N, 2*np.pi / np.sqrt(3) / N])
m2 = np.array([-2*np.pi / N, 2*np.pi / np.sqrt(3) / N])

# q points in FBZ
q = []
def get_q():
    for i in range(N):
        for j in range(N):
            q.append(i*m1 + j*m2)

get_q()


##################################################

# Structral factor
def Im_S(q):
    s = Jx * np.sin(np.dot(q, n1)) + Jy * np.sin(np.dot(q, n2))
    return s

def Re_S(q):
    s = Jx * np.cos(np.dot(q, n1)) + Jy * np.cos(np.dot(q, n2)) + Jz
    return s

# Theta
#def theta(q):
#    return - 0.5 * np.arctan(Im_S(q) / Re_S(q))

def occup2():
    occupation2 = 0.0
    for k in q:
        occupation2 += 0.5*(1 +(Re_S(k))/(np.sqrt(Re_S(k)**2 + Im_S(k)**2)))
    return occupation2

print occup2()


"""
idx=[]

l = int(np.ceil(N/2.0))

def get_q():
    for i in range(-l, l+1):
        for j in range(-l, l+1):
            print i,j
            if Is_In_BZ(i,j):
                idx.append([i,j])
                q.append(i * m1 + j * m2)

    if len(q) > N**2:
        print 'Double counted points near the BZ boundary'
    if len(q) < N**2:
        print 'Missing points near the BZ bounday'


def Is_In_BZ(i,j):
    a = i * m1 + j * m2
    x = a[0]
    y = a[1]

    if -2 * np.pi / np.sqrt(3) < y < 2 * np.pi / np.sqrt(3) + 1E-10:
        if -np.sqrt(3) * (x + 4*np.pi/3) < y < -np.sqrt(3) * (x - 4*np.pi/3) + 1E-10:
            if np.sqrt(3) * (x - 4*np.pi/3) < y < np.sqrt(3) * (x + 4*np.pi/3) + 1E-10:
                print i,j
                return 1
    return 0


get_q()
"""









