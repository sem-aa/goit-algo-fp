import random
from collections import Counter

def monte_carlo_simulation(num_trials=100000):
    """Simulate rolling two dice using the Monte Carlo method."""
    sums = [random.randint(1,6) + random.randint(1,6) for _ in range(num_trials)]
    counts = Counter(sums)
    probabilities = {s: count/num_trials for s, count in counts.items()}
    return probabilities

def analytic_probabilities():
    """Return the analytical probabilities of sums for two dice."""
    return {2:1/36, 3:2/36, 4:3/36, 5:4/36, 6:5/36,
            7:6/36, 8:5/36, 9:4/36, 10:3/36, 11:2/36, 12:1/36}

def compare(mc_probs, analytic_probs):
    """Compare Monte Carlo probabilities with analytical ones."""
    print("Sum | Monte-Carlo | Analytical")
    for s in range(2,13):
        mc = mc_probs.get(s,0)
        an = analytic_probs[s]
        print(f"{s:>4}  | {mc:.4f}      | {an:.4f}")
