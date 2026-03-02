import numpy as np
import matplotlib.pyplot as plt
m = 2.0        
F = 4.0       
a = F / m      

t = np.linspace(0, 10, 200)
v = a * t                      
x = 0.5 * a * t**2              
a_plot = np.ones_like(t) * a 

plt.figure(figsize=(10, 5))
plt.plot(t, x, label="Position (x = 0.5 a t²)", linewidth=3)
plt.plot(t, v, label="Velocity (v = a t)", linestyle="--", linewidth=3)
plt.plot(t, a_plot, label="Acceleration (a)", linestyle=":", linewidth=3)
plt.title("Newton's Second Law — F = m a (Constant force example)")
plt.xlabel("Time (s)")
plt.ylabel("Position / Velocity / Acceleration")
plt.grid(True, linestyle="--", alpha=0.4)
plt.legend()
plt.show()