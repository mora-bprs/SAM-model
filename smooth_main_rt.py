import cv2
import time
from threading import Thread
import torch
from utils import get_device, get_model
from utils import get_box_coordinates, get_image_with_box_corners

# Configuration
fast_sam_checkpoint = "weights/FastSAM-x.pt"
fast_sam_s_checkpoint = "weights/FastSAM-s.pt"

# device = get_device()
device = "cpu"

# #######################################
# model_name = input("Enter the model name you want >>> ")
model_name = "fastSAM-s"

model = get_model(model_name)


class WebcamStream:
    def __init__(self, stream_id=0, buffer_size=1):
        self.stream_id = stream_id
        self.buffer_size = buffer_size
        self.vcap = cv2.VideoCapture(self.stream_id)
        self.vcap.set(cv2.CAP_PROP_BUFFERSIZE, buffer_size)
        if not self.vcap.isOpened():
            print("[Exiting]: Error accessing webcam stream.")
            exit(0)
        fps_input_stream = int(self.vcap.get(cv2.CAP_PROP_FPS))
        print("FPS of webcam hardware/input stream:", fps_input_stream)
        
        self.grabbed, self.frame = self.vcap.read()
        if not self.grabbed:
            print('[Exiting] No more frames to read')
            exit(0)
            
        self.stopped = True
        self.t = Thread(target=self.update, args=())
        self.t.daemon = True
    
    def start(self):
        self.stopped = False
        self.t.start()
        
    def update(self):
        while True:
            if self.stopped:
                break
            self.grabbed, self.frame = self.vcap.read()
            if not self.grabbed:
                print('[Exiting] No more frames to read')
                self.stopped = True
                break 
        self.vcap.release()
    
    def read(self):
        return self.frame
    
    def stop(self):
        self.stopped = True

# Define the camera index
camera_index = 0

webcam_stream = WebcamStream(stream_id=camera_index, buffer_size=2)  # Set the buffer size here
webcam_stream.start()

num_frames_processed = 0 
start = time.time()

while True:
    if webcam_stream.stopped:
        break
    else:
        frame = webcam_stream.read()

    # Processing Image
    try:
        box_corners_dict = get_box_coordinates(frame, model, device, False, False, False)
        print(box_corners_dict)
        annotated_frame = get_image_with_box_corners(frame, box_corners_dict)  # in RGB
        num_frames_processed += 1

        cv2.imshow("frame", annotated_frame)
        
    except ValueError:  # No box is detected
        cv2.imshow("frame", frame)
    
    num_frames_processed += 1

    key = cv2.waitKey(1)
    if key == ord('q'):
        break

end = time.time()
webcam_stream.stop()

elapsed = end - start
fps = num_frames_processed / elapsed 
print("FPS:", fps, ", Elapsed Time:", elapsed, ", Frames Processed:", num_frames_processed)

cv2.destroyAllWindows()
