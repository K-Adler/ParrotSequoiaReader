# -*- coding: utf-8 -*-
"""
Created on Tue Jan 23 10:56:08 2018
Script to read Exif-data from Sequoia images.
@author: Karla
"""
    
import os
import exiftool
import base64
import struct

print('Enter file output name:')
fileName = str(raw_input())    
irrFile = open(fileName+"Irr.txt","w")
    
print('Enter directory/folder of Sequoia images:')
inputPath = str(raw_input())
    
tags = []
tempTag = []
irrTag = []

#fmt = "<qHHHHfffqHHHHfffqHHHHfffqHHHHfffqHHHHfffqHHHHfffqHHHHfffqHHHHfffqHHHHfff"
fmt = "<QHHHHfffQHHHHfffQHHHHfffQHHHHfffQHHHHfffQHHHHfffQHHHHfffQHHHHfff"
    
arr = os.listdir(inputPath)
for i in range(1, len(arr)):
    with exiftool.ExifTool() as et:
        box = et.get_metadata(inputPath+arr[i])
        boxTemp = et.get_tag('XMP:SensorTemperature', inputPath+arr[i])
        boxISO = et.get_tag('EXIF:ISO', inputPath+arr[i])
        boxEXP = et.get_tag('EXIF:ShutterSpeedValue', inputPath+arr[i])
        boxIrrScale = et.get_tag('XMP:IrradianceUnitScale', inputPath+arr[i])
        boxFnumber = et.get_tag('EXIF:FNumber', inputPath+arr[i])
        
        
        Irr = et.get_tag('XMP:IrradianceList', inputPath+arr[i])
        byteIrr = base64.b64decode(Irr)
        boxIrr = struct.unpack_from(fmt, byteIrr)
        irrCountMean = (boxIrr[1]+boxIrr[9]+boxIrr[17]+boxIrr[25]+boxIrr[33]+boxIrr[41]+boxIrr[49]+boxIrr[57])/8
        irrGain = (str(boxIrr[3])+str(boxIrr[11])+str(boxIrr[19])+str(boxIrr[27])+str(boxIrr[35])+str(boxIrr[43])+str(boxIrr[51])+str(boxIrr[59]))
        
        
    tags.append(box)
    tempTag.append(boxTemp)
    
    irrTag.append(irrCountMean)
    irrFile.write(str(irrCountMean)+" "+str(boxTemp)+" "+str(boxISO)+" "+str(boxEXP)+" "+str(boxFnumber)+" "+str(boxIrrScale)+" "+str(irrGain)+"\n")
    
irrFile.close()