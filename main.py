import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

class HeatEquation2D:
    def __init__(self, Nx=120, Ny=120, Lx=1.0, Ly=1.0, alpha=0.01,
                 T_init=20.0, T_hot=100.0, T_left=0.0, T_right=0.0,
                 T_bottom=0.0, hotspot_temp=200.0, hotspot_radius=0.07,
                 safety_factor=0.40):
        self.Nx, self.Ny = Nx, Ny
        self.Lx, self.Ly = Lx, Ly
        self.alpha = alpha
        self.dx = Lx / (Nx + 1)
        self.dy = Ly / (Ny + 1)
        self.dt = safety_factor * (self.dx**2 * self.dy**2) / (2 * alpha * (self.dx**2 + self.dy**2))
        self.rx = alpha * self.dt / self.dx**2
        self.ry = alpha * self.dt / self.dy**2
        self.T_hot, self.T_left, self.T_right, self.T_bottom = T_hot, T_left, T_right, T_bottom
        self.time = 0.0
        self.x = np.linspace(0, Lx, Nx + 2)
        self.y = np.linspace(0, Ly, Ny + 2)
        self.T = self._init_field(T_init, hotspot_temp, hotspot_radius)
        print(f"Solver ready — dt = {self.dt:.2e} s,  rx = {self.rx:.4f},  ry = {self.ry:.4f}")

    def _init_field(self, T_init, hotspot_temp, hotspot_radius):
        T = np.full((self.Ny + 2, self.Nx + 2), T_init, dtype=np.float64)
        T[-1, :] = self.T_hot
        T[0,  :] = self.T_bottom
        T[:,  0] = self.T_left
        T[:, -1] = self.T_right
        cx, cy = self.Lx / 2, self.Ly / 2
        sigma = hotspot_radius * self.Lx
        XX, YY = np.meshgrid(self.x, self.y)
        T += (hotspot_temp - T_init) * np.exp(-((XX - cx)**2 + (YY - cy)**2) / (2 * sigma**2))
        T[-1, :] = self.T_hot
        T[0,  :] = self.T_bottom
        T[:,  0] = self.T_left
        T[:, -1] = self.T_right
        return T

    def step(self, n=1):
        for _ in range(n):
            T = self.T
            T[1:-1, 1:-1] = (
                T[1:-1, 1:-1]
                + self.rx * (T[2:, 1:-1] - 2*T[1:-1, 1:-1] + T[:-2, 1:-1])
                + self.ry * (T[1:-1, 2:] - 2*T[1:-1, 1:-1] + T[1:-1, :-2])
            )
            self.time += self.dt

solver = HeatEquation2D()

fig, ax = plt.subplots(figsize=(6, 5))
fig.patch.set_facecolor("#0d0d0d")
ax.set_facecolor("#0d0d0d")
ax.tick_params(colors="white")
ax.set_xlabel("x [m]", color="white")
ax.set_ylabel("y [m]", color="white")

im = ax.imshow(solver.T, origin="lower", extent=[0,1,0,1],
               cmap="inferno", vmin=0, vmax=210,
               interpolation="bilinear", aspect="auto")

cbar = fig.colorbar(im, ax=ax, pad=0.02)
cbar.set_label("Temperature (°C)", color="white")
plt.setp(cbar.ax.yaxis.get_ticklabels(), color="white")

title = ax.set_title("t = 0.000000 s", color="white", fontsize=12)
fig.tight_layout()

def update(frame):
    solver.step(60)
    im.set_data(solver.T)
    title.set_text(f"2D Heat Diffusion — t = {solver.time:.4f} s")
    return im, title

anim = animation.FuncAnimation(fig, update, frames=200, interval=30, blit=False, repeat=False)
anim.save("heat_diffusion.gif", writer=animation.PillowWriter(fps=20), dpi=100)

from IPython.display import Image
Image("heat_diffusion.gif")
  
