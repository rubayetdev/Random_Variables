import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import poisson

# Poisson Distribution Parameters
lambdas = [2, 5, 8]  # Varying lambda values
k = np.arange(0, 20)  # Possible values of k

# Plotting
plt.figure(figsize=(8, 6))
for lam in lambdas:
    plt.stem(k, poisson.pmf(k, lam), label=f"$\lambda={lam}$", basefmt=" ", linefmt="-", markerfmt="o")

plt.title("Poisson Distribution")
plt.xlabel("k")
plt.ylabel("PMF")
plt.legend()
plt.grid(True)
plt.show()
