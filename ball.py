import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
g=9.8
fig, ax = plt.subplots()

circle, = ax.plot([], [], 'bo', ms=10)
r = np.array([5.,5.])
v = np.array([-5.,0.])
h=0.05

def init():
    ax.set_xlim([-2., 10.])
    ax.set_ylim([-2., 10.])
    return circle,

def updatefig(frame): 
    r[1] = h*v[1]+r[1]
    v[1] = v[1]-h*g
    if r[1] <= 0.:
        v[1] = -v[1]  
        
    r[0] = h*v[0]+r[0]
    v[0] = v[0]-h*0
    if r[0] <= 0. or r[0] >= 10.:
        v[0] = -v[0] 

    
    circle.set_xdata(r[0])
    circle.set_ydata(r[1])
    return circle,

anim = animation.FuncAnimation(fig, updatefig, frames=200, init_func=init, interval=100, blit=True, repeat=False)

plt.show()
