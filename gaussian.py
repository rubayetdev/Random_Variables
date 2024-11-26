import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm

# Gaussian Distribution Parameters
mu_values = [0, 1, -1]  # Varying mean values
sigma = 1  # Standard deviation

# Plotting
x = np.linspace(-5, 5, 1000)
plt.figure(figsize=(8, 6))
for mu in mu_values:
    plt.plot(x, norm.pdf(x, mu, sigma), label=f"$\mu={mu}$, $\sigma^2={sigma ** 2}$")

plt.title("Gaussian Distribution")
plt.xlabel("x")
plt.ylabel("PDF")
plt.legend()
plt.grid(True)
plt.show()
