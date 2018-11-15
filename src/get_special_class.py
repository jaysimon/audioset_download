#!/usr/bin/env python
# -*- coding: utf-8 -*- #
# Copyright (C) 2018 ShenZhen Hian Speech S&T Co.,Ltd. All rights reserved.
# FileName : 10_get_special_class_in_audioset.py
# Author : Hou Wei
# Version : V1.0
# Date: 2018-10-18
# Description:To get special audio of unbalanced_train_segements.csv
# History:


import os


def Dict2List(dcDict):
    """Return key of dictionary as list
    """
    lList = []
    for key in dcDict:
        lList.append(key)
    return lList


def ContainList(lAll, dcSpec):
    """check lAll, if contains key of dcSpec, record and return
    """
    lResult = []
    lList = Dict2List(dcSpec)
    for sLine in lAll:
        if(sLine[0] != "#"):
            # print(line)
            lWords = sLine.split()
            lTmp = lWords[3].strip("\"")
            lTags = lTmp.split(",")
            # print(tags)
            lRet = list(set(lList).intersection(set(lTags)))
            for sTag in lRet:
                dcSpec[sTag] += 1
            if(len(lRet) > 0):
                print(sLine)
                lResult.append(sLine)
    return lResult, dcSpec


def main():
        # lFowlNoise = [
        #   "/m/05zppz", "/m/02zsn", "/m/0ytgt", "m/0912c9", "/t/dd00134",
        #   "/m/07swgks", "/m/0j6m2"]
        # male speech, female speech, child speech, vehicle horn,
        #   car passing by, gurgling, stream

        # fowl = [
        #    "/m/025rv6n", "/m/09b5t", "/m/07st89h", "/m/07qn5dc", "/m/01rd7k",
        #    "/m/07svc2k", "/m/09ddx", "/m/07qdb04", "/m/0dbvp", "/m/07qwf61"]

        # Race car/auto racing, Medium engine, Heavy engine, Engine knocking,
        #   Engine starting, Accelerating/revving/vroomv
        # dcSpec = {
        #    "/m/0ltv": 0, "/t/dd00066": 0, "/t/dd00067": 0, "/m/01h82_": 0,
        #    "/t/dd00130": 0, "/m/07q2z82": 0}

        # Inside, small room, Inside, large room or hall, Inside, public space,
        # Outside, urban or manmade, Outside, rural or natural, Reverberation
        # Echo, Noise, Environmental noise, Static, Mains hum, Distortion
        # Sidetone, Cacophony, White noise, Pink noise, Throbbing, Vibration
        dcSpec = {
            "/t/dd00125": 0, "/t/dd00126": 0, "/t/dd00127": 0,
            "/t/dd00128": 0, "/t/dd00129": 0, "/m/01b9nn": 0, "/m/01jnbd": 0,
            "/m/096m7z": 0, "/m/06_y0by": 0, "/m/07rgkc5": 0, "/m/06xkwv": 0,
            "/m/0g12c5": 0, "/m/08p9q4": 0, "/m/07szfh9": 0, "/m/0chx_": 0,
            "/m/0cj0r": 0, "/m/07p_0gm": 0, "/m/01jwx6": 0}

        sAll = "../list/unbalanced_train_segments.csv"
        sExtracted = "../list/03_noise_segments.csv"
        fAll = open(sAll, "r")
        fExtracted = open(sExtracted, "w")
        lAll = fAll.readlines()
        lContain, dcSpec = ContainList(lAll, dcSpec)
        fExtracted.write("".join(lContain))
        fAll.close()
        fExtracted.close()
        print(dcSpec)
        print("Write to file:%s Contain: %d" % (sExtracted, len(lContain)))


if __name__ == "__main__":
    main()
