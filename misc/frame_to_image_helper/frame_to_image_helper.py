import os
import argparse

# Add arguments for command line usage
parser = argparse.ArgumentParser(description='Run the frame to image python command on an entire directory and not just a single file with correct prefixes and so on')

parser.add_argument('-d', '--directory', help='the directory containing the video files', required=True)

args = parser.parse_args()

# Make variables from the parser arguments
dir_path = args.directory


# for each of the files in the given directory, run the command
for filename in os.listdir(dir_path):
    
    if not os.path.exists('../../media/images/processed/' + str(filename).replace('.mp4','')):
        os.mkdir('../../media/images/processed/' + str(filename).replace('.mp4',''))
    
    os.system('python ../../frames_to_images/frame_to_image.py -v ' + str(dir_path) + str(filename) + ' -d ../../media/images/processed/' + str(filename).replace('.mp4','') +'/ -p ' + str(filename).replace('.mp4',''))

