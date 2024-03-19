import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider

# Constants for the objective function
c1, c2 = 0.8, 1.2  # Coefficients for x and y in the objective function

# Define the constraints
def constraint1(x):
    return (140 - 10*x) / 20

def constraint2(x):
    return (7.2-0.6*x) / 0.8

# Initial Z value
initial_Z = 10

# Create the plot
fig, ax = plt.subplots()
plt.subplots_adjust(left=0.1, bottom=0.25)

x = np.linspace(0, 20, 400)
y1 = constraint1(x)
y2 = constraint2(x)

# Plot constraints with labels for the legend
ax.plot(x, y1, label=r'$10A + 20B \leq 140$', color='blue')
ax.fill_between(x,15 , y1, alpha=1, color='pink')

ax.plot(x, y2, label=r'$0.6A + 0.8B \leq 7.2$', color='red')
ax.fill_between(x, 15, y2, alpha=1, color='pink')

ax.set_xlim((0, 15))
ax.set_ylim((0, 10))
ax.set_xlabel('$x$')
ax.set_ylabel('$y$')

# Level curve for the objective function
y4 = (initial_Z - c1 * x) / c2
line, = ax.plot(x, y4, '--', color='green', label=f'Storage Space: $0.8A+1.2B={initial_Z}$')

# Initially create the legend with all labels
ax.legend()

# Add slider for adjusting Z value
axZ = plt.axes([0.1, 0.1, 0.65, 0.03])
sZ = Slider(axZ, 'Z', 1, 50, valinit=initial_Z)

# Update function for the slider
def update(val):
    Z = sZ.val
    line.set_ydata((Z - c1 * x) / c2)
    # Update the label for the level curve in the legend
    line.set_label(f'Storage Space: $0.8A+1.2B={Z}$')
    # Rebuild the legend to include the updated label
    ax.legend()
    fig.canvas.draw_idle()

sZ.on_changed(update)

plt.show()
