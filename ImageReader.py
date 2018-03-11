# -*- coding: utf-8 -*-
"""
Created on Tue Feb 13 17:22:20 2018

@author: Karla
"""

import os
import numpy
from PIL import Image
import exiftool

print('Enter file output name:')
ImgfileName = str(raw_input())
ImgtempFile = open(ImgfileName+"Temp.txt","w")
    
print('Enter directory/folder of Sequoia images:')
ImginputPath = str(raw_input())
    
Imgtags = []
ImgtempTag = []
    
Imgarr = os.listdir(ImginputPath)
imgSize = 1228800.0
for i in range(0, len(Imgarr)):
    with exiftool.ExifTool() as et:
        Imgbox = et.get_metadata(ImginputPath+Imgarr[i])
        ImgboxTemp = et.get_tag('XMP:SensorTemperature', ImginputPath+Imgarr[i])
        imgBlack = et.get_tag('XMP:BlackCurrent', ImginputPath+Imgarr[i])
        
    Imgtags.append(Imgbox)
    ImgtempTag.append(ImgboxTemp)
    
    im = Image.open(ImginputPath+Imgarr[i])
    imarray = (numpy.array(im))/64
    imMean = (numpy.mean(imarray))
    imMedian = (numpy.median(imarray))
    
    imQ3 = (numpy.percentile(imarray,75))
    imQ1 = (numpy.percentile(imarray,25))
    imIQR = imQ3 - imQ1
    
    imQ3out = imQ3 + (1.5*imIQR)
    imQ1out = imQ1 - (1.5*imIQR)
    
    outQ3array = imarray[numpy.where(imarray > imQ3out)]
    outQ1array = imarray[numpy.where(imarray < imQ1out)]
    
    outQ3count = outQ3array.size
    outQ1count = outQ1array.size
    
    totOutCount = outQ3count + outQ1count
    percOut = (totOutCount/imgSize)*100
    
    
    ImgtempFile.write(str(ImgboxTemp)+" "+str(imMean)+" "+str(imMedian)+" "+str(percOut)+" "+str(imgBlack)+"\n")

    
ImgtempFile.close()