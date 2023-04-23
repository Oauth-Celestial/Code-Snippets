import os
from os import path
import shutil
from progressbar import ProgressBar

image_extension = [".jpg",".jpeg",".png",".gif",".tiff",".raw"]
video_extension = [".mp4",".mov",".avi"]
audio_extension = [".mp3"]
document_extension = [".pdf",".txt",".doc",".docx", ".csv",".xslx"]

def getFileExtension(filePath:str):

    return os.path.splitext(filePath)[1]

def makeFolder(basePath:str):

    folderName = ["Organized Images","Organized Videos","Organized audio","Organized Documents","Organized Others"]
    folderPath = [ os.path.join(basePath, name) for name in folderName]
    
    for folder in folderPath:
        if not (path.exists(folder)):
            os.mkdir(folder)
        else:
            pass
    organizeImages(basePath=basePath,destinationPath=folderPath[0])
    organizeVideos(basePath=basePath,destinationPath=folderPath[1])
    organizeAudio(basePath=basePath,destinationPath=folderPath[2])
    organizeDocments(basePath=basePath,destinationPath=folderPath[3])
    organizeRemainingFiles(basePath=basePath,destinationPath=folderPath[4])
    


def organizeImages(basePath:str,destinationPath):
    for i in os.scandir(basePath):
        if (i.is_file()):
            if(getFileExtension(i.path) in image_extension):
                try:
                    shutil.move(i.path,destinationPath)
                except:
                    pass
    print("Images Moved")


def organizeVideos(basePath:str,destinationPath):
    for i in os.scandir(basePath):
        if (i.is_file()):
            if(getFileExtension(i.path) in video_extension):
                try:
                    shutil.move(i.path,destinationPath)
                except:
                    pass
    print("Videos Moved")

def organizeDocments(basePath:str,destinationPath):
    for i in os.scandir(basePath):
        if (i.is_file()):
            if(getFileExtension(i.path) in document_extension):
                try:
                    shutil.move(i.path,destinationPath)
                except:
                    pass
    print("Documents Moved")


def organizeAudio(basePath:str,destinationPath):
    for i in os.scandir(basePath):
        if (i.is_file()):
            if(getFileExtension(i.path) in audio_extension):
                try:
                    shutil.move(i.path,destinationPath)
                except:
                    pass
    print("Audio Moved")

def organizeRemainingFiles(basePath:str,destinationPath):
    for i in os.scandir(basePath):
        if (i.is_file()):
            try:
                shutil.move(i.path,destinationPath)
            except:
                pass
               
    print("Folder Cleared")


userInputPath = input("Please enter the path to Organize ")
if (os.path.exists(userInputPath)):

    os.chdir(userInputPath)
    workingFolder = os.getcwd()
    makeFolder(workingFolder)

else:
    print("Enter a Valid Path")
