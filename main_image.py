import torch
from utils import get_device, get_model, plot_square, plot_image, annotate_square_corners, show_box, show_mask, show_points

import numpy as np
from matplotlib import pyplot as plt
from fastsam import FastSAM, FastSAMPrompt
from utils import get_box_coordinates, get_image_with_box_corners

# Configuration
fast_sam_checkpoint = "/content/FastSAM-x.pt"
fast_sam_s_checkpoint = "/content/FastSAM-s.pt"

# device = get_device()
device = "cpu"

# #######################################3
import cv2

print("Choose the model you want to choose")
print("""1) DeepLabv3\n2) Segnet\n3) UNet\n4) CornerNet\n5) fastSAM\n6) fastSAM-s\n7) SAM""")
# model_name = input("Enter the model name you want >>> ")
model_name = "fastSAM"

camera_index = 1
model = get_model(model_name)

# image_path = input("Enter the image path >>>")

image_path = "box_train/train/box_42.jpg"
# image_path = r"E:\Projects Archive\3_EDR-bin picking\SAM Model\box_train\train\box_104.jpg" #not fine
# image_path = "./box_train/train/box_17.jpg" # fine
  
image = cv2.imread(image_path)
image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)


print()
print("hello before ")
print()

########################## Edit below ########################################

box_corners_dict = get_box_coordinates(image, model, device, False, False, False)  # it seems like model does not care about the color format , i'm not sure, have to verify???
print()
print("hello after")

print(box_corners_dict)
print()

annotated_frame = get_image_with_box_corners(image, box_corners_dict) # in RGB 

# convert back to BGR
annotated_frame = cv2.cvtColor(annotated_frame, cv2.COLOR_RGB2BGR)
cv2.imshow("Annotated image", annotated_frame)
cv2.waitKey(0)
cv2.destroyAllWindows()