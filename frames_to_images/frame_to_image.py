from typing import DefaultDict
import cv2
import argparse
import os

# Add arguments for command line usage
parser = argparse.ArgumentParser(description='Convert every frame of a video file to single jpg files.')

parser.add_argument('-v', '--video', help='the directory for the video file', required=True)
parser.add_argument('-d', '--destination', help='the name of your wanted destianation folder for the images', default='result_images')
parser.add_argument('-p', '--prefix', help='the prefix of your resulting images', default='frame')

args = parser.parse_args()

# Make variables from the parser arguments
video_path = args.video
dir_path = args.destination
prefix = args.prefix

if not os.path.exists(dir_path):
    os.mkdir(dir_path)

# Opens the Video file from the parsed video file
cap= cv2.VideoCapture(video_path)

i=0

while(cap.isOpened()):
    ret, frame = cap.read()
    if ret == False:
        break
    cv2.imwrite('./'+ dir_path + '/' + prefix + '_'+str(i)+'.jpg',frame)
    i+=1
 
cap.release()
cv2.destroyAllWindows()