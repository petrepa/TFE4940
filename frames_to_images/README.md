# Frame to Image
This is a Python code which lets you convert every frame of a video file to a single jpg files from the command line.

## Usage
Minimal example: 
```
python3 frame_to_image.py -v ./video/chroma_key_test.mov
```

To see all the options:
```
python3 frame_to_image.py -h
```

This will give: 
```
usage: frame_to_image.py [-h] -v VIDEO [-d DESTINATION] [-p PREFIX]

Convert every frame of a video file to single jpg files.

optional arguments:
  -h, --help            show this help message and exit
  -v VIDEO, --video VIDEO
                        the directory for the video file
  -d DESTINATION, --destination DESTINATION
                        the name of your wanted destianation folder for the images
  -p PREFIX, --prefix PREFIX
                        the prefix of your resulting images
```

| Argument    | Default value |
|-------------|---------------|
| video       | none          |
| destination |'result_images'|
| prefix      |'frame'        |

Full example: 
```
python3 frame_to_image.py -v ./video/chroma_key_test.mov -d test_mappe -p test_prefix
``` 