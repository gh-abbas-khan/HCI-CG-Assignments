import numpy as np
import matplotlib.pyplot as plt

height = 300
width = 400
channels = 3

image = np.zeros((height, width, channels), dtype=np.uint8)

mid_height = height // 2
mid_width = width // 2

# Top-left: Red
image[:mid_height, :mid_width] = [255, 0, 0]

# Top-right: Green
image[:mid_height, mid_width:] = [0, 255, 0]

# Bottom-left: Blue
image[mid_height:, :mid_width] = [0, 0, 255]

# Bottom-right: White
image[mid_height:, mid_width:] = [255, 255, 255]

print("--- SYNTHETIC MATRIX METRICS ---")
print(f"Array Shape (H, W, C) : {image.shape}")
print(f"Data Type             : {image.dtype}")
print(f"Total Elements        : {image.size:,} values")
print(f"Memory Footprint      : {image.nbytes:,} bytes ({image.nbytes / 1024:.2f} KB)")

plt.figure(figsize=(8, 6))
plt.imshow(image)
plt.title("Synthetic RGB Image: Four Color Quadrants")
plt.axis("off")
plt.tight_layout()

plt.savefig("task2_synthetic_image.png", dpi=200)
plt.show()