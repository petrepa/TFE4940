import os
import argparse

# Add arguments for command line usage
parser = argparse.ArgumentParser(description='Run the image to numerical python command on an entire directory and not just a single file with correct prefixes and so on')

parser.add_argument('-i', '--input', help='the directory containing the processed files which will be validated', required=True)
parser.add_argument('-t', '--truth', help='the directory containing the truth files', required=True)
parser.add_argument('-d', '--destination', help='the destination directory where the processed binary black and white images will appear', required=True)

args = parser.parse_args()

# Make variables from the parser arguments
input_path = args.input
truth_path = args.truth
dest_path = args.destination

# for each of the files in the given directory, run the command
# for filename in os.listdir(input_path):
    
#     if not os.path.exists(dest_path):
#         os.mkdir(dest_path)
    

#     os.system('python ../../image_to_numerical/image_to_numerical.py -i ' + str(input_path) + str(filename) + ' -t ' + str(input_path) + str(filename) + ' -d ' + str(dest_path))

i = 0

for filename in os.listdir(input_path):
    truth_filename = os.listdir(truth_path)
    os.system('python ../../image_to_numerical/image_to_numerical.py -i ' + str(input_path) + str(filename) + ' -t ' + str(input_path) + str(truth_filename[i]) + ' -d ' + str(dest_path))
    i += 1
