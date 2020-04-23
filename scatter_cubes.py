import matplotlib.pyplot as plt

x_values = range(1, 5001)
y_values = [x**3 for x in x_values]

plt.style.use('seaborn')
fig, ax = plt.subplots()
ax.scatter(x_values, y_values, c='red', s=10)

# Set titles and label Axis'
ax.set_title("Cubed numbers", fontsize=24)
ax.set_xlabel("Value", fontsize=14)
ax.set_ylabel("Cube of Value", fontsize=14)

# Set the range for each axis.
ax.axis([0, 5000, 0, 5100])

# # Tick parameters
# ax.tick_params(axis='both', labelsize=14)

plt.show()