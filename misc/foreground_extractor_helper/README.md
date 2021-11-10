# Foreground Extractor Helper
This code is meant to be run at the computer running the machine learning silhouette / foreground extractor.
It will take a directory as input and run the python command for each of the files in the directory. This is to avoid repetetive work. 


## Usage
Minimal example: 
```
python foreground_extractor.py -d final_2/
```

To see all the options:
```
python foreground_extractor.py -h
```

This will give: 
```
usage: foreground_extractor.py [-h] -d DIRECTORY

Run the foreground extractor python command on an entire directory and not just a single file

optional arguments:
  -h, --help            show this help message and exit
  -d DIRECTORY, --directory DIRECTORY
                        the directory containing the video files
```

| Argument    | Default value |
|-------------|---------------|
| desitnation | none          |

Full example: 
```
python foreground_extractor.py -d final_2/
``` 