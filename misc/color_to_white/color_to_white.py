from PIL import Image


import argparse
import os

# Add arguments for command line usage
parser = argparse.ArgumentParser(description='Convert a RGBs in an image to white. Leaving the black background')

parser.add_argument('-t', '--target', help='the directory for the target image file', required=True)
parser.add_argument('-d', '--destination', help='the name of your wanted destianation folder for the images', default='result_images')
parser.add_argument('-p', '--prefix', help='the prefix of your resulting images', default='frame')

args = parser.parse_args()

# Make variables from the parser arguments
target_path = args.target
dir_path = args.destination
prefix = args.prefix

os.mkdir(dir_path)

prefix_i=0

# go through all of the files in the target path
for filename in os.listdir(target_path):
    if filename.endswith(".jpg"): #only does the action on jpgs

        # Separate RGB arrays
        im = Image.open(target_path + '/' + filename)
        R, G, B = im.convert('RGB').split()
        r = R.load()
        g = G.load()
        b = B.load()
        w, h = im.size

        # Convert non-black pixels to white
        for i in range(w):
            for j in range(h):
                if(r[i, j] != 0 or g[i, j] != 0 or b[i, j] != 0):
                    r[i, j] = 255 # Just change R channel

        # Merge just the R channel as all channels
        im = Image.merge('RGB', (R, R, R))
        im.save('./' + dir_path + '/' + prefix + '_' + str(prefix_i) + '.jpg')
        
        prefix_i+=1