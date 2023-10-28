import matplotlib.pyplot as plt
import matplotlib.patches as patches

# Create a figure and axis
fig, ax = plt.subplots()

# Draw the palm of the hand
palm = patches.Circle((0, 0), 1, fill=True, color='beige')
ax.add_patch(palm)

# Draw the fingers
finger_lengths = [0.4, 0.3, 0.2, 0.1]
finger_angles = [-45, -20, 20, 45]

for length, angle in zip(finger_lengths, finger_angles):
    x = length * 1.5 * (2 ** 0.5) * (2 ** 0.5 / 2) * (2 ** 0.5 / 2)
    y = length * 1.5 * (2 ** 0.5) * (2 ** 0.5 / 2) * (2 ** 0.5 / 2)
    rotation = angle

    finger = patches.Rectangle((-x/2, 0), x, length, angle=rotation, fill=True, color='beige')
    ax.add_patch(finger)

# Set aspect ratio to be equal to make it look like a hand
ax.set_aspect('equal', 'box')

# Set axis limits and display the hand
ax.set_xlim(-1.5, 1.5)
ax.set_ylim(0, 1.5)
ax.axis('off')
plt.show()
