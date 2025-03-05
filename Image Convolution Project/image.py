import cv2
import numpy as np

# Load images
image_path = 'Lena.png'
image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)

# Convert to float for calculations
image_double = image.astype(np.float64)

# Define kernels
kernel1 = np.array([[0, -1, 0],
                     [-1, 5, -1],
                     [0, -1, 0]])

kernel2 = (1/24) * np.array([[1, 2, 1],
                              [3, 6, 3],
                              [1, 2, 1]])

# Edge detection
edgedetection_image = cv2.filter2D(image_double, -1, kernel1)
edgedetection_image = np.clip(edgedetection_image, 0, 255).astype(np.uint8)

# Gaussian blur
guassianblur_image = cv2.filter2D(image_double, -1, kernel2)
guassianblur_image = np.clip(guassianblur_image, 0, 255).astype(np.uint8)

# Save images
cv2.imwrite('edge_detection.png', edgedetection_image)
cv2.imwrite('gaussian_blur.png', guassianblur_image)

# Display images
cv2.imshow('Edge Detection', edgedetection_image)
cv2.imshow('Gaussian Blur', guassianblur_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
