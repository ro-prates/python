# import necessary libraries
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# set up figure and axes
fig = plt.figure(figsize=(7,7))
ax = plt.axes(xlim=(-20, 20), ylim=(-20, 20))

# set up the three bodies and their initial conditions
body1 = {"m":1,"x":0.0,"y":0.0,"vx":0.5,"vy":0.5}
body2 = {"m":2,"x":10.0,"y":0.0,"vx":-1.0,"vy":-0.5}
body3 = {"m":3,"x":-10.0,"y":0.0,"vx":1.0,"vy":0.5}

# create a scatter plot of the three bodies
scat1 = ax.scatter(body1["x"],body1["y"],c="red")
scat2 = ax.scatter(body2["x"],body2["y"],c="blue")
scat3 = ax.scatter(body3["x"],body3["y"],c="green")

# define the update function for the animation
def update(frame_number):
    # set the acceleration vector
    ax1,ay1 = -body1["x"]/np.sqrt(body1["x"]**2+body1["y"]**2)**3, -body1["y"]/np.sqrt(body1["x"]**2+body1["y"]**2)**3
    ax2,ay2 = -body2["x"]/np.sqrt(body2["x"]**2+body2["y"]**2)**3, -body2["y"]/np.sqrt(body2["x"]**2+body2["y"]**2)**3
    ax3,ay3 = -body3["x"]/np.sqrt(body3["x"]**2+body3["y"]**2)**3, -body3["y"]/np.sqrt(body3["x"]**2+body3["y"]**2)**3
    
    # update the velocites
    body1["vx"] += ax1/body1["m"]
    body1["vy"] += ay1/body1["m"]
    body2["vx"] += ax2/body2["m"]
    body2["vy"] += ay2/body2["m"]
    body3["vx"] += ax3/body3["m"]
    body3["vy"] += ay3/body3["m"]
    
    # update the positions
    body1["x"] += body1["vx"]
    body1["y"] += body1["vy"]
    body2["x"] += body2["vx"]
    body2["y"] += body2["vy"]
    body3["x"] += body3["vx"]
    body3["y"] += body3["vy"]
    
    # update the plot
    scat1.set_offsets([body1["x"],body1["y"]])
    scat2.set_offsets([body2["x"],body2["y"]])
    scat3.set_offsets([body3["x"],body3["y"]])

# create the animation
animation = FuncAnimation(fig, update, frames=200, interval=20)

# show the animation
plt.show()