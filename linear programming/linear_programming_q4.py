
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider

# Constants for the objective function
c1, c2 = 2, 5  # Coefficients for x and y in the objective function

# Define the constraints
def constraint1(x):
    return (200 - x)


# Initial Z value
initial_Z = 300

# Create the plot
fig, ax = plt.subplots()
plt.subplots_adjust(left=0.1, bottom=0.25)

x = np.linspace(0, 400, 400)
y1 = constraint1(x)

# Plot constraints with labels for the legend
ax.plot(x, y1, label=r'$f + t \leq 200$', color='blue')
ax.axvline(150, color='black')
ax.axhline(120, color='black')

ax.set_xlim((0, 210))
ax.set_ylim((0, 210))
ax.set_xlabel('$flags$')
ax.set_ylabel('$t-shirts$')

# Highlight the feasible region
ax.fill_between(x, 210, y1, alpha=1, color='pink')
ax.fill_between(x, 210, 120, alpha=1, color='pink')
ax.fill_betweenx(np.arange(0,210), 150, 210, alpha=1, color='pink')


# Level curve for the objective function
y4 = (initial_Z - c1 * x) / c2
line, = ax.plot(x, y4, '--', color='green', label=f'Income: $f+5t = {initial_Z}$')

# Initially create the legend with all labels
ax.legend()

# Add slider for adjusting Z value
axZ = plt.axes([0.1, 0.1, 0.65, 0.03],)
sZ = Slider(axZ, 'Z', 100, 1100, valinit=initial_Z)

# Update function for the slider
def update(val):
    Z = sZ.val
    line.set_ydata((Z - c1 * x) / c2)
    # Update the label for the level curve in the legend
    line.set_label(f'Income: $f+5t = {Z}$')
    # Rebuild the legend to include the updated label
    ax.legend()
    fig.canvas.draw_idle()

sZ.on_changed(update)

plt.show()
