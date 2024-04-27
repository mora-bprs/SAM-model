import cv2
import time

# Define the camera index
camera_index = 1

# Opening video capture stream
vcap = cv2.VideoCapture(camera_index)
if not vcap.isOpened():
    print("[Exiting]: Error accessing webcam stream.")
    exit(0)

fps_input_stream = int(vcap.get(cv2.CAP_PROP_FPS))
print("FPS of webcam hardware/input stream:", fps_input_stream)

# Reading single frame for initialization/hardware warm-up
grabbed, frame = vcap.read()

# Processing frames in input stream
num_frames_processed = 0
start = time.time()

while True:
    grabbed, frame = vcap.read()
    if not grabbed:
        print('[Exiting] No more frames to read')
        break

    # Adding a delay for simulating time taken for processing a frame
    delay = 0.03  # Delay value in seconds
    time.sleep(delay)
    num_frames_processed += 1

    cv2.imshow('frame', frame)
    key = cv2.waitKey(1)
    if key == ord('q'):
        break

end = time.time()

# Printing time elapsed and FPS
elapsed = end - start
fps = num_frames_processed / elapsed
print("FPS:", fps, ", Elapsed Time:", elapsed, ", Frames Processed:", num_frames_processed)

# Releasing input stream, closing all windows
vcap.release()
cv2.destroyAllWindows()
