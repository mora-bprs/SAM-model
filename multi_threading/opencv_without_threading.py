import cv2
import time
import torch
from utils import get_device, get_model, plot_square, plot_image, annotate_square_corners, show_box, show_mask, show_points
import numpy as np
from matplotlib import pyplot as plt
from fastsam import FastSAM, FastSAMPrompt
from utils import get_box_coordinates, get_image_with_box_corners, annotate_frame_with_mask
import cv2
import threading
import time

# Configuration
fast_sam_checkpoint = "weights/FastSAM-x.pt"
fast_sam_s_checkpoint = "weights/FastSAM-s.pt"

# device = get_device()
device = "cpu"

# #######################################
# model_name = input("Enter the model name you want >>> ")
model_name = "fastSAM-s"

model = get_model(model_name)

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
    try:
      # box_corners_dict = get_box_coordinates(frame, model, device, False, False, False)
      # print(box_corners_dict)
      
      # TO PLOT THE BOX CORNERS
      # annotated_frame = get_image_with_box_corners(frame, box_corners_dict)  # in RGB
      
      # TO PLOT THE MASK 
      annotated_frame = annotate_frame_with_mask(frame, model, device, False, False, False)
      num_frames_processed += 1

      cv2.imshow('frame', annotated_frame)
      
    except ValueError:  # No box is detected
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
