import matplotlib.pyplot as plt

input_values = [1, 2, 3, 4, 5]
cubes = [1, 8, 27, 64, 125]

plt.style.use('seaborn')
fig, ax = plt.subplots()
ax.plot(input_values, cubes, linewidth=5)

# Set titles and label Axis'
ax.set_title("Cubed numbers", fontsize=24)
ax.set_xlabel("Value", fontsize=14)
ax.set_ylabel("Cube of Value", fontsize=14)

# Tick parameters
ax.tick_params(axis='both', labelsize=14)

plt.show()