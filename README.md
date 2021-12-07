<h1 align="center">
  Measuring the Quality of a<br>
  Machine Learning Based Silhouette Extractor
</h1>

<h4 align="center">TFE4940<br>Electronic Systems Design and Innovation, Master Thesis</h4>

<p align="center">
  <a href="#description">Description</a> •
  <a href="#installation">Installation</a> •
  <a href="#more-info">More Info</a> •
  <a href="#contributors">Contributors</a>
</p>

This repository contains the master thesis done by Peter Remøy Paulsen, the fall of 2021, as the final part of his masters degree in electronic systems design and innovation. 

In this thesis, we took a deeper look into the quality of the machine learning based foreground extractor used for the [AdMiRe project](http://www.admire3d.eu/).
The AdMiRe project aims to create engaging television by
> developing, validating and demonstrating innovative solutions based on mixed reality technology. These solutions will enable audiences at home to be incorporated into the live TV programme they are watching and to interact with people in the TV studio. They will also provide content creators with tools that radically improve talent immersion and interaction with computer-generated elements.

To evaluate the quality of the machine learning based foreground extractor, we set up some objective and subjective measures, and took a look at if there was any correlation between these two types of measures

[Complete report can be found here.](https://github.com/petrepa/TFE4940/blob/master/TFE4940_peterrp_final_report.pdf)

[A TL;DR version of the report can be found here.](https://github.com/petrepa/TFE4940/wiki/Report-TL;DR)

## Description
We built a set of videos by combining a constructed foreground video, using green screen, with some background videos. The machine learning based foreground extractor then processed the resulting video. 

The videos was then rated objectively using typical measures for image semantic segmentation.
For the subjective measures, a group of participants rated the videos giving their opinions.


## Installation

#### Git Clone
**HTTPS**:
```
git clone https://github.com/petrepa/TFE4940.git
```
or **SSH**:
```
git clone git@github.com:petrepa/TFE4940.git
```


## More info
Can be found in the [Wiki](https://github.com/petrepa/TFE4940/wiki)

## Contributors
* Researcher and Developer: [Peter Remøy Paulsen](https://github.com/petrepa) 👨‍🎓
* Supervisor: [Jordi Puig](https://www.ntnu.no/ansatte/jordi.puig)👨‍🔬
    * Overseeing supervisor: [Andrew Perkis](https://www.ntnu.edu/employees/andrew.perkis) 👨‍🏫
