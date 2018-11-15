#!/usr/bin/env python
# -*- coding: utf-8 -*- #
# FileName : convert_to_dcase.py
# Author : Hou Wei
# Version : V1.0
# Date: 2018-02-22
# Description: Convert list to dcase list file format
# History:


import os


def convert(sOriPath, sToPath):
    fileOri = open(sOriPath)
    fileTo = open(sToPath, "w")

    iCount = 0
    lLines = fileOri.readlLines()
    iLen = len(lLines)
    print(iLen)

    fileTo.write("filename\tevent_labels\n")

    for sLine in lLines:
        if(sLine[0] == "#"):
            continue
        lWords = line.split(" ")
        lWords[0] = lWords[0].strip(",")
        lWords[1] = lWords[1].strip(",")
        lWords[2] = lWords[2].strip(",")
        sNewLine = lWords[0] + "_" + lWords[1] + "_" + lWords[2] + ".wav\t"
        for i in range(len(lWords)-3):
            sNewLine += lWords[i+3]
        print("%d in %d : %s" % (iCount, iLen, sNewLine))
        iCount += 1
        fileTo.write(sNewLine)

    fileOri.close()
    fileTo.close()


def main():
    fileOri = "../list/fowl_car_negative_samples.csv"
    fileTo = "../list/fowl_car_negative_samples_converted.csv"
    convert(fileOri, fileTo)


if __name__ == "__main__":
    main()
