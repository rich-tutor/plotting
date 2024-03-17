from arrow import Arrow
from projectile import Projectile
from matplotlib import pyplot as plt


class InteractiveGraph():
    def __init__(self):
        self.fig, self.ax = plt.subplots()
        self.ax.set_xlim(0, 10)
        self.ax.set_ylim(0, 10)
        self.arrow = Arrow(self.fig, self.ax)
        self.cid_release = self.fig.canvas.mpl_connect('button_release_event', self.onrelease)
        self.projectile = None


    def onrelease(self, event):
        if self.projectile:
            self.projectile.ani.event_source.stop()
            self.projectile.scat.remove()
        x0, y0 = self.arrow.x0, self.arrow.y0
        vx, vy = self.arrow.calculate_velocity()
        self.projectile = Projectile(x0, y0, self.fig, self.ax, vx, vy, 0.01)
        self.projectile.animate()


if __name__=='__main__':
    graph = InteractiveGraph()
    plt.show()


