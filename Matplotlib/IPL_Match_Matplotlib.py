import matplotlib.pyplot as plt

# Define a function to calculate cumulative sums
def qsum(x):
    return [sum(x[:i]) for i in range(1, len(x) + 1)]

# Data representing IPL teams and their match results
ipl = {
    "RR": [1, 1, 1, 0, 1],
    "KKr": [1, 0, 1, 0, 1],
    "SRH": [1, 1, 1, 1, 0],
    "CSK": [0, 1, 1, 0, 0]
}

# Extract keys (team names) from the dictionary
key = list(ipl.keys())

# Extract values (match results) from the dictionary
values = list(ipl.values())

# Calculate cumulative sums for each team
cumulative_sums = [qsum(x) for x in values]

# Plot cumulative sums for each team
plt.plot(range(1, 6), cumulative_sums[0], marker="*", label="RR")  # RR
plt.plot(range(1, 6), cumulative_sums[1], marker="*", label="KKr")  # KKr
plt.plot(range(1, 6), cumulative_sums[2], marker="*", label="SRH")  # SRH
plt.plot(range(1, 6), cumulative_sums[3], marker="*", label="CSK")  # CSK

# Adjust y-axis ticks as needed
plt.yticks(range(0, 6))

# Set labels and title
plt.xlabel('Matches')
plt.ylabel('Cumulative Sum')
plt.title('Cumulative Sums of Teams')

# Display legend
plt.legend()

# Show the plot
plt.show()
