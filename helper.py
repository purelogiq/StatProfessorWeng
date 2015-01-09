#------------------------------------------------------------------------------
# Author:      Israel Madueme (imadueme@andrew.cmu.edu)
# Created:     08/05/2012
# Class:       15-112E Summer
#
# Helper io functions.
#------------------------------------------------------------------------------
class InvalidInput(Exception): pass
class InvalidFileName(Exception): pass
class InvalidCSV(Exception): pass
class NumTooSmall(Exception): pass
class NumTooLarge(Exception): pass


def readInt(prompt, lowBound, upBound):
    """Reads an integer between lowBound and upBound (inclusive) from input.
    Set lowBound or upBound (or both) to None to not bound in that direction.
    Returns the integer or raises an exception."""
    anInt = raw_input(prompt)
    try:
        anInt = int(anInt)
    except:
        raise InvalidInput()
    if lowBound != None and anInt < lowBound:
        raise NumTooSmall()
    if upBound != None and anInt > upBound:
        raise NumTooLarge()
    return anInt


def readFloat(prompt, lowBound, upBound):
    """Reads a float between lowBound and upBound (inclusive) from input.
    Set lowBound or upBound (or both) to None to not bound in that direction.
    Returns the float or raises an exception."""
    aFloat = raw_input(prompt)
    try:
        aFloat = float(aFloat)
    except:
        raise InvalidInput()
    if lowBound != None and aFloat < lowBound:
        raise NumTooSmall()
    if upBound != None and aFloat > upBound:
        raise NumTooLarge()
    return aFloat


def readString(prompt, allowed):
    """Return what is read by raw_input.
    Raises an InvalidInput Exception if allowed is not None and is a list of
    (lowercase) strings and what is inputed is not in that list."""
    text = str(raw_input(prompt)) #str() for IDE code completion...
    if(allowed != None):
        text = text.lower()
        text = text.strip()
        if(text not in allowed):
            raise InvalidInput()
        return text #returns stripped, lowercase version
    return text


def getInt(prompt, errorMessage, lowBound, upBound):
    """Ask for a valid int until one is given then return the int."""
    error = ""
    value = None
    while value == None:
        try:
            value = readInt(error + prompt, lowBound, upBound)
        except:
            error = errorMessage
    return value


def getFloat(prompt, errorMessage, lowBound, upBound):
    """Ask for a valid float until one is given then return the float."""
    error = ""
    value = None
    while value == None:
        try:
            value = readFloat(error + prompt, lowBound, upBound)
        except:
            error = errorMessage
    return value


def getString(prompt, errorMessage, allowed):
    """Ask for a valid string until one is given then return the string."""
    error = ""
    value = None
    while value == None:
        try:
            value = readString(error + prompt, allowed)
        except:
            error = errorMessage
    return value


def loadNumericCSV(fileName):
    """Loads a numeric CSV and returns the values as a list.
    Raises an exception if there is something wrong with the CSV.
    In this application, a CSV cannot contain any entries that aren't numbers.
    Values can be organized however (on a new line, or on the same line),
    aslong as they are seperated by commas.
    """
    try:
        theFile = open(fileName)
    except:
        raise InvalidFileName()
    fileString = theFile.read()
    fileString = fileString.strip()
    values = fileString.split(",")
    values = removeEmptyItems(values)
    numValues = []
    for value in values:
        try:
            num = float(value)
        except:
            raise InvalidCSV(value)
        numValues.append(num)
    return numValues


def saveFile(data):
    filePath = False
    while filePath == False:
        try:
            filePath =\
		getString("Enter a file path (with the file name (.txt)): ",
                                 "Invalid file path. ",
                                 None)
        except: pass

    aFile = open(filePath, "w")
    aFile.write(data)
    print


def readNumByLine():
    done = "done"
    message = "Enter a number or '"+done+"': "
    nums = []
    num = None
    while num != done:
        num = raw_input(message).strip()
        if num == done: break
        try:
            num = float(num)
        except:
            message = "Invalid. Please enter a number or '"+done+"': "
            continue
        nums.append(num)
        message = "Enter a number or '"+done+"': "
    if not len(nums) > 0:
        return readNumByLine()
    else:
        return nums


def removeEmptyItems(aList):
    """Removes empty items from a list."""
    notEmpty = []
    for item in aList:
        if not item == "":
            notEmpty.append(item)
    return notEmpty
