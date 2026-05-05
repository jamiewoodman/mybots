import matplotlib.pyplot as plt
import numpy as np

# Load data
quadFitnesses = []
octoFitnesses = []

with open("quad_fitness_curve.txt", "r") as f:
    for line in f:
        quadFitnesses.append(float(line.strip()))

with open("octo_fitness_curve.txt", "r") as f:
    for line in f:
        octoFitnesses.append(float(line.strip()))

generations = range(len(quadFitnesses))

plt.figure(figsize=(10, 6))
plt.plot(generations, quadFitnesses, label="Quadruped", color="blue")
plt.plot(generations, octoFitnesses, label="Octopod", color="red")
plt.xlabel("Generation")
plt.ylabel("Best Fitness")
plt.title("Fitness Over Generations: Quadruped vs Octopod")
plt.legend()
plt.grid(True)
plt.savefig("fitness_curve.png")
plt.show()