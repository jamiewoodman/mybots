import numpy as np
from parallelHillClimber import PARALLEL_HILL_CLIMBER

numRuns = 10
bestFitnesses = []
bestPHC = None
bestFitnessOverall = float('inf')

for run in range(numRuns):
    print(f"Run {run+1} of {numRuns}")
    phc = PARALLEL_HILL_CLIMBER()
    phc.Evolve(showBest=False)
    
    bestFitness = min(phc.parents[i].fitness for i in phc.parents)
    bestFitnesses.append(bestFitness)
    print(f"Best fitness this run: {bestFitness}")
    
    if bestFitness < bestFitnessOverall:
        bestFitnessOverall = bestFitness
        bestPHC = phc

print("\nResults:")
print(f"All best fitnesses: {bestFitnesses}")
print(f"Mean: {np.mean(bestFitnesses):.4f}")
print(f"Std Dev: {np.std(bestFitnesses):.4f}")

resultsFile = open("ab_results.txt", "w")
for f in bestFitnesses:
    resultsFile.write(str(f) + "\n")
resultsFile.close()

print(f"\nShowing best robot overall (fitness: {bestFitnessOverall:.4f})")
bestPHC.Show_Best()