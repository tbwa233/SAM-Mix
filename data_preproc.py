import h5py
import nibabel as nib
import numpy as np
import os
import math
from PIL import Image
from tqdm import tqdm

"""
This script generates an arbitrary number of datasets from given directories in volumeDirs and segmentationDirs.
These ith directory in each must contain the volumes and/or segmentations for the ith dataset. 
The number of .nii files in the volume and segmentation directories for each dataset must be equal and the order must be the same (i.e. the first segmentation .nii file and the first volume .nii file must be from the same scan).
"""

volumeDirs = ["Datasets/RawData/TestingData/TestingVolumes/", "Datasets/RawData/TrainingData/TrainingVolumes/", "Datasets/RawData/ValidationData/ValidationVolumes/"]
segmentationDirs = ["Datasets/RawData/TestingData/TestingSegmentations/", "Datasets/RawData/TrainingData/TrainingSegmentations/", "Datasets/RawData/ValidationData/ValidationSegmentations/"]

fileNames = ["FullLiTSTestingDataset.hdf5", "FullLiTSTrainingDataset.hdf5", "FullLiTSValidationDataset.hdf5"]

#The number of CT scans used in each dataset is logged but not used in the rest of the script
numFiles = []
for fileName in volumeDirs:
    numFiles.append(len([name for name in os.listdir(fileName) if os.path.isfile(os.path.join(fileName, name))]))

#Percent of slices to keep from each scan, starts from middle of array
keepRate = 0.3

#Resize all slices/segmentations to imageDim x imageDim
imageDim = 256

#Standard window-leveling performed on all slices
def window_level(vol, window_center, window_width): 
    img_min = window_center - window_width // 2 
    img_max = window_center + window_width // 2 
    window_image = vol.copy() 
    window_image[window_image < img_min] = img_min 
    window_image[window_image > img_max] = img_max 

    return window_image 

#Hard-coded maximum and minimum values for full LiTS dataset because recalculating is very slow
minVal = -3055
maxVal = 5811

#Run cell to create binary datasets based on the LiTS format
livers = []
total = []

for i in range(len(volumeDirs)):
    volumeDir = volumeDirs[i]
    segmentationDir = segmentationDirs[i]

    numLivers = 0
    totalSlices = 0

    file = h5py.File(fileNames[i], "w")

    sliceNum = 0

    for i, name in tqdm(enumerate(os.listdir(volumeDir))):
        #Disregards hidden files
        if name[0] == '.':
            continue

        #Loads segmentation and volume data from .nii file
        ctScan = nib.load(volumeDir + name)
        volumeData = ctScan.get_fdata()

        volumeData = window_level(volumeData, 40, 400)

        segmentation = nib.load(segmentationDir + os.listdir(segmentationDir)[i])
        segmentData = segmentation.get_fdata()

        #Loops through all usable slices and adds data to h5 file
        #Finds middle index, subtracts half * keepRate from it, goes to middle index + half * keepRate
        for plane in range(math.ceil(((volumeData.shape[2] - 1) / 2) - (((volumeData.shape[2] - 1) / 2) * keepRate)), 
        math.floor(((volumeData.shape[2] - 1) / 2) + (((volumeData.shape[2] - 1) / 2) * keepRate))):

            volumeSlice = np.array(Image.fromarray(volumeData[:,:,plane].astype(np.int16)).resize((imageDim, imageDim), Image.BILINEAR))
            segmentSlice = segmentData[:,:,plane].astype(np.int16)

            volumeSlice = volumeSlice.astype(np.float16)

            volumeSlice -= minVal
            volumeSlice /= maxVal - minVal

            #Gets max value of current segmenation, limits it to 1 (1 if contains liver, 0 if not)
            label = min(np.amax(segmentSlice), 1)
            segmentSlice = np.array(Image.fromarray(segmentSlice).resize((imageDim, imageDim), Image.NEAREST))

            numLivers += label
            totalSlices += 1

            #Creates subgroup for current slice in current scan, adds slice/segmentation/label data
            currSlice = file.create_group("Slice" + str(sliceNum))
            currSlice.create_dataset("Slice", data=volumeSlice)
            currSlice.create_dataset("Segmentation", data=segmentSlice)
            currSlice.attrs.create("ImageLabel", label, (1,), "int")

            sliceNum += 1

    livers.append(numLivers)
    total.append(totalSlices)

print(f"Liver Present: {livers} Total: {total}")

file.close()
