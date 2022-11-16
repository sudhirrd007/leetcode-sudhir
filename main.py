import os
import shutil

# constants
NUMBER = 'number'
FILENAME = 'fileName'
DIFFICULTY = 'difficulty'
LANGUAGE = 'language'
TAGS = 'tags'
LEETCODELINK = 'leetcodeLink'

METADATA = {NUMBER: 0, FILENAME: "", DIFFICULTY: "", LANGUAGE: "", TAGS: [], LEETCODELINK: ""}

FOLDER_MAPPINGS = {
    'ARRAY': 'Array',
    'HASHTABLE': 'HashTable',
    'LINKEDLIST': 'LinkedList',
    'MATH': 'Math',
    'RECURSION': 'Recursion'
}


# class definitions -------------------------
class FileAnalyzer:
    def __init__(self, fileLocation, METADATA) -> None:
        self.fileLocation = fileLocation
        self.metadata = METADATA
        self.fetchData()

    def fetchData(self) -> list:
        separator = '='
        with open(f'./TemporaryFiles/{self.fileLocation}', "r") as file:
            for line in file:
                if('end' in line):
                    break
                for KEY in self.metadata.keys():
                    if(KEY == 'tags'):
                        tagsStr = line.split(separator)[-1].strip()
                        self.metadata[KEY] = [tag.strip() for tag in tagsStr.split(",")]
                        break
                    if(KEY in line):
                        self.metadata[KEY] = line.split(separator)[-1].strip()
                        break


# PROGRAM STARTING POINT -------------------------

# fetching recently added files
unsavedFiles = dict()
for fileName in os.listdir('./TemporaryFiles'):
    unsavedFiles[fileName] = FileAnalyzer(fileName, METADATA.copy()).metadata

# looping through all files
for fileName in unsavedFiles.keys():
    tagsList = unsavedFiles[fileName][TAGS]
    fileLoc = f'./TemporaryFiles/{fileName}'
    for tag in tagsList:
        # Folder existence check
        folderLoc = f'./{FOLDER_MAPPINGS[tag]}'
        if(not os.path.isdir(folderLoc)):
            raise Exception("No folder exist!!!")

        # file existence check
        destinationLoc = f'./{folderLoc}/{fileName}'
        if(not os.path.exists(destinationLoc)):
            shutil.copyfile(fileLoc, destinationLoc)
            print(f'[+] {fileName} copied to {folderLoc}')

        if(not os.path.exists(f'./ALL/{fileName}')):
            shutil.copyfile(fileLoc, f'./ALL/{fileName}')
            print(f'[+] {fileName} copied to ./ALL')
      
    os.remove(fileLoc)
    print(f'[-] {fileName} removed ')