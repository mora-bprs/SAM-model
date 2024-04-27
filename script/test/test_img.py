import cv2

# Define the image path
image_path = "box_train/train/box_42.jpg"

# Read the image
image = cv2.imread(image_path)
print(type(image))

# Check if the image was successfully loaded
if image is not None:
    # Display the image
    cv2.imshow("Image", image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
else:
    print("Error: Unable to load image from the given path.")
