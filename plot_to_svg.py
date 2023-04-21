import sqlite3
import matplotlib.pyplot as plt

# Connect to the database
conn = sqlite3.connect('github_stats.db')
c = conn.cursor()

# Retrieve the data from the database
c.execute("SELECT datetime, stars, forks FROM stats")
data = c.fetchall()

# Extract the stars and forks from the data
stars = [row[1] for row in data]
forks = [row[2] for row in data]

# Create a list of integers for the x-axis labels
x_labels = list(range(1, len(stars) + 1))

# Create a figure with two y-axes
fig, ax1 = plt.subplots()
ax2 = ax1.twinx()

# Plot the stars on the first y-axis
ax1.plot(x_labels, stars, color='tab:blue', label='Stars')
ax1.set_ylabel('Stars', color='tab:blue')
ax1.tick_params(axis='y', labelcolor='tab:blue')

# Plot the forks on the second y-axis
ax2.plot(x_labels, forks, color='tab:orange', label='Forks')
ax2.set_ylabel('Forks', color='tab:orange')
ax2.tick_params(axis='y', labelcolor='tab:orange')

# Set the x-axis labels and title
# plt.xticks(x_labels)
plt.xlabel('Time')
plt.title('Stars and Forks of Auto-GPT over time')

# Add a legend to the plot
lines, labels = ax1.get_legend_handles_labels()
lines2, labels2 = ax2.get_legend_handles_labels()
ax2.legend(lines + lines2, labels + labels2, loc='best')

# Save the plot as an svg file
plt.savefig('stars.svg')
