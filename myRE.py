import datetime
import subprocess

def findAll(file, item):
    """
    This function will find the item in the file
    with the correct given file path and file
    name, and return a count of item in each row.
    """
    with open(file) as f:
        lines = f.readlines()
        count = 0

        for line in lines:
            if item in line:
                count += 1
    
    return count

def getDate():
    """
    This function will return a string with
    proper date format.
    """
    now = datetime.datetime.now()
    return now[0:18]



