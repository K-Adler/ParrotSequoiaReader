# ParrotSeqoiaReader
Script for reading Parrot Sequoia EXIF and XMP data from the raw .TIFF images.

This script is coded in Python 2.7 and uses the wonderful exiftool provided by Phil Harvey (https://www.sno.phy.queensu.ca/~phil/exiftool/).
The script requires that you have exiftool installed on your computer as an .EXE file downloadable from the link above and with an accesible path so it can be accessed by the script. Further you need a python module in order to communicate with the exiftool .EXE which is provided by the excellent script from https://github.com/smarnach/pyexiftool.

At this given moment there are 2 scripts available for download. First there is the "ExifRead.py" which prompts you to input image directory path and output .txt file output name. The output you will get will be Base64 decoded sunshine sensor data as in the digital count value and its gain. Further you will recieve data on shutterspeed, aperture and ISO.
The second script "ImageReader.py" will use the same input parameters as the script described above but will present you with image statistics rather than sunshine and camera readings. The image statistics are mean image digital value, median image digital value, dark current value and percentage of pixels classified as statistical outliers (In order to know the total amount of noise in the image).

These scripts are a working product at the moment and are subject to changes due to them being benificial for my master thesis project. I figured to release them here as there is a lot of confusion on the Parrot Sequoia forum on how to decode the EXIF and XMP data in a meaningful way.

NOTE: A full description syllabus of the readings and data will be provded shortly.


License

This script is free of use and is merely a merger of the tool by Phil Harvey and the PyExifTool module from smarnach for use with the Parrot Sequoia camera.
