#Author: Jacob Rust
#Date: 21/07/2019
#Description:This script sorts downloaded files into folders of their respective types


import os
import sys
import filecmp

#creates a folder for a file type if it does not exist
def createFolder(downloadsDir, fileTypes):
    for fileType in fileTypes.keys():
        directory = downloadsDir + "\\" + fileType

        if not os.path.exists(directory):
            os.mkdir(directory)

def moveFile(filename, downloadsDir, fileTypes):
    if "." in filename: 
        temp = filename.split(".")
        ext = temp[-1].lower() #for the file extension
    else:
        return

    for fileType in fileTypes.keys():
        if ext in fileTypes[fileType]:
            src_path = downloadsDir + "\\" + filename
            dest_path = downloadsDir + "\\" + fileType + "\\" + filename
        else: continue

        if not os.path.isfile(dest_path): 
            os.rename(src_path, dest_path) #Moves the file
        elif os.path.isfile(dest_path) and filecmp.cmp(src_path, dest_path, shallow = False):
            os.remove(src_path)
            print(src_path, "deleted")
        return
        

def main():

    #Dictionary contains file types as keys and lists of their corresponding file formats
    fileTypes = {}
    fileTypes["Images"] = ["jpg", "gif", "png", "jpeg", "bmp"]
    fileTypes["Audio"] = ["mp3", "wav", "aiff", "flac", "aac"]
    fileTypes["Video"] = ["m4v", "flv", "mpeg", "mov", "mpg", "mpe", "wmv", \
                          "MOV", "mp4", "mkv", "webm", "avi"]
    fileTypes["Documents"] = ["doc", "docx", "txt", "ppt", "pptx", "pdf", "rtf", "epub"]
    fileTypes["Data_and_Tables"] = ["xlsx", "csv"]
    fileTypes["webpage_and_webdocs"] = ["html", "svg"]
    fileTypes["Exe"] = ["exe"]
    fileTypes["Compressed"] = ["zip", "tar", "7", "rar"]
    fileTypes["Virtual_Machine_and_iso"] = ["vmdk", "ova", "iso"]
    
    #The second command line argument is the download directory
    downloadDirectory = sys.argv[1]
    downloadFiles = os.listdir(downloadDirectory)
    createFolder(downloadDirectory, fileTypes)

    for filename in downloadFiles:
        try:
            moveFile(filename, downloadDirectory, fileTypes)
        except Exception:
            print(filename, "won\'t be sorted")
            continue

main()
            

    




        
