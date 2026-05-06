import numpy as np
from parallelHillClimber import PARALLEL_HILL_CLIMBER
import constants as c

numRuns = 10
robotType = "quad"  # change to "octo" on octopod branch
bestFitnesses = []
bestPHC = None
bestFitnessOverall = float('inf')
allMatrices = []

for run in range(numRuns):
    print(f"\n=== Run {run+1} of {numRuns} ===")
    phc = PARALLEL_HILL_CLIMBER()
    phc.parents[0].Start_Simulation("GUI")
    phc.Evolve(showBest=False)

    bestFitness = min(phc.parents[i].fitness for i in phc.parents)
    bestFitnesses.append(bestFitness)
    allMatrices.append(phc.fitnessMatrix)
    print(f"Best fitness this run: {bestFitness}")

    if bestFitness < bestFitnessOverall:
        bestFitnessOverall = bestFitness
        bestPHC = phc

# Stack all run matrices and save
combinedMatrix = np.concatenate(allMatrices, axis=0)  # (numRuns*p) x g
np.savetxt(robotType + "_fitness_combined.txt", combinedMatrix)
np.save(robotType + "_fitness_combined.npy", combinedMatrix)

print("\nResults:")
print(f"All best fitnesses: {bestFitnesses}")
print(f"Mean: {np.mean(bestFitnesses):.4f}")
print(f"Std Dev: {np.std(bestFitnesses):.4f}")

with open(robotType + "_results.txt", "w") as f:
    for fit in bestFitnesses:
        f.write(str(fit) + "\n")

print(f"\nShowing best robot overall (fitness: {bestFitnessOverall:.4f})")
bestPHC.Show_Best()