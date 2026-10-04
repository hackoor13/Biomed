import numpy as np
import matplotlib.pyplot as plt

Nx=18
Ny=9

M= Ny//2

c=3
h=0.1

N=Nx*Ny

A=np.zeros((N,N))
b=np.zeros((N))

for i in range(Ny):
    for j in range(Nx):
        k=i*Nx+j
        
        if j==0 :
            if i==M:
                A[k,k]=1
                b[k]=1
            else:
                A[k,k]=1
                A[k,k+1]=-1
                b[k]=0
        elif j == Nx-1:
            A[k,k]=1+c*h
            A[k,k-1]=-1
            b[k]=0
        elif i == 0:
            A[k,k]=1
            A[k,k+Nx]=-1
            b[k]=0
        elif i == Ny-1:
            A[k,k]=1
            A[k,k-Nx]=-1
            b[k]=0
        else:
            A[k,k]=4
            A[k,k-1]=-1
            A[k,k+1]=-1
            A[k,k-Nx]=-1
            A[k,k+Nx]=-1
            b[k]=0
U = np.linalg.solve(A, b)
u=U.reshape((Ny,Nx))


plt.imshow(u, origin="lower", aspect="auto")

for i in range(Ny):
    for j in range(Nx):
        plt.text(j, i, f"{u[i,j]:.2f}",
                 ha="center", va="center")

plt.colorbar(label="u")
plt.xlabel("x")
plt.ylabel("y")
plt.title("Solution u(x,y)")
plt.show()