import numpy as np
import matplotlib.pyplot as plt

t = np.linspace(0, 10, 200)
x = np.zeros_like(t)   
v = np.zeros_like(t)   
plt.figure(figsize=(10, 5))
plt.plot(t, x, label="Position (x)", linewidth=3)
plt.plot(t, v, label="Velocity (v)", linestyle="--", linewidth=3)
plt.title("Newton's First Law — Law of Inertia (Object at rest)")
plt.xlabel("Time (s)")
plt.ylabel("Value")
plt.grid(True, linestyle="--", alpha=0.4)
plt.legend()
plt.show()