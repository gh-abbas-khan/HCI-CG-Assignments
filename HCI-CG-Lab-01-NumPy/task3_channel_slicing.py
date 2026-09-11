import os
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image

script_folder = os.path.dirname(os.path.abspath(__file__))
image_path = os.path.join(script_folder, "sample.jpg")

if not os.path.exists(image_path):
    print(f"Error: '{image_path}' was not found.")
    print("Place sample.jpg in the same folder as this Python file.")
    raise SystemExit

img = np.array(Image.open(image_path).convert("RGB"))

# Extract 2D color-channel intensity grids
red_channel = img[:, :, 0]
green_channel = img[:, :, 1]
blue_channel = img[:, :, 2]

# Create RGB arrays containing only one active channel
red_only = np.zeros_like(img)
green_only = np.zeros_like(img)
blue_only = np.zeros_like(img)

red_only[:, :, 0] = red_channel
green_only[:, :, 1] = green_channel
blue_only[:, :, 2] = blue_channel

print("--- CHANNEL EXTRACTION SUMMARY ---")
print(f"Original Image Shape     : {img.shape}")
print(
    f"Red Channel 2D Shape     : {red_channel.shape} | "
    f"Mean Intensity: {red_channel.mean():.2f}"
)
print(
    f"Green Channel 2D Shape   : {green_channel.shape} | "
    f"Mean Intensity: {green_channel.mean():.2f}"
)
print(
    f"Blue Channel 2D Shape    : {blue_channel.shape} | "
    f"Mean Intensity: {blue_channel.mean():.2f}"
)

fig, axes = plt.subplots(2, 3, figsize=(15, 9))

# Top row: individual color images
axes[0, 0].imshow(red_only)
axes[0, 0].set_title("Red-Only Image")
axes[0, 0].axis("off")

axes[0, 1].imshow(green_only)
axes[0, 1].set_title("Green-Only Image")
axes[0, 1].axis("off")

axes[0, 2].imshow(blue_only)
axes[0, 2].set_title("Blue-Only Image")
axes[0, 2].axis("off")

# Bottom row: grayscale channel intensity maps
axes[1, 0].imshow(red_channel, cmap="gray")
axes[1, 0].set_title("Red Channel Intensity")
axes[1, 0].axis("off")

axes[1, 1].imshow(green_channel, cmap="gray")
axes[1, 1].set_title("Green Channel Intensity")
axes[1, 1].axis("off")

axes[1, 2].imshow(blue_channel, cmap="gray")
axes[1, 2].set_title("Blue Channel Intensity")
axes[1, 2].axis("off")

plt.tight_layout()
plt.savefig("task3_channel_slicing.png", dpi=200)
plt.show()