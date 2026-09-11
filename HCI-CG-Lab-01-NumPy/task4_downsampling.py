import os
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image

image_path = "sample.jpg"
N = 8

if not os.path.exists(image_path):
    print(f"Error: '{image_path}' was not found.")
    print("Place sample.jpg in the same folder as this Python file.")
    raise SystemExit

img = np.array(Image.open(image_path).convert("RGB"))

original_height, original_width, channels = img.shape

# Take every N-th pixel from rows and columns
downsampled = img[::N, ::N, :]

# Expand pixels to create the blocky/pixelated image
expanded = np.repeat(np.repeat(downsampled, N, axis=0), N, axis=1)

# Crop in case dimensions are not perfectly divisible by N
expanded = expanded[:original_height, :original_width, :]

height_reduction = (1 - downsampled.shape[0] / original_height) * 100
width_reduction = (1 - downsampled.shape[1] / original_width) * 100
memory_savings = (1 - downsampled.nbytes / img.nbytes) * 100

print(f"--- DOWNSAMPLING ANALYSIS (N = {N}) ---")
print(f"Original Shape     : {img.shape} | Memory: {img.nbytes:,} bytes")
print(
    f"Downsampled Shape  : {downsampled.shape} | "
    f"Memory: {downsampled.nbytes:,} bytes"
)
print(f"Re-expanded Shape  : {expanded.shape} | Visual: Blocky Pixelation")
print(
    f"Dimension Reduction: {height_reduction:.2f}% height reduction, "
    f"{width_reduction:.2f}% width reduction"
)
print(f"Memory Savings     : {memory_savings:.2f}% data reduction")

fig, axes = plt.subplots(1, 3, figsize=(18, 6))

axes[0].imshow(img)
axes[0].set_title(f"Original Image\n{img.shape}")
axes[0].axis("off")

axes[1].imshow(downsampled)
axes[1].set_title(f"Downsampled Image (N={N})\n{downsampled.shape}")
axes[1].axis("off")

axes[2].imshow(expanded)
axes[2].set_title(f"Re-expanded / Pixelated\n{expanded.shape}")
axes[2].axis("off")

plt.tight_layout()
plt.savefig("task4_downsampling_pixelation.png", dpi=200)
plt.show()