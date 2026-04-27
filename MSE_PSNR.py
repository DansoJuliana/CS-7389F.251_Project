import cv2
import numpy as np
import math

def calculate_mse(img1, img2):
    err = np.mean((img1 - img2) ** 2)
    return err

def calculate_psnr(img1, img2):
    mse = calculate_mse(img1, img2)
    if mse == 0:
        return float('inf')  # identical images
    PIXEL_MAX = 255.0
    psnr = 20 * math.log10(PIXEL_MAX / math.sqrt(mse))
    return psnr


for i in range(1, 10):
    original_path = f"images/in{i}.png"
    stego_path = f"images/out{i}.png"

    original = cv2.imread(original_path)
    stego = cv2.imread(stego_path)

    if original is None or stego is None:
        print(f"Skipping Image {i} (missing file)")
        continue

    mse = calculate_mse(original, stego)
    psnr = calculate_psnr(original, stego)

    print(f"\nImage {i}:")
    print(f"MSE  = {mse:.4f}")
    print(f"PSNR = {psnr:.4f} dB")