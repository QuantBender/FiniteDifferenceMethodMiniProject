import numpy as np
import matplotlib.pyplot as plt
import warnings
warnings.filterwarnings("ignore")


def u_0(x):
    if  x < 2:
        return 0.4
    else:
        return 0.1
      
def u_exact(x, t):
    if ((x-2)/t) < 0.25:
        return 0.4
    else:
        return 0.1
      
L = 6
N = 100
CFL = 0.8
dx = L/(N-1)

x = np.linspace(0, L, N)

u0 = np.zeros(N)

for i in range(N):
    u0[i] = u_0(x[i])
    
u = u0.copy()
un = np.zeros(N)

t = 0

t1 = 2.5
t2 = 4.5

fig, axs = plt.subplots(2, 2, figsize=(12, 10))

# Plot for t = t1
while t <= t1:
    dt = (CFL*dx)/(max(np.abs(u)))
    un = u.copy()
    for j in range(0, N-1):
        u[j] = un[j] - (dt/dx)*un[j]*(un[j+1]-un[j])
    u[0] = u[1]
    u[-1] = u[-2]
    
    t += dt
    
u_exacte = [u_exact(y, t1) for y in x]

_=axs[0, 0].plot(x, u_exacte, label='Exact Solution')
_=axs[0, 0].plot(x, u, label='Approximate Solution')
_=axs[0, 0].set_xlabel('x')
_=axs[0, 0].set_ylabel('u')
_=axs[0, 0].set_title(f't = {t1} et N = {N}')
_=axs[0, 0].legend()
_=axs[0, 0].set_ylim(-.5, 1)
_=axs[0, 0].grid(True)

# Plot for t = t2
t = 0
u = u0.copy()

while t <= t2:
    dt = (CFL*dx)/(max(np.abs(u)))
    un = u.copy()
    for j in range(0, N-1):
        u[j] = un[j] - (dt/dx)*un[j]*(un[j+1]-un[j])
    u[0] = u[1]
    u[-1] = u[-2]
    
    t += dt
    
u_exacte = [u_exact(y, t2) for y in x]

_=axs[0, 1].plot(x, u_exacte, label='Exact Solution')
_=axs[0, 1].plot(x, u, label='Approximate Solution')
_=axs[0, 1].set_xlabel('x')
_=axs[0, 1].set_ylabel('u')
_=axs[0, 1].set_title(f't = {t2} et N = {N}')
_=axs[0, 1].legend()
_=axs[0, 1].set_ylim(-.5, 1)
_=axs[0, 1].grid(True)

# Plot for t = t1 with N=200
N = 200
dx = L/(N-1)

x = np.linspace(0, L, N)

u0 = np.zeros(N)

for i in range(N):
    u0[i] = u_0(x[i])
    
u = u0.copy()
un = np.zeros(N)

t = 0

while t <= t1:
    dt = (CFL*dx)/(max(abs(u)))
    un = u.copy()
    for j in range(0, N-1):
        u[j] = un[j] - (dt/dx)*un[j]*(un[j+1]-un[j])
    u[0] = u[1]
    u[-1] = u[-2]
    
    t += dt
    
u_exacte = [u_exact(y, t1) for y in x]

_=axs[1, 0].plot(x, u_exacte, label='Exact Solution')
_=axs[1, 0].plot(x, u, label='Approximate Solution')
_=axs[1, 0].set_xlabel('x')
_=axs[1, 0].set_ylabel('u')
_=axs[1, 0].set_title(f't = {t1} et N = {N}')
_=axs[1, 0].legend()
_=axs[1, 0].set_ylim(-.5, 1)
_=axs[1, 0].grid(True)

# Plot for t = t2 with N=200
t = 0
u = u0.copy()

while t <= t2:
    dt = (CFL*dx)/(max(abs(u)))
    un = u.copy()
    for j in range(0, N-1):
        u[j] = un[j] - (dt/dx)*un[j]*(un[j+1]-un[j])
    u[0] = u[1]
    u[-1] = u[-2]
    
    t += dt
    
u_exacte = [u_exact(y, t2) for y in x]

_=axs[1, 1].plot(x, u_exacte, label='Exact Solution')
_=axs[1, 1].plot(x, u, label='Approximate Solution')
_=axs[1, 1].set_xlabel('x')
_=axs[1, 1].set_ylabel('u')
_=axs[1, 1].set_title(f't = {t2} et N = {N}')
_=axs[1, 1].legend()
_=axs[1, 1].set_ylim(-.5, 1)
_=axs[1, 1].grid(True)
  
_=plt.tight_layout()
_=plt.suptitle("Schema Decentre en Aval", y=1.02)
plt.show()
