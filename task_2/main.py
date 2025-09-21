from task_2.pythagoras_tree import plt, draw_tree, math

def main():
    level = int(input("Enter recusion depth (e. g., 10): "))
    
    plt.figure(figsize=(8, 8))
    # Initial branch: from bottom to top
    draw_tree(0, -300, 200, math.pi/2, level)
    
    plt.axis("off")
    plt.show()

if __name__ == "__main__":
    main()