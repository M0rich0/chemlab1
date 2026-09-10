#This code produces the bar graph for the measurements lab
import matplotlib.pyplot as plt

# Data from the five trials
trials = ["Trial 1", "Trial 2", "Trial 3", "Trial 4", "Trial 5"]

volumes = [10.05, 20.01, 30.00, 40.02, 50.00]
masses = [54.370, 63.730, 73.665, 83.438, 93.476]

# Calculate density for each trial
densities = [mass / volume for mass, volume in zip(masses, volumes)]

# Calculate experimental average density
average_density = sum(densities) / len(densities)

# True density of water at 22.9 °C
true_density = 0.9976

# Print the results
for trial, density in zip(trials, densities):
    print(f"{trial}: {density:.3f} g/mL")

print(f"Average density: {average_density:.3f} g/mL")
print(f"True density: {true_density:.4f} g/mL")

# Create the bar graph
plt.figure(figsize=(10, 6))

bars = plt.bar(
    trials,
    densities,
    color="skyblue",
    edgecolor="black",
    label="Experimental Density"
)

# Average density line
plt.axhline(
    average_density,
    color="red",
    linestyle="--",
    linewidth=2,
    label=f"Average = {average_density:.3f} g/mL"
)

# True density line
plt.axhline(
    true_density,
    color="green",
    linestyle="-",
    linewidth=2,
    label=f"True Density = {true_density:.4f} g/mL"
)

# Add density values above each bar
for bar, density in zip(bars, densities):
    plt.text(
        bar.get_x() + bar.get_width() / 2,
        bar.get_height() + 0.1,
        f"{density:.3f}",
        ha="center",
        fontsize=10
    )

# Labels and title
plt.xlabel("Trial")
plt.ylabel("Density (g/mL)")
plt.title("Density of Water at 22.9 °C Obtained with a Graduated Cylinder")

plt.ylim(0, 6)
plt.grid(axis="y", linestyle="--", alpha=0.4)
plt.legend()

plt.tight_layout()
plt.show()
