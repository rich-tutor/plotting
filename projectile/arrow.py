from matplotlib import pyplot as plt

class Arrow():
    def __init__(self, fig=None, ax=None):

        if fig is None and ax is None:
            self.fig, self.ax = plt.subplots()
            self.ax.set_xlim(0, 10)
            self.ax.set_ylim(0, 10)
        else:
            self.fig = fig
            self.ax = ax

        self.arrow = None
        self.x0 = None
        self.y0 = None
        self.xt = None
        self.yt = None

        # connect event listener
        self.cid_onclick = self.fig.canvas.mpl_connect('button_press_event', self.onclick)
        self.cid_release = self.fig.canvas.mpl_connect('button_release_event', self.onrelease)
        self.cid_move = None


    def onclick(self, event):
        self.x0 = event.xdata
        self.y0 = event.ydata
        print('button clicked at:',  self.x0, self.y0)
        self.cid_move = self.fig.canvas.mpl_connect('motion_notify_event', self.onmove)

    def onmove(self,event):
        # draw arrow pointing from x0, y0 to event.xdata, event.ydata
        print('moving at:', event.xdata, event.ydata)
        if self.arrow:
            self.arrow.remove()
        self.arrow =self.ax.annotate('', xy=(event.xdata, event.ydata), xytext=(self.x0, self.y0),arrowprops=dict(facecolor='black'))
        self.fig.canvas.draw()

    def onrelease(self, event):
        # disconnect onmove
        self.fig.canvas.mpl_disconnect(self.cid_move)
        self.xt,self.yt= event.xdata,event.ydata


    def calculate_velocity(self):
        vx = self.xt - self.x0
        vy = self.yt - self.y0
        return vx,vy


if __name__ == "__main__":
    arrow = Arrow()
    plt.show()