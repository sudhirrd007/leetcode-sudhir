import os
import shutil
import string
import sqlite3
import pandas as pd


# Constants -------------------------------------
# srd, need to change every time
FOLDER_MAPPINGS = {
    'ARRAY': {'title': 'Array', 'folderName': 'Array', 'readmeName': 'array'},
    'BINARYSEARCH': {'title': 'Binary Search', 'folderName': 'BinarySearch', 'readmeName': 'binary-search'},
    'DIVIDEANDCONQUER': {'title': 'Divide and Conquer', 'folderName': 'DivideAndConquer', 'readmeName': 'divide-and-conquer'},
    'HASHTABLE': {'title': 'Hash Table', 'folderName': 'HashTable', 'readmeName': 'hash-table'},
    'LINKEDLIST': {'title': 'Linked List', 'folderName': 'LinkedList', 'readmeName': 'linked-list'},
    'MATH': {'title': 'Math', 'folderName': 'Math', 'readmeName': 'math'},
    'RECURSION': {'title': 'Recursion', 'folderName': 'Recursion', 'readmeName': 'recursion'}
}

# -------------------------------------------------------
# Class Definitions -------------------------------------
# -------------------------------------------------------
class Problem:
    def __init__(self, fileLocation) -> None:
        self.fileLocation = fileLocation
        self.NUMBER = 0
        self.TITLE = ''
        self.FILENAME = ''
        self.DIFFICULTY = ''
        self.LANGUAGE = ''
        self.ACCEPTANCERATE = ''
        self.TAGS = []
        self.LEETCODELINK = ''
        self.NOTES = ''
        self.fetchData()

    def fetchData(self) -> list:
        separator = '='
        with open(self.fileLocation, "r") as file:
            for line in file:
                if('end-srd' in line):
                    break
                elif('number-srd' in line):
                    self.NUMBER = line.split(separator)[-1].strip()
                elif('title-srd' in line):
                    self.TITLE = line.split(separator)[-1].strip()
                elif('filename-srd' in line):
                    self.FILENAME = line.split(separator)[-1].strip()
                elif('difficulty-srd' in line):
                    self.DIFFICULTY = line.split(separator)[-1].strip().lower()
                elif('language-srd' in line):
                    self.LANGUAGE = line.split(separator)[-1].strip().lower()
                elif('tags-srd' in line):
                    tagsStr = line.split(separator)[-1].strip()
                    tags = [tag.strip() for tag in tagsStr.split(",")]
                    self.TAGS = [tag for tag in tags if (tag)]
                elif('leetcodelink-srd' in line):
                    self.LEETCODELINK = line.split(separator)[-1].strip()
                elif('acceptancerate-srd' in line):
                    self.ACCEPTANCERATE = line.split(separator)[-1].strip()
                elif('notes-srd' in line):
                    self.NOTES = line.split(separator)[-1].strip()

# ----------------------------------------------------------
# Function Declarations ------------------------------------
# ----------------------------------------------------------
def createTable(dbName='leetcode.db'):
    # connect to SQLite3
    con = sqlite3.connect(dbName)
    cur = con.cursor()
    
    # Create Table
    cur.execute("CREATE TABLE IF NOT EXISTS Problem(number INTEGER PRIMARY KEY, \
        title TEXT NOT NULL, \
        filename TEXT NOT NULL, \
        difficulty TEXT NOT NULL, \
        language TEXT NOT NULL, \
        tags TEXT NOT NULL, \
        leetcodelink TEXT NOT NULL, \
        acceptancerate INTEGER NOT NULL, \
        notes TEXT NOT NULL)")
    con.commit()

def introStringReadMe():
    INTRO_STRING = """
## Official [LeetCode](https://leetcode.com/problemset/all/) problems with solutions


![language](https://img.shields.io/badge/language-python%20%2F%20javascript-blue)&nbsp;
![license](https://img.shields.io/badge/license-MIT-orange)&nbsp;
![update](https://img.shields.io/badge/update-weekly-blue)&nbsp;
![status](https://img.shields.io/badge/status-stable-orange)&nbsp;
![visitors](https://visitor-badge.laobi.icu/badge?page_id=sudhirrd007.leetcode.solutions)&nbsp;
<br><br>\n\n\n"""
    return INTRO_STRING

def indexStringReadMe():
    INDEX_STRING = "# Index\n"
    ALPHABET_LIST = list(string.ascii_lowercase)

    for alphabet in ALPHABET_LIST:
        TEMP_INDEX_STRING = ""
        for tag in sorted(list(FOLDER_MAPPINGS.keys())):
            if(tag[0].lower() == alphabet):
                # folderName = FOLDER_MAPPINGS[tag]['folderName']
                title = FOLDER_MAPPINGS[tag]['title']
                readmeName = FOLDER_MAPPINGS[tag]['readmeName']
                TEMP_INDEX_STRING += f'[{title}](#{readmeName}) <br> \n'
        if(TEMP_INDEX_STRING):
            INDEX_STRING += f'{alphabet.upper()} <br> \n{TEMP_INDEX_STRING} \n'
    INDEX_STRING += '<hr> \n\n'
    return INDEX_STRING

def tableHeaderStringReadMe():
    TABLE_HEADER_STRING = """
|  #  | Title  |   Difficulty  |    Language   | Acceptance rate | LeetCode Link | Notes |
|-----|------- |  ------------ | ------------- | --------------- | ------------- | ----- |\n"""
    return TABLE_HEADER_STRING

def contentStringReadMe():
    CONTENT_STRING = ""
    for tag in sorted(list(FOLDER_MAPPINGS.keys())):
        TEMP_CONTENT_STRING = ""
        readmeName = FOLDER_MAPPINGS[tag]['readmeName']
        TEMP_CONTENT_STRING = f'# {readmeName}\n'
        TEMP_CONTENT_STRING += tableHeaderStringReadMe()

    # TEMPLATE = "| 1 | [Two Sum](./data_files/PROGRAMS/EASY/0001_Two_Sum.py) | EASY | [python](./data_files/PROGRAMS/EASY/0001_Two_Sum.py) | 6948 ms | 46.8% | [Redirect](https://leetcode.com/problems/two-sum) | - |"
        for row in DATA[tag]:
            TEMP_CONTENT_STRING += "| " + str(row['number'])
            TEMP_CONTENT_STRING += " | " + "[" + row['title'] + "](" + row['filelocation'] + ")"
            TEMP_CONTENT_STRING += " | " + str(row['difficulty'])
            TEMP_CONTENT_STRING += " | " + "[" + row['language'] + "](" + row['filelocation'] + ")"
            TEMP_CONTENT_STRING += " | " + str(row['acceptancerate'])
            TEMP_CONTENT_STRING += " | " + "[Redirect](" + row['leetcodelink'] + ")"
            TEMP_CONTENT_STRING += " | " + str(row['notes']) + "|\n"

        CONTENT_STRING += TEMP_CONTENT_STRING + "\n[⬆️ Back to index](#index) <br> \n\n"
    return CONTENT_STRING


# ------------------------------------------------
# Program Starting Point -------------------------
# ------------------------------------------------

# connect to SQLite3
con = sqlite3.connect("leetcode.db")
cur = con.cursor()

# create table if exist
createTable()

## fetching tags of recently added files
unsavedFilesTags = dict()

## insert data into leetcode.db
for fileName in os.listdir('./TemporaryFiles'):
    problemObj = Problem(f'./TemporaryFiles/{fileName}')
    unsavedFilesTags[fileName] = problemObj.TAGS
    # query
    query = f"""
        INSERT INTO Problem (number, title, fileName, difficulty, language, tags, leetcodeLink, acceptanceRate, notes) VALUES
            ({problemObj.NUMBER}, '{problemObj.TITLE}', '{problemObj.FILENAME}', 
            '{problemObj.DIFFICULTY}', '{problemObj.LANGUAGE}', '{'-'.join(problemObj.TAGS)}', 
            '{problemObj.LEETCODELINK}', '{problemObj.ACCEPTANCERATE}', '{problemObj.NOTES}')"""
    cur.execute(query)
    con.commit()
##

## Copying files to appropriate folders
for fileName in unsavedFilesTags.keys():
    fileLoc = f'./TemporaryFiles/{fileName}'
    for tag in unsavedFilesTags[fileName]:
        # Folder existence check
        folderName = FOLDER_MAPPINGS[tag]['folderName']
        folderLoc = f'./{folderName}'
        if(not os.path.isdir(folderLoc)):
            os.mkdir(folderLoc)
        # file existence check
        destinationLoc = f'./{folderLoc}/{fileName}'
        # copy to respective folders
        if(not os.path.exists(destinationLoc)):
            shutil.copyfile(fileLoc, destinationLoc)
            print(f'[+] {fileName} copied to {folderLoc}')
        # copy to 'ALL' Folder
        if(not os.path.exists(f'./ALL/{fileName}')):
            shutil.copyfile(fileLoc, f'./ALL/{fileName}')
            print(f'[+] {fileName} copied to ./ALL')
    # delete copied folder      
    os.remove(fileLoc)
    print(f'[-] {fileName} removed ')
##

# combining all the data in DATA
DATA = {tag: [] for tag in FOLDER_MAPPINGS.keys()}

# template for fetching records from leetcode.db
DICT = {'number': None, \
    'title': None, \
    'filename': None, \
    'filelocation': None, \
    'difficulty': None, \
    'language': None, \
    'leetcodelink': None, \
    'acceptancerate': None, \
    'notes': None}

# fetching all the records from leetcode.db
df = pd.read_sql_query("SELECT * from Problem ORDER BY number ASC", con)

# adding data to DATA
for dataRow in df.iterrows():
    row = dataRow[1]
    DICT['number'] = row['number']
    DICT['title'] = row['title']
    DICT['filename'] = row['filename']
    DICT['difficulty'] = row['difficulty']
    DICT['language'] = row['language']
    DICT['leetcodelink'] = row['leetcodelink']
    DICT['acceptancerate'] = row['acceptancerate']
    DICT['notes'] = row['notes']
    # adding filelocation key into DICT
    for tag in row['tags'].split('-'):
        folderLoc = FOLDER_MAPPINGS[tag]['folderName']
        fileName = row['filename']
        DICT['filelocation'] = f'./{folderLoc}/{fileName}'
        # appending DICT to DATA
        DATA[tag].append(DICT.copy())

# Generating ReadME.md file
with open('./README.md', 'w') as file:
    MASTER_STRING = introStringReadMe()
    MASTER_STRING += indexStringReadMe()
    MASTER_STRING += contentStringReadMe()
    file.write(MASTER_STRING)