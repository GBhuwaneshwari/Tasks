import cv2
# Load the image
image = cv2.imread('image2.jpg')

# Display the image
cv2.imshow('Original Image', image)
cv2.waitKey(0)

# Convert to grayscale
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Apply Gaussian Blur
blurred = cv2.GaussianBlur(gray, (5, 5), 0)

# Detect edges using Canny edge detector
edges = cv2.Canny(blurred, 50, 150)

# Find contours
contours, _ = cv2.findContours(edges, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

# Draw contours on the original image
cv2.drawContours(image, contours, -1, (0, 255, 0), 3)

# Display the result
cv2.imshow('Contour Detection', image)
cv2.waitKey(0)

# Close all windows
cv2.destroyAllWindows()
