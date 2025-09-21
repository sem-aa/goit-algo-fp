import matplotlib.pyplot as plt
import math

def draw_tree(x, y, length, angle, level):
    if level == 0:
        return
    
    # End of the current branch
    x2 = x + length * math.cos(angle)
    y2 = y + length * math.sin(angle)
    
    # Draw the branch
    plt.plot([x, x2], [y, y2], color="green", linewidth=1)
    
    # Recursively draw two new branches
    new_length = length * 0.7   # reduction coefficient
    draw_tree(x2, y2, new_length, angle + math.pi / 4, level - 1)  # left branch
    draw_tree(x2, y2, new_length, angle - math.pi / 4, level - 1)  # right branch


def main():
    level = int(input("Enter recusion depth (e. g., 10): "))
    
    plt.figure(figsize=(8, 8))
    # Initial branch: from bottom to top
    draw_tree(0, -300, 200, math.pi/2, level)
    
    plt.axis("off")
    plt.show()

if __name__ == "__main__":
    main()
