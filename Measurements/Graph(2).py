#This code produces the bar graph for the measurements lab
import matplotlib.pyplot as plt

# Trial data
trials = ["Trial 1", "Trial 2", "Trial 3", "Trial 4", "Trial 5"]

volumes = [10.05, 20.01, 30.00, 40.02, 50.00]
masses = [10.178, 19.538, 29.473, 39.246, 49.284]

# Calculate density for each trial
densities = [mass / volume for mass, volume in zip(masses, volumes)]

# Calculate average experimental density
average_density = sum(densities) / len(densities)

# Accepted/true density of water at 22.9 °C
true_density = 0.9976

# Create bar graph
plt.figure(figsize=(10, 6))

bars = plt.bar(
    trials,
    densities,
    color=["#4C78A8", "#59A14F", "#F28E2B", "#E15759", "#B279A2"],
    edgecolor="black"
)

# Average density line
plt.axhline(
    average_density,
    color="blue",
    linestyle="--",
    linewidth=2,
    label=f"Average Density = {average_density:.4f} g/mL"
)

# True density line
plt.axhline(
    true_density,
    color="red",
    linestyle="--",
    linewidth=2,
    label=f"True Density = {true_density:.4f} g/mL"
)

# Add density values above each bar
for bar, density in zip(bars, densities):
    plt.text(
        bar.get_x() + bar.get_width() / 2,
        bar.get_height() + 0.002,
        f"{density:.4f}",
        ha="center",
        va="bottom",
        fontsize=10
    )

# Labels and title
plt.title("Density of Water at 22.9 °C Obtained with a Graduated Cylinder", fontsize=16, fontweight="bold")
plt.xlabel("Trial", fontsize=12)
plt.ylabel("Density (g/mL)", fontsize=12)

# Set y-axis range so the differences are easier to see
plt.ylim(0.95, 1.03)

# Add grid
plt.grid(axis="y", linestyle=":", alpha=0.5)

# Legend
plt.legend()

plt.tight_layout()
plt.show()
