import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
g=9.8
fig, ax = plt.subplots()

circle, = ax.plot([], [], 'bo', ms=10)
r = np.array([5.,5.])
v = np.array([-5.,0.])
h=0.02

def init():
    ax.set_xlim([-2., 10.])
    ax.set_ylim([-2., 10.])
    return circle,

def updatefig(frame): 
    v[1] = v[1]-h*g
    r[1] = r[1]+h*v[1]-0.5*g*h*h
    if r[1] <= 0.:
        v[1] = -v[1] 
 
    v[0] = v[0]-h*0
    r[0] = r[0]+h*v[0]
    
    if r[0] <= 0. or r[0] >= 10.:
       v[0] = -v[0] 


    
    circle.set_xdata(r[0])
    circle.set_ydata(r[1])
    return circle,

anim = animation.FuncAnimation(fig, updatefig, frames=600, init_func=init, interval=10, blit=True, repeat=False)

plt.show()
