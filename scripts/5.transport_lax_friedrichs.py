import numpy as np
import matplotlib.pyplot as plt
import warnings
warnings.filterwarnings("ignore")


def u_0(x):
    if 3 <= x <= 4:
        return 1
    else:
        return 0
      
      
L = 10
a = 2
N = 100
CFL = 0.8
dx = L/(N-1)
dt = round(CFL*dx/a, 2)

x = np.linspace(0, L, N)

u0 = np.zeros(N)
u0[int(3/dx):int(4/dx)] = 1

u = u0.copy()
un = np.zeros(N)

t = 0

t1 = 2.5
t2 = 4.5

fig, axs = plt.subplots(2, 2, figsize=(12, 10))

# Plot for t = t1
while t <= t1:
    un = u.copy()
    for j in range(1, N-1):
        u[j] = 0.5*(un[j-1]+un[j+1]) - a*dt/(2*dx)*(un[j+1]-un[j-1])
    u[0] = u[-1]
    u[-1] = u[-2]

    t += dt
    
u_exact = [u_0((x - a*t1)%L) for x in x]

_=axs[0, 0].plot(x, u_exact, label='Exact Solution')
_=axs[0, 0].plot(x, u, label='Approximate Solution')
_=axs[0, 0].set_xlabel('x')
_=axs[0, 0].set_ylabel('u')
_=axs[0, 0].set_title(f't = {t1} et N = {N}')
_=axs[0, 0].legend()
_=axs[0, 0].set_ylim(-1.5, 1.5)
_=axs[0, 0].grid(True)

# Plot for t = t2
t = 0
u = u0.copy()

while t <= t2:
    un = u.copy()
    for j in range(1, N-1):
        u[j] = 0.5*(un[j-1]+un[j+1]) - a*dt/(2*dx)*(un[j+1]-un[j-1])
    u[0] = u[-1]
    u[-1] = u[-2]

    t += dt
    
u_exact = [u_0((x - a*t2)%L) for x in x]

_=axs[0, 1].plot(x, u_exact, label='Exact Solution')
_=axs[0, 1].plot(x, u, label='Approximate Solution')
_=axs[0, 1].set_xlabel('x')
_=axs[0, 1].set_ylabel('u')
_=axs[0, 1].set_title(f't = {t2} et N = {N}')
_=axs[0, 1].legend()
_=axs[0, 1].set_ylim(-1.5, 1.5)
_=axs[0, 1].grid(True)

# Plot for t = t1 with N=200
N = 200
dx = L/(N-1)
dt = round(CFL*dx/a, 2)

x = np.linspace(0, L, N)

u0 = np.zeros(N)
u0[int(3/dx):int(4/dx)] = 1

u = u0.copy()
un = np.zeros(N)

t = 0
u = u0.copy()

while t <= t1:
    un = u.copy()
    for j in range(1, N-1):
        u[j] = 0.5*(un[j-1]+un[j+1]) - a*dt/(2*dx)*(un[j+1]-un[j-1])
    u[0] = u[-1]
    u[-1] = u[-2]

    t += dt
    
u_exact = [u_0((x - a*t1)%L) for x in x]

_=axs[1, 0].plot(x, u_exact, label='Exact Solution')
_=axs[1, 0].plot(x, u, label='Approximate Solution')
_=axs[1, 0].set_xlabel('x')
_=axs[1, 0].set_ylabel('u')
_=axs[1, 0].set_title(f't = {t1} et N = {N}')
_=axs[1, 0].legend()
_=axs[1, 0].set_ylim(-1.5, 1.5)
_=axs[1, 0].grid(True)

# Plot for t = t2 with N=200
t = 0
u = u0.copy()

while t <= t2:
    un = u.copy()
    for j in range(1, N-1):
        u[j] = 0.5*(un[j-1]+un[j+1]) - a*dt/(2*dx)*(un[j+1]-un[j-1])
    u[0] = u[-1]
    u[-1] = u[-2]

    t += dt
    
u_exact = [u_0((x - a*t2)%L) for x in x]

_=axs[1, 1].plot(x, u_exact, label='Exact Solution')
_=axs[1, 1].plot(x, u, label='Approximate Solution')
_=axs[1, 1].set_xlabel('x')
_=axs[1, 1].set_ylabel('u')
_=axs[1, 1].set_title(f't = {t2} et N = {N}')
_=axs[1, 1].legend()
_=axs[1, 1].set_ylim(-1.5, 1.5)
_=axs[1, 1].grid(True)
  
_=plt.tight_layout()
_=plt.suptitle("Schema Lax-Friedrichs", y=1.02)
plt.show()
