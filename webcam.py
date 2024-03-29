import cv2

def camera(index):
    # Open the default camera (usually the first one)
    cap = cv2.VideoCapture(index)

    # Check if the camera opened successfully
    if not cap.isOpened():
        print("Error: Couldn't open camera.")
        return

    while True:
        # Capture frame-by-frame
        ret, frame = cap.read()

        # If frame is read correctly ret is True
        if not ret:
            print("Error: Couldn't read frame.")
            break

        # Display the frame
        cv2.imshow('Webcam', frame)

        # Check for 'q' key press to exit the loop
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # Release the capture
    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    try:
        camera(1)
    except Exception as e:
        print(e)


