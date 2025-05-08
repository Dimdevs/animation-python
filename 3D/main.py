import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np

fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111, projection='3d')

sun_x, sun_y, sun_z = 0, 0, 0

planet_data = {
    "Mercury": {"radius": 0.01, "distance": 1, "color": 'gray'},    
    "Venus": {"radius": 0.02, "distance": 1.5, "color": '#877882'},  
    "Earth": {"radius": 0.05, "distance": 2, "color": 'blue'},      
    "Mars": {"radius": 0.03, "distance": 3, "color": 'red'},        
    "Jupiter": {"radius": 0.15, "distance": 5, "color": 'orange'}, 
    "Saturn": {"radius": 0.12, "distance": 7, "color": 'gold'},    
    "Uranus": {"radius": 0.1, "distance": 9, "color": 'lightblue'},
    "Neptune": {"radius": 0.1, "distance": 11, "color": 'darkblue'}
}

ax.scatter(sun_x, sun_y, sun_z, c='#FCF259', marker='o', s=100, label="Sun")

for planet, data in planet_data.items():
    theta = np.linspace(0, 2 * np.pi, 100)
    x_orbit = data["distance"] * np.cos(theta)
    y_orbit = data["distance"] * np.sin(theta)
    z_orbit = np.zeros_like(x_orbit)
    ax.plot(x_orbit, y_orbit, z_orbit, color='gray', linestyle='dotted')
    ax.scatter(x_orbit[0], y_orbit[0], z_orbit[0], c=data["color"], s=data["radius"]*1000, label=planet)

ax.set_xlabel('X Axis')
ax.set_ylabel('Y Axis')
ax.set_zlabel('Z Axis')

ax.set_title('Tata Surya 3D - Matahari dan Planet-Planet')

ax.legend()

plt.show()