#This code produces the bar graph for the measurements lab
import matplotlib.pyplot as plt

# Trial data
trials = ["Trial 1", "Trial 2", "Trial 3", "Trial 4", "Trial 5"]

volumes = [10.00, 20.00, 30.00, 40.00, 50.00]
masses = [10.183, 19.853, 29.793, 39.677, 49.605]

# Calculate density for each trial
densities = [mass / volume for mass, volume in zip(masses, volumes)]

# Calculate average density
average_density = sum(densities) / len(densities)

# True density of water at 23.0 °C
true_density = 0.9975

# Create the bar graph
plt.figure(figsize=(10, 6))

bars = plt.bar(
    trials,
    densities,
    color=["#4C78A8", "#59A14F", "#F28E2B", "#E15759", "#B279A2"],
    edgecolor="black"
)

# Add average density line
plt.axhline(
    average_density,
    color="blue",
    linestyle="--",
    linewidth=2,
    label=f"Average Density = {average_density:.4f} g/mL"
)

# Add true density line
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
        bar.get_height() + 0.001,
        f"{density:.4f}",
        ha="center",
        va="bottom",
        fontsize=10
    )

# Title and axis labels
plt.title(
    "Density of Water at 23.0 °C Obtained with a Volumetric Pipette",
    fontsize=16,
    fontweight="bold"
)

plt.xlabel("Trial", fontsize=12)
plt.ylabel("Density (g/mL)", fontsize=12)

# Make the differences visible
plt.ylim(0.98, 1.025)

# Grid
plt.grid(axis="y", linestyle=":", alpha=0.5)

# Legend
plt.legend()

plt.tight_layout()
plt.show()

