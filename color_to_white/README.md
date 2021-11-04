# Color to White
This is a Python code which lets you convert any directory containing colored images and convert the colors to white. Blacks will be left alone. Nice for silhouette extracted images.

## Usage
Minimal example: 
```
python3 color_to_white.py -t ./test_images 
```

To see all the options:
```
python3 color_to_white.py -h
```

This will give: 
```
usage: color_to_white.py [-h] -t TARGET [-d DESTINATION] [-p PREFIX]

Convert a RGBs in an image to white. Leaving the black background

optional arguments:
  -h, --help            show this help message and exit
  -t TARGET, --target TARGET
                        the directory for the target image file
  -d DESTINATION, --destination DESTINATION
                        the name of your wanted destianation folder for the images
  -p PREFIX, --prefix PREFIX
                        the prefix of your resulting images
```

| Argument    | Default value |
|-------------|---------------|
| target      | none          |
| destination |'result_images'|
| prefix      |'frame'        |

Full example: 
```
python3 color_to_white.py -t ./test_images -d test_results -p result
``` 