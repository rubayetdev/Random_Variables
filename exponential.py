import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import expon

# Exponential Distribution Parameters
lambda_values = [0.5, 1, 2]  # Varying rate parameters
x = np.linspace(0, 10, 1000)  # x values

# Plotting
plt.figure(figsize=(8, 6))
for lam in lambda_values:
    plt.plot(x, expon.pdf(x, scale=1 / lam), label=f"$\lambda={lam}$")

plt.title("Exponential Distribution")
plt.xlabel("x")
plt.ylabel("PDF")
plt.legend()
plt.grid(True)
plt.show()
