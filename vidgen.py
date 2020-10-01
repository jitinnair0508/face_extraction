import cv2
import numpy as np
from glob import glob
import requests 
import os
import time

def generate_output(frame_dir):
  img_array = []
  for filename in sorted(glob(f"{frame_dir}/*.png")):
    img = cv2.imread(filename)
    height, width, layers = img.shape
    size = (width,height)
    img_array.append(img)
    
  fourcc = cv2.VideoWriter_fourcc(*'mp4v')
  out = cv2.VideoWriter('./output@10.mp4', fourcc, 1.5, size)
  
  for i in range(len(img_array)):
    out.write(img_array[i])
  out.release()

def main():
#   video_url = "/Users/admin/Documents/LAF/dataset/1.MTS"
#   get_video(video_url)

  start = time.process_time()
  #video = cv2.VideoCapture(r"C:\Users\Dell\Desktop\Implementation ARMY Mog\1.MTS")
  if not os.path.exists('./folder'):
    os.mkdir('./folder')
  #estimate_optical_flow(video, './frames2')
  generate_output('./folder')
  print("TIME TAKEN : ",time.process_time() - start)
  

#   os.remove('./frames2')



if __name__ == "__main__":
  main()