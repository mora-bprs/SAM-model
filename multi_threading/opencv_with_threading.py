import cv2
import time
from threading import Thread

class WebcamStream:
    def __init__(self, stream_id=0):
        self.stream_id = stream_id
        self.vcap = cv2.VideoCapture(self.stream_id)
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
camera_index = 1

webcam_stream = WebcamStream(stream_id=camera_index)
webcam_stream.start()

num_frames_processed = 0 
start = time.time()

while True:
    if webcam_stream.stopped:
        break
    else:
        frame = webcam_stream.read()

    delay = 0.03
    time.sleep(delay)
    num_frames_processed += 1

    cv2.imshow('frame', frame)
    key = cv2.waitKey(1)
    if key == ord('q'):
        break

end = time.time()
webcam_stream.stop()

elapsed = end - start
fps = num_frames_processed / elapsed 
print("FPS:", fps, ", Elapsed Time:", elapsed, ", Frames Processed:", num_frames_processed)

cv2.destroyAllWindows()
