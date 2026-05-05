import numpy as np
import matplotlib.pyplot as plt
from parallelHillClimber import PARALLEL_HILL_CLIMBER
import constants as c

numRuns = 10
bestFitnesses = []
bestPHC = None
bestFitnessOverall = float('inf')
allFitnessCurves = []

for run in range(numRuns):
    print(f"Run {run+1} of {numRuns}")
    phc = PARALLEL_HILL_CLIMBER()
    
    # Evaluate parents first so fitness exists
    phc.Evaluate(phc.parents)
    
    # record random robot fitness before evolution
    if run == 0:
        randomFitness = min(phc.parents[i].fitness for i in phc.parents)
        print(f"Random robot fitness: {randomFitness}")
    
    # Now evolve (skip the initial Evaluate inside Evolve)
    for currentGeneration in range(c.numberOfGenerations):
        phc.Evolve_For_One_Generation()
    phc.Show_Best() if False else None  # suppress GUI
    
    bestFitness = min(phc.parents[i].fitness for i in phc.parents)
    bestFitnesses.append(bestFitness)
    allFitnessCurves.append(phc.fitnessOverGenerations)
    print(f"Best fitness this run: {bestFitness}")
    
    if bestFitness < bestFitnessOverall:
        bestFitnessOverall = bestFitness
        bestPHC = phc

# Save average fitness curve
avgCurve = np.mean(allFitnessCurves, axis=0)
robotType = "quad"  # change to "octo" on octopod branch
with open(f"{robotType}_fitness_curve.txt", "w") as f:
    for val in avgCurve:
        f.write(str(val) + "\n")

# Save results
print("\nResults:")
print(f"All best fitnesses: {bestFitnesses}")
print(f"Mean: {np.mean(bestFitnesses):.4f}")
print(f"Std Dev: {np.std(bestFitnesses):.4f}")

with open(f"{robotType}_results.txt", "w") as f:
    for fit in bestFitnesses:
        f.write(str(fit) + "\n")

print(f"\nShowing best robot overall (fitness: {bestFitnessOverall:.4f})")
bestPHC.Show_Best()