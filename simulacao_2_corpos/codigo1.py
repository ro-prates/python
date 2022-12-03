import matplotlib.pyplot as plt
import matplotlib.animation as animation

def animate(i):
    
    # 3-body problem equations
    G = 6.67408
    m1, m2, m3 = 1.0, 1.0, 1.0
    x1, y1, vx1, vy1 = -1.0, 0.0, 0.0, 0.5
    x2, y2, vx2, vy2 = 1.0, 0.0, 0.0, -0.5
    x3, y3, vx3, vy3 = 0.0, 1.0, 0.5, 0.0

    r12 = ((x1-x2)**2 + (y1-y2)**2)**0.5
    r13 = ((x1-x3)**2 + (y1-y3)**2)**0.5
    r23 = ((x2-x3)**2 + (y2-y3)**2)**0.5
    ax1 = G * m2 * (x2 - x1) / r12**3 + G * m3 * (x3 - x1) / r13**3
    ay1 = G * m2 * (y2 - y1) / r12**3 + G * m3 * (y3 - y1) / r13**3
    ax2 = G * m1 * (x1 - x2) / r12**3 + G * m3 * (x3 - x2) / r23**3
    ay2 = G * m1 * (y1 - y2) / r12**3 + G * m3 * (y3 - y2) / r23**3
    ax3 = G * m1 * (x1 - x3) / r13**3 + G * m2 * (x2 - x3) / r23**3
    ay3 = G * m1 * (y1 - y3) / r13**3 + G * m2 * (y2 - y3) / r23**3

    x1 += vx1
    y1 += vy1
    x2 += vx2
    y2 += vy2
    x3 += vx3
    y3 += vy3
    vx1 += ax1
    vy1 += ay1
    vx2 += ax2
    vy2 += ay2
    vx3 += ax3
    vy3 += ay3
    
    # Plotting the orbits of the bodies
    plt.cla()
    plt.plot(x1,y1, marker='o')
    plt.plot(x2,y2, marker='o')
    plt.plot(x3,y3, marker='o')
    plt.xlabel('x-axis')
    plt.ylabel('y-axis')
    plt.title('3-Body Problem Animation')
    plt.legend(['Body 1', 'Body 2', 'Body 3'])

anim = animation.FuncAnimation(plt.gcf(), animate, frames=200, interval=50)
plt.show()