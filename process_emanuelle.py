# This code hase been acquired from TRN-pytorch repository
# 'https://github.com/metalbubble/TRN-pytorch/blob/master/process_dataset.py'
# which is prepared by Bolei Zhou
#
# Processing the raw dataset of Jester
#
# generate the meta files:
#   category.txt:               the list of categories.
#   train_videofolder.txt:      each row contains [videoname num_frames classIDX]
#   val_videofolder.txt:        same as above
#
# Created by Bolei Zhou, Dec.2 2017

import os
from os.path import join
from shutil import copy
import random

dataFolder = '../../data'
dataset_name = 'emmanuelle'
labelsDict = {
    0:"1",
    1:"a",
    2:"an",
    3:"b",
    4:"c",
    5:"ch",
    6:"d",
    7:"ei",
    8:"eu",
    9:"f",
    10:"g",
    11:"gn",
    12:"i",
    13:"in",
    14:"j",
    15:"l",
    16:"ll",
    17:"m",
    18:"n",
    19:"o",
    20:"on",
    21:"ou",
    22:"p",
    23:"r",
    24:"s",
    25:"t",
    26:"u",
    27:"v",
    28:"x",
    29:"z"
}


reverseLabelsDict = {value:key for key,value in labelsDict.items()}
liste = []
with open("folders.txt", "w") as f:
    symbolList = os.listdir(join(dataFolder, dataset_name))
    for i, symbol in enumerate(symbolList):
        print(symbol, i, "/", len(symbolList))
        for seq in os.listdir(join(dataFolder, dataset_name, symbol)):
            seqName = str(reverseLabelsDict[symbol])+seq[-2:]
            try:
                os.makedirs(join(dataFolder, dataset_name+"2", seqName))
            except FileExistsError as e:
                pass
            fileList = os.listdir(join(dataFolder, dataset_name, symbol, seq))
            for picName in fileList:
                newPicName = picName.split("_")[1].zfill(9)
                copy(join(dataFolder, dataset_name, symbol, seq, picName), join(dataFolder, dataset_name+"2", seqName, newPicName))
            f.write(seqName+", "+str(len(fileList))+", "+str(reverseLabelsDict[symbol])+"\n")
            liste.append((seqName, len(fileList), reverseLabelsDict[symbol]))
print(len(liste), liste)
random.shuffle(liste)

ratio = 0.8
trainListe = liste[:int(ratio * len(liste))]
valListe = liste[int(ratio * len(liste)):]
print(len(trainListe), len(valListe))

with open("../../data/emmanuelle2/train_videofolder.txt", "w") as f:
    for tup in trainListe:
        f.write("%s %s %s\n"%tup)


with open("../../data/emmanuelle2/val_videofolder.txt", "w") as f:
    for tup in valListe:
        f.write("%s %s %s\n"%tup)