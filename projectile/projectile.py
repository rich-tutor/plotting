from matplotlib import pyplot as plt
from matplotlib import animation
import numpy as np

class Projectile():

    def __init__(self, x0=1, y0=1, fig=None, ax=None, vx=2, vy=5, dt=0.01):
        self.x0 =  x0
        self.y0 = y0
        self.vx = vx
        self.vy = vy
        self.dt = dt
        self.duration=5
        self.ani= None

        self.xy= None

        if fig is None and ax is None:
            self.fig, self.ax = plt.subplots()
            self.ax.set_xlim(0, 10)
            self.ax.set_ylim(0, 10)
            self.scat = self.ax.scatter(x0, y0, s=50)
        else:
            self.fig, self.ax =fig,ax
            self.scat = self.ax.scatter(x0, y0, s=50)


    def calculate_projectile(self):
        '''
        calculate the coordinates x,y with time interval dt
        :return: None
        '''
        t = np.arange(0, self.duration, self.dt)
        x = self.x0 + self.vx * t
        y = self.y0 + self.vy * t - 0.5 * 9.8 * t**2
        self.xy = np.vstack((x, y)).T

    def update(self, frame):
        '''
        update the scatter plot with coordinates x,y for current frame
        :return:
        '''
        self.scat.set_offsets(self.xy[frame])

    def animate(self):
        if self.ani:
            self.ani.event_source.stop()

        self.calculate_projectile()
        self.ani = animation.FuncAnimation(self.fig, self.update, frames=len(self.xy), interval=self.dt)
        self.fig.canvas.draw()




if __name__ == "__main__":
    p = Projectile()

    p.animate()
    plt.show()