# Schéma 1 (centré)
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

# Plot for t = t1
while t <= t1:
    un = u.copy()
    for j in range(1, N-1):
        u[j] = un[j] - a*dt/(2*dx)*(un[j+1]-un[j-1])
    u[0] = u[-1]
    u[-1] = u[-2]
    
    t += dt

u_exact = [u_0((x - a*t1)%L) for x in x]

L1_centre = np.linalg.norm(u-u_exact, 1)


# Schéma 2 décentré en amont
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

while t < 2.5:
    un = u.copy()
    for j in range(1, N-1):
        u[j] = un[j] - a*dt/dx*(un[j]-un[j-1]) 
    u[0] = u[-1]
    u[-1] = u[-2]

    t = round(t+dt, 2)
    
L1_decentre_amont = np.linalg.norm(u-u_exact, 1)


# Schéma 2 décentré en aval
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

while t < 2.5:
    un = u.copy()
    for j in range(0, N-1):
        u[j] = un[j] - a*dt/dx*(un[j+1]-un[j])
    u[0] = u[-1]
    u[-1] = u[-2]

    t = round(t+dt, 2)
    
L1_decentre_aval = np.linalg.norm(u-u_exact, 1)


# Schéma 3 (Lax-Friedrichs)
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

while t < 2.5:
    un = u.copy()
    for j in range(1, N-1):
        u[j] = 0.5*(un[j-1]+un[j+1]) - a*dt/(2*dx)*(un[j+1]-un[j-1])
    u[0] = u[-1]
    u[-1] = u[-2]

    t = round(t+dt, 2)
    
L1_Lax_Friedrichs = np.linalg.norm(u-u_exact, 1)


# Schéma 4 (Lax-Wendroff)
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

while t < 2.5:
    un = u.copy()
    for j in range(1, N-1):
        u[j] = un[j] - ((a*dt)/(2*dx))*(un[j+1]-un[j-1]) + (((a**2)*dt**2)/(2*dx**2))*(un[j-1]-2*un[j]+un[j+1])
    u[0] = u[-1]
    u[-1] = u[-2]

    t = round(t+dt, 2)
    
L1_Lax_Wendroff = np.linalg.norm(u-u_exact, 1)


# All errors in pandas series
import pandas as pd

errors = pd.Series([L1_centre, L1_decentre_amont, L1_Lax_Friedrichs, L1_Lax_Wendroff], index=['Centre', 'Decentre Amont', 'Lax-Friedrichs', 'Lax-Wendroff'])

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

