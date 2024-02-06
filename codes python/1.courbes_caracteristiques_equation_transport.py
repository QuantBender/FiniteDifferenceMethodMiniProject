import numpy as np
import matplotlib.pyplot as plt
import warnings
warnings.filterwarnings("ignore")

# Define the values of a and xi
a = 2
xi_values = [-4, -3, -2, -1, 0, 1, 2, 3, 4]

# Define the time range
t = np.linspace(-10, 10, 100)

plt.figure(figsize=(12, 8))
# Plot the characteristic curves for each xi value
for xi in xi_values:
    x = a * t + xi
    plt.plot(t, x, label=f"xi = {xi}")

# Plot the x and y axes
plt.axhline(0, color='black')
plt.axvline(0, color='black')

plt.xlabel('Time')
plt.ylabel('x(t)')
plt.title('Courbes Caracteristiques')
plt.grid(True)
plt.legend()

# Set the x and y axes limits to center at 0
_ = plt.xlim(-10, 10)
_ = plt.ylim(-10, 10)

# Set the x and y axis ticks
_ = plt.xticks(np.arange(-10, 11, 2))
_ = plt.yticks(np.arange(-10, 11, 2))

# Hide the legend
plt.legend().set_visible(False)
plt.show()
