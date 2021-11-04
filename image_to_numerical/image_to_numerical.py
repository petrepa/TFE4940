import cv2
import numpy as np
import argparse
import sys
from rich.console import Console

console = Console()


np.set_printoptions(threshold=sys.maxsize)


# Add arguments for command line usage
parser = argparse.ArgumentParser(description='Convert a black and white image to a numerical array (black = 0 and white = 1).')

parser.add_argument('-i', '--input', help='the image file', required=True)
parser.add_argument('-t', '--truth', help='the truth table image file', required=False)

args = parser.parse_args()

# Make variables from the parser arguments
img_path = args.input
truth_path = args.truth



def image_to_numerical(image):
    img = cv2.imread(image, 0) # read image as grayscale. Set second parameter to 1 if rgb is required 
    print('Ran funciton on image "%s"' % (image))
    return(img)

img_array = image_to_numerical(img_path)

if args.truth is not None:
    truth_array = image_to_numerical(truth_path)

def intersection_over_union(array1, array2):
    try:
        intersection = np.logical_and(array1, array2)
        union = np.logical_or(array1, array2)
        iou_score = np.sum(intersection) / np.sum(union)
        print('IoU is %s' % (iou_score))
    except:
        console.print('!! intersection_over_union function failed !!','\n\nAre you sure the images have the identical size?', style="bold red")

intersection_over_union(img_array, truth_array)