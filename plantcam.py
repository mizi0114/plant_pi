from picamera2 import Picamera2, Preview
import time
import os 
from datetime import datetime, timedelta

plantpic_folder = "<YOUR DIRECTORY PATH HERE>"
file_name = "plantpic_"
date_now = datetime.now()
date_str = date_now.strftime("%Y-%m-%d")
file_extension = ".jpg"

def plant_pi_cam():
     picam2 = Picamera2()
     camera_config = picam2.create_still_configuration(main={"size": (1920, 1080)})
     picam2.configure(camera_config)
     picam2.start()
     picam2.capture_file(f"{plantpic_folder}{file_name}{date_str}{file_extension}")

plant_pi_cam()