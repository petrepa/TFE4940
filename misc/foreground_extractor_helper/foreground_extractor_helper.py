import os
import argparse

# Add arguments for command line usage
parser = argparse.ArgumentParser(description='Run the foreground extractor python command on an entire directory and not just a single file')

parser.add_argument('-d', '--directory', help='the directory containing the video files', required=True)

args = parser.parse_args()

# Make variables from the parser arguments
dir_path = args.directory


# for each of the files in the given directory, run the mahine learning silhouette extractor command
for filename in os.listdir(dir_path):
    os.system('python ./demo/video_matting/custom/run.py --video ' + str(dir_path) + str(filename) + ' --fps 30 --model_path ./model/weight_photographic.ckpt --result-type fg')