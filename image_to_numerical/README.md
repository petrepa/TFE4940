# Image to Numerical
This is a Python code which does the numerical analysis on the two identical sized images.
Does the following:
* Calculates a numerical array from the images provided 
* Calculates the objective measures between the images:
    * Intersection over Union

### TODO
* Calculates the objective measures between the images:
    * Pixel Accuracy
    * Dice Coefficient

## Usage
Minimal example: 
```
python3 image_to_numerical.py -v ./video/chroma_key_test.mov
```

To see all the options:
```
python3 image_to_numerical.py -h
```

This will give: 
```
usage: image_to_numerical.py [-h] -i INPUT [-t TRUTH]

Convert a black and white image to a numerical array (black = 0 and white = 1).

optional arguments:
  -h, --help            show this help message and exit
  -i INPUT, --input INPUT
                        the image file
  -t TRUTH, --truth TRUTH
                        the truth table image file
```

| Argument    | Default value |
|-------------|---------------|
| input       | none          |
| truth       | none          |

Full example: 
```
python3 image_to_numerical.py -i ../color_to_white/test_results/result_2.jpg -t ../color_to_white/test_results/result_1.jpg
``` 