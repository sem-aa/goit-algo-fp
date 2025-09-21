import matplotlib.pyplot as plt

def print_table(probabilities):
    """Print a table of probabilities."""
    print("Sum | Probability")
    for s, p in sorted(probabilities.items()):
        print(f"{s:>4}  | {p:.4f}")

def plot_probabilities(probabilities, title="Sum Probabilities"):
    """Plot a bar chart of probabilities."""
    probabilities = dict(sorted(probabilities.items()))
    plt.bar(probabilities.keys(), probabilities.values(), color='skyblue')
    plt.xlabel("Sum of two dice")
    plt.ylabel("Probability")
    plt.title(title)
    plt.xticks(range(2,13))
    plt.show()
