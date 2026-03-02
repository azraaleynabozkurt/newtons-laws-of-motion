import numpy as np
import matplotlib.pyplot as plt

m1 = 1.0     
m2 = 3.0     
F_on_1 = 5.0     
F_on_2 = -5.0   

a1 = F_on_1 / m1
a2 = F_on_2 / m2

t = np.linspace(0, 10, 200)
v1 = a1 * t
v2 = a2 * t

plt.figure(figsize=(10, 5))
plt.plot(t, v1, label=f"Object 1 velocity (m={m1} kg)", linewidth=3)
plt.plot(t, v2, label=f"Object 2 velocity (m={m2} kg)", linestyle="--", linewidth=3)
plt.title("Newton's Third Law — Action and Reaction (Equal and opposite forces)")
plt.xlabel("Time (s)")
plt.ylabel("Velocity (m/s)")
plt.grid(True, linestyle="--", alpha=0.4)
plt.legend()
plt.show()