import cv2
import numpy as np
import argparse
import sys
import csv
import os
from rich.console import Console

console = Console()


np.set_printoptions(threshold=sys.maxsize)


# Add arguments for command line usage
parser = argparse.ArgumentParser(description='Convert a black and white image to a numerical array (black = 0 and white = 1).')

parser.add_argument('-i', '--input', help='the image file', required=True)
parser.add_argument('-t', '--truth', help='the truth table image file', required=False)
parser.add_argument('-d', '--destination', help='the directory where the binary black and white images from the input will be saved', required=False)

args = parser.parse_args()

# Make variables from the parser arguments
img_path = args.input
truth_path = args.truth
dest_path = args.destination

def get_filename():
    #return the filename of the image
    filename_long = str(img_path).rpartition('/')
    return filename_long[2]

def image_to_numerical(image):
    img = cv2.imread(image, 0) # read image as grayscale. Set second parameter to 1 if rgb is required 
    print('Ran image_to_numerical on image "%s"' % (image))
    
    #convert the grayscale image to a binary black and white image
    (thresh, blackAndWhiteImage) = cv2.threshold(img, 0, 255, cv2.THRESH_BINARY)

    return(blackAndWhiteImage)

def save_image(image):
    img = cv2.imread(image, 0) # read image as grayscale. Set second parameter to 1 if rgb is required 
    print('Ran funciton on image "%s"' % (image))
    
    #convert the grayscale image to a binary black and white image
    (thresh, blackAndWhiteImage) = cv2.threshold(img, 0, 255, cv2.THRESH_BINARY)

    #save the image
    filename_long = str(image).rpartition('/')
    filename = dest_path + '/' + filename_long[2]

    cv2.imwrite(filename, blackAndWhiteImage)
    print("Filename: " + filename)
    return filename_long[2]



def intersection_over_union(array1, array2):
    try:
        intersection = np.logical_and(array1, array2)
        union = np.logical_or(array1, array2)
        iou_score = np.sum(intersection) / np.sum(union)

        return iou_score
    except:
        console.print('!! intersection_over_union function failed !!','\n\nAre you sure the images have the identical size?', style="bold red")

def dice_coeff(array1, array2):
    J = intersection_over_union(array1, array2)
    S = (2 * J)/(1+J)

    #print('Dice Coefficient is %s' % (S))
    
    return S

def pixel_accuracy(array1, array2):
    try:
        i = 0

        TP = np.sum(np.logical_and(array1, array2))
        TN = np.sum(np.logical_not(np.logical_or(array1, array2)))
        FPN = np.sum(np.logical_xor(array1, array2))
        TPN = np.sum(np.logical_not(np.logical_xor(array1, array2)))

        accuracy = (TP + TN)/(TP + TN + FPN)

        return TP, TN, FPN, accuracy, TPN
    except:
        console.print('!! pixel_accuracy function failed !!','\n\nAre you sure the images have the identical size?', style="bold red")


def write_to_csv():
    row_value = main()
    csv_filename = get_filename()
    #complete filename of csv file with file type ending
    csv_fn = str(csv_filename).strip('.jpg') + '.csv'

    # if the csv file doesn't already exist, make it and write the header
    if not os.path.isfile(csv_fn):
        with open(csv_fn, 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(['filename','Iou','DC','PA','TP','TN','FPN'])

    # append the new data to the file
    with open(csv_fn, 'a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(row_value)

def main():
    img_array = image_to_numerical(img_path)

    if args.truth is not None:
        truth_array = image_to_numerical(truth_path)

    IoU = intersection_over_union(img_array, truth_array)
    print('IoU is %s' % (IoU))

    DC = dice_coeff(img_array, truth_array)
    print('DC is %s' % (DC))

    TP, TN, FPN, PA, TPN = pixel_accuracy(img_array, truth_array)
    print('PA: %s - TP is %s, TN is %s, FPN is %s, TPN is %s, TP + TN is %s' % (PA, TP, TN, FPN, TPN, (TP+TN)))

    filename = save_image(img_path)

    return filename, IoU, DC, PA, TP, TN, FPN

write_to_csv()


