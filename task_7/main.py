from task_7.monte_carlo import monte_carlo_simulation, analytic_probabilities, compare
from task_7.utils import print_table, plot_probabilities

def main():
    num_trials = 100000
    mc_probs = monte_carlo_simulation(num_trials)
    
    print("Monte Carlo simulation results:")
    print_table(mc_probs)
    plot_probabilities(mc_probs, f"Monte Carlo Method: {num_trials} rolls")
    
    analytic_probs = analytic_probabilities()
    print("\nComparison with analytical probabilities:")
    compare(mc_probs, analytic_probs)

if __name__ == "__main__":
    main()
