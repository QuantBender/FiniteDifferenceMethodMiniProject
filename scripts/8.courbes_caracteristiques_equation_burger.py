import numpy as np
import matplotlib.pyplot as plt

# Define the range of t
t = np.linspace(0, 4, 40)

# Define the values of a
a_values = np.linspace(0, 4, 40)

# Create a figure
_=plt.figure(figsize=(8, 6))

# Plot the characteristic curves for each a
for a in a_values:
    u0 = 0.4 if a < 2 else 0.1
    x = t * u0 + a
    _=plt.plot(x, t, label=f'a={a:.2f}')

# Add labels and title
_=plt.xlabel('x')
_=plt.ylabel('t')
_=plt.title("Characteristic curves for Burger's equation")

# Show the plot
plt.show()
