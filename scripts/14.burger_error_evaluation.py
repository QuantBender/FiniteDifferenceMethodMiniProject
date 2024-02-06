# Schéma 1 (centré)
import numpy as np
import matplotlib.pyplot as plt
import warnings
warnings.filterwarnings("ignore")


def u_0(x):
    if  x < 2:
        return 0.4
    else:
        return 0.1
      
def F(u):
    return (u**2)/2
  
  
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


# Plot for t = t1
while t <= t1:
    dt = (CFL*dx)/(max(np.abs(u)))
    un = u.copy()
    for j in range(1, N-1):
        u[j] = un[j] - ((dt)/(2*dx))*un[j]*(un[j+1]-un[j-1])
    u[0] = u[1]
    u[-1] = u[-2]
    
    t += dt
    
u_exacte = [u_exact(y, t1) for y in x]

L1_centre = np.linalg.norm(u-u_exacte, 1)


# Schéma 2 (décentré en amont)
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


# Plot for t = t1
while t <= t1:
    dt = (CFL*dx)/(max(np.abs(u)))
    un = u.copy()
    for j in range(1, N):
        u[j] = un[j] - (dt/dx)*(F(un[j])-F(un[j-1]))
    u[0] = u[1]
    u[-1] = u[-2]
    
    t += dt
    
u_exacte = [u_exact(y, t1) for y in x]

L1_amont = np.linalg.norm(u-u_exacte, 1)


# Schéma 3 (décentré en aval)
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

L1_aval = np.linalg.norm(u-u_exacte, 1)

# Schéma 4 (Lax-Friedrichs)

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


# Plot for t = t1
while t <= t1:
    dt = (CFL*dx)/(max(np.abs(u)))
    un = u.copy()
    for j in range(1, N-1):
        u[j] = 0.5*(un[j+1]+un[j-1]) - (dt/(2*dx))*(F(un[j+1])-F(un[j-1]))
    u[0] = u[1]
    u[-1] = u[-2]
    
    t += dt
    
u_exacte = [u_exact(y, t1) for y in x]

L1_friedrichs = np.linalg.norm(u-u_exacte, 1)

# Schéma 5 (Lax-Wendroff)
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


# Plot for t = t1
while t <= t1:
    dt = (CFL*dx)/(max(np.abs(u)))
    un = u.copy()
    for j in range(1, N-1):
        alpha = 1 - (dt/(2*dx))*(un[j+1]-un[j])
        lambda_ = (dt/dx)
        u[j] = un[j] + un[j]*(lambda_**2/2)*(F(un[j-1])-2*F(un[j])+F(un[j+1])) - alpha*(lambda_/2)*(F(un[j+1])-F(un[j-1]))
    u[0] = u[1]
    u[-1] = u[-2]
    
    t += dt
    
u_exacte = [u_exact(y, t1) for y in x]

L1_wendroff = np.linalg.norm(u-u_exacte, 1)

# All errors in pandas series
import pandas as pd

errors = pd.Series([L1_centre, L1_amont, L1_friedrichs, L1_wendroff], index=['Centre', 'Decentre Amont', 'Lax-Friedrichs', 'Lax-Wendroff'])

_=plt.figure(figsize=(10, 8))
# Plot errors with barplot having error value above bar
ax = errors.plot(kind='bar', figsize=(10, 8), color='skyblue', zorder=2, width=0.5)

for i in ax.patches:
    _=ax.text(i.get_x() + i.get_width() / 2, i.get_height() + 0.1, round(i.get_height(), 2), ha='center', va='bottom')

_=ax.set_xticklabels(ax.get_xticklabels(), rotation=45)  # Rotate xticks by 45 degrees

_=ax.set_xlabel('Schemas numeriques')
_=ax.set_ylabel('Erreur en norme L1')
_=ax.set_title('Erreur en norme L1 pour chaque schema numerique')
_=ax.grid(axis='y', linestyle='--', zorder=1)
plt.show()
