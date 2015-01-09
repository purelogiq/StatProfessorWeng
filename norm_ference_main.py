#------------------------------------------------------------------------------
# Author:      Israel Madueme (imadueme@andrew.cmu.edu)
# Created:     08/08/2012
# Class:       15-112E Summer
#
# NormFerence main application
#------------------------------------------------------------------------------
from prof import Prof
from sample import Sample
import helper

def run():
    class Struct: pass
    global userInput
    userInput = Struct()
    intro()


def intro():
    Prof.speak("", Prof.TEXT_NORMFERENCE)
    Prof.speak(Prof.FACE_NORMAL, Prof.TEXT_INTRO)
    helper.readString("Are you ready?: ", None)
    letsGetStarted()


def letsGetStarted():
    print           #Prints new line
    Prof.speak(Prof.FACE_NORMAL, Prof.TEXT_OVERVIEW)
    ready = helper.getString("Are you ready?" +
                             "[yes/talk faster]: ",
                             Prof.FACE_INVALID_INPUT,
                             ["yes", "talk faster"])
    if ready == "talk faster":
        Prof.speech_delay = 0
    dataOrDescriptive()


def dataOrDescriptive():
    print
    Prof.speak(Prof.FACE_NORMAL, Prof.TEXT_DATA_OR_DIS)
    data = helper.getString("What type of data do you have? [list/summary]: ",
                            Prof.FACE_INVALID_INPUT,
                            ["list", "summary"])
    print
    if data == "list":
        getListData()
    else:
        userInput.numbers = False
        getSummaryData()


def getListData():
    print
    Prof.speak(Prof.FACE_NORMAL, Prof.TEXT_FILE_OR_MANUALLY)
    dataLoc = helper.getString("How do you want to enter the numbers? " +
                               "[file/by hand]: ",
                               Prof.FACE_INVALID_INPUT,
                               ["file", "by hand"])

    error = ""
    userInput.numbers = False
    while userInput.numbers == False:
        if dataLoc == "file":
            try:
                userInput.numbers =\
                   helper.loadNumericCSV(helper.readString(error +
                                                 "Enter a file path: ", None))
            except helper.InvalidCSV:
                error = "Invalid CSV file. "
            except:
                error = "Invalid file path. "
        else:
            userInput.numbers = helper.readNumByLine()
    print
    getSummaryData()


def getSummaryData():
    if(userInput.numbers == False):
        userInput.numbers = None
        getXBar()
        getSampleSize()
    else:
        userInput.xbar = None
        userInput.n = len(userInput.numbers)

    getSigma()
    if(userInput.sigma == None and userInput.numbers == None):
        getS()
    else:
        userInput.s = None

    getNullHyp()
    getConfidenceLevel()

    getIsRandom()
    if userInput.n >= 30: userInput.isNormal = True
    else: getIsNormal()
    getIsIndependant()

    getMeasurementName()

    report()


def getXBar():
    Prof.speak(Prof.FACE_NORMAL, Prof.TEXT_GET_XBAR)
    userInput.xbar = helper.getFloat("Enter the average (x-bar): ",
                                     Prof.FACE_INVALID_INPUT,
                                     None, None)
    print


def getSampleSize():
    Prof.speak(Prof.FACE_NORMAL, Prof.TEXT_GET_N)
    userInput.n = helper.getInt("Enter the sample size (n) [>= 1]: ",
                                     Prof.FACE_INVALID_INPUT,
                                     1, None)
    print


def getSigma():
    Prof.speak(Prof.FACE_NORMAL, Prof.TEXT_GET_SIGMA)
    know = helper.getString("Do you know the value of sigma? [yes/no]: ",
                            Prof.FACE_INVALID_INPUT,
                            ["yes", "no"])
    if know == "yes":
        userInput.sigma = \
           helper.getFloat("Enter the population standard deviation (sigma)"+
                            "[>=1]: ",
                                Prof.FACE_INVALID_INPUT,
                                1, None)
    else:
        userInput.sigma = None
    print


def getS():
    Prof.speak(Prof.FACE_NORMAL, Prof.TEXT_GET_S)
    userInput.s =\
        helper.getFloat("Enter the sample standard deviation (s) [>= 1]: ",
                            Prof.FACE_INVALID_INPUT,
                            1, None)
    print


def getNullHyp():
    Prof.speak(Prof.FACE_NORMAL, Prof.TEXT_GET_NULL)
    userInput.nullHyp =\
        helper.getFloat("Enter your hypothesis for the population mean (Ho): ",
                                Prof.FACE_INVALID_INPUT,
                                None, None)
    print


def getConfidenceLevel():
    Prof.speak(Prof.FACE_NORMAL, Prof.TEXT_GET_CL)
    cLevel = helper.getString("Enter how confident you want to be [95/99]: ",
                                     Prof.FACE_INVALID_INPUT,
                                     ["95", "99"])
    if cLevel == "99":
        userInput.cLevel = Sample.Z_CLEVEL_99
    else:
        userInput.cLevel = Sample.Z_CLEVEL_95
    print


def getIsRandom():
    Prof.speak(Prof.FACE_NORMAL, Prof.TEXT_GET_ISRANDOM)
    isRandom =\
        helper.getString("Was the sample collected randomly? [yes/no] : ",
                            Prof.FACE_INVALID_INPUT,
                            ["yes", "no"])
    if isRandom == "yes": userInput.isRandom = True
    else: userInput.isRandom = False
    print


def getIsNormal():
    Prof.speak(Prof.FACE_NORMAL, Prof.TEXT_GET_ISNORMAL)
    isNormal =\
        helper.getString("Do you think the population is normal? [yes/no]: ",
                                     Prof.FACE_INVALID_INPUT,
                                     ["yes", "no"])
    if isNormal == "yes": userInput.isNormal = True
    else: userInput.isNormal = False
    print


def getIsIndependant():
    Prof.speak(Prof.FACE_NORMAL, Prof.TEXT_GET_ISINDEPENDANT)
    isIndependant =\
        helper.getString("Were the measurements independant? [yes/no]: ",
                            Prof.FACE_INVALID_INPUT,
                            ["yes", "no"])
    if isIndependant == "yes": userInput.isIndependant = True
    else: userInput.isIndependant = False
    print


def getMeasurementName():
    Prof.speak(Prof.FACE_NORMAL, Prof.TEXT_GET_LABEL)
    userInput.measurementName = \
            helper.getString("Enter a label for the data: ",
                                     Prof.FACE_INVALID_INPUT,
                                     None)
    print


def report():
    sample = Sample(numbers = userInput.numbers,
                    xbar = userInput.xbar,
                    sigma = userInput.sigma,
                    s = userInput.s,
                    n = userInput.n,
                    nullHyp = userInput.nullHyp,
                    confidenceLevel = userInput.cLevel,
                    isRandom = userInput.isRandom,
                    isNormal = userInput.isNormal,
                    isIndependant = userInput.isIndependant,
                    measurementName = userInput.measurementName)

    Prof.speech_delay = 0.1
    Prof.speak(Prof.FACE_NORMAL, Prof.TEXT_CALCULATING)
    Prof.speak(Prof.FACE_HMM, Prof.TEXT_HMMM)
    Prof.speak(Prof.FACE_MHMM, Prof.TEXT_MHMMM)
    Prof.speak(Prof.FACE_WOAH, Prof.TEXT_WOAH)
    Prof.speak(Prof.FACE_CANT_BE_RIGHT, Prof.TEXT_CANT_BE_RIGHT)
    Prof.speak(Prof.FACE_HOW_TO_DO, Prof.TEXT_HOW_TO_DO_THIS)
    Prof.speak(Prof.FACE_OH, Prof.TEXT_OOO)
    Prof.speak(Prof.FACE_AHA, Prof.TEXT_AHA)
    Prof.speak(Prof.FACE_DONE, Prof.TEXT_DONE)

    #give report
    if(sample.numbers != None):
        Prof.speak(Prof.FACE_NORMAL, Prof.REPORT_HISTOGRAM)
        sample.printHistogram()

    #report summary statistics
    Prof.report(Prof.REPORT_AVERAGE,
                [sample.measurementName, sample.xbar, None, None])

    sd = sample.s if sample.sigma == None else sample.sigma
    Prof.report(Prof.REPORT_DEVIATION,
                [sd, sample.xbar, sample.measurementName, None])

    if(sample.numbers != None):
        Prof.report(Prof.REPORT_MEDIAN_AND_RANGE,
                    [sample.median, sample.iqr[0], sample.iqr[1],
                     sample.measurementName])

    concludeHypothesis(sample)
    concludeAssumtions(sample)
    saveData(sample)
    Prof.speak(Prof.FACE_DONE, Prof.TEXT_END)


def concludeHypothesis(sample):
    cLevel = 95
    if(sample.confidenceInterval == Sample.Z_CLEVEL_99):
        cLevel = 99

    Prof.report(Prof.REPORT_INTERVAL,
                [sample.confidenceInterval[0], sample.confidenceInterval[1],
                 cLevel, sample.measurementName])

    if sample.nullHyp > sample.confidenceInterval[1]:
        Prof.report(Prof.REPORT_HYP_ABOVE,
                    [sample.nullHyp, sample.confidenceInterval[1],
                     sample.measurementName, None],
                    Prof.FACE_SORRY)

    elif sample.nullHyp < sample.confidenceInterval[0]:
        Prof.report(Prof.REPORT_HYP_BELOW,
                    [sample.nullHyp, sample.confidenceInterval[0],
                     sample.measurementName, None],
                    Prof.FACE_SORRY)

    elif(sample.nullHyp >= sample.confidenceInterval[0] and
         sample.nullHyp <= sample.confidenceInterval[1]):
            Prof.report(Prof.REPORT_HYP_OK,
                   [sample.confidenceInterval[0], sample.confidenceInterval[1],
                    sample.nullHyp, sample.measurementName],
                    Prof.FACE_DONE)


def concludeAssumtions(sample):
    if(not sample.isRandom):
        Prof.speak(Prof.FACE_SORRY, Prof.REPORT_NOT_RANDOM)
    if(not sample.isNormal):
        Prof.speak(Prof.FACE_SORRY, Prof.REPORT_NOT_NORMAL)
    if(not sample.isIndependant):
        Prof.speak(Prof.FACE_SORRY, Prof.REPORT_NOT_INDEPENDANT)
    if(sample.isRandom and sample.isNormal and sample.isIndependant):
        Prof.speak(Prof.FACE_DONE, Prof.REPORT_GOOD_TEST)


def saveData(samp):
    Prof.speak(Prof.FACE_NORMAL, Prof.TEXT_SAVE)
    saveOrNot = helper.getString("Would you like to save? [yes/no]: ",
                                 Prof.FACE_INVALID_INPUT,
                                 ["yes", "no"])

    if saveOrNot == "yes":
        data = ""
        data += "Report for {0}\n".format(samp.measurementName)
        if(samp.histogram != None):
            data += ("Histogram of data, suspected ouliers marked with *\n\n")
            for r in xrange(len(samp.histogram)):
                aRow = ""
                for col in samp.histogram[r]:
                    aRow += col
                if r == samp.indexOfMean:
                    aRow += "  <--average = " + str(round(samp.xbar, 3))
                elif r == 0:
                    aRow += "  <--min = " + str(round(samp.min, 3))
                elif r == len(samp.histogram) - 1:
                    aRow += "  <--max = " + str(round(samp.max, 3))
                data += aRow + "\n"
        data += "\n\r"
        data += "Average {0} is {1}\n\n".format(samp.measurementName,
                                                 samp.xbar)

        sd = samp.s if samp.sigma == None else samp.sigma
        data += "Sample standard deviation: {0}\n\n".format(sd)
        data += "Sample mean standard deviation: {0}\n\n".format(
                samp.meanSD)
        if (samp.numbers != None):
            data += "Sample median is {0}\n\n".format(samp.median)
            data += "25th percentile: {0}\n\n".format(samp.iqr[0])
            data += "75th percentile: {0}\n\n".format(samp.iqr[1])
            data += "IQR: {0}\n\n".format(samp.iqr[1] - samp.iqr[0])

        data += "Hypothesized mean: {0}\n\n".format(samp.nullHyp)

        cLevel = 95
        if(samp.confidenceInterval == Sample.Z_CLEVEL_99):
            cLevel = 99
        data += ("Confidence Interval of confidence level {0}: " +
                 "({1}, {2})\n\n").format(cLevel,
                                     samp.confidenceInterval[0],
                                     samp.confidenceInterval[1])
        data += "Sample random: {0}\n\n".format(samp.isRandom)
        data += "Sample distribution normal: {0}\n\n".format(samp.isNormal)
        data += "Sampling independant: {0}\n\n".format(samp.isIndependant)
        helper.saveFile(data)

run()
