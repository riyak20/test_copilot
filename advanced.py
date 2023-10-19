import matplotlib.pyplot as plt

# Sample data
x = [1, 2, 3, 4, 5]
y = [2, 4, 6, 8, 10]

# Create a figure and axis object
fig, ax = plt.subplots()

# Plot the data
ax.plot(x, y)

# Set the axis labels and title
ax.set_xlabel('X-axis')
ax.set_ylabel('Y-axis')
ax.set_title('My Graph')

# Show the graph
plt.show()