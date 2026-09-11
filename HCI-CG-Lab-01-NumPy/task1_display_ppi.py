import math


def get_positive_int(prompt):
    while True:
        try:
            value = int(input(prompt))
            if value > 0:
                return value
            print("Please enter a positive whole number.")
        except ValueError:
            print("Invalid input. Please enter a whole number.")


def get_positive_float(prompt):
    while True:
        try:
            value = float(input(prompt))
            if value > 0:
                return value
            print("Please enter a value greater than zero.")
        except ValueError:
            print("Invalid input. Please enter a numeric value.")


width_px = get_positive_int("Enter horizontal resolution (pixels): ")
height_px = get_positive_int("Enter vertical resolution (pixels): ")
diagonal_inches = get_positive_float("Enter physical diagonal size (inches): ")

total_pixels = width_px * height_px
gcd_value = math.gcd(width_px, height_px)
aspect_width = width_px // gcd_value
aspect_height = height_px // gcd_value

diagonal_pixels = math.sqrt(width_px ** 2 + height_px ** 2)
ppi = diagonal_pixels / diagonal_inches

if ppi < 100:
    category = "Low Density (Standard Monitor)"
elif ppi <= 200:
    category = "Medium Density (HD Display)"
else:
    category = "High Density (Retina / Mobile)"

print("\n--- DISPLAY METRICS ANALYSIS ---")
print(f"Total Pixel Count : {total_pixels:,} pixels")
print(f"Aspect Ratio      : {aspect_width}:{aspect_height}")
print(f"Calculated DPI    : {ppi:.2f} DPI")
print(f"Density Category  : {category}")