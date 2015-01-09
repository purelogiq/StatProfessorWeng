#------------------------------------------------------------------------------
# Author:      Israel Madueme (imadueme@andrew.cmu.edu)
# Created:     08/06/2012
# Class:       15-112E Summer
#
# Sample class to calculate and store data of the sample.
#------------------------------------------------------------------------------
class Sample:
    """Class that performs and stores calculations for
    1-quantitative sample mean distributions."""

    Z_CLEVEL_95 = 2 #ESTIMATED Z SCORE
    Z_CLEVEL_99 = 3
    DEFAULT_BIN_NUM = 12

    def __init__(self, numbers, xbar, sigma, s, n,
                 nullHyp, confidenceLevel,
                 isRandom, isNormal, isIndependant, measurementName):
        """Performs and stores calculations of the sample data upon creation.
        numbers: a list containing the quantitative sample data.
        xbar: the average value in the sample, use if the exact values of the
              sample data (numbers) is unavailable. Otherwise set to None.
        sigma: the POPULATION standard deviation, set to None if unknown.
        s: the SAMPLE standard deviation, set to None if unknown/not needed.
           Use sigma if known, otherwise use s. Can be automatically calculated
           if numbers was provided.
        n: the sample size. Always provide n.
        nullHyp: the mean value to test against.
        confidenceLevel: the confidence level of the constructed interval. Must
                         be one of the Z_CLEVEL_?? constants in this class.
        isRandom: True or False if the sample was selected randomly.
        isNormal: True or False if the SAMPLE MEAN distribution is normal due
                  to either the CLT or if the population distrubtion is normal.
        measurementName: A label for what the data actually measures (e.g. age)

        """
        #Store arguments.
        self.numbers = numbers
        self.xbar = float(xbar) if xbar != None else None
        self.sigma = float(sigma) if sigma != None else None
        self.s = float(s) if s != None else None
        self.n = float(n)
        self.nullHyp = float(nullHyp)
        self.confidenceLevel = confidenceLevel
        self.isRandom = isRandom
        self.isNormal = isNormal                #The mean of
        self.isIndependant = isIndependant
        self.measurementName = measurementName

        #Store default instance variables.
        self.meanSD = None
        self.median = None
        self.marginOfError = None
        self.iqr = None
        self.outliers = None
        self.min = None
        self.max = None
        self.range = None
        self.histogram = None
        self.confidenceInterval = None

        #Calculate data.
        self.calXBar()
        self.calSampleSD()
        self.calMeanSD()
        self.createConfidenceInterval()
        if self.numbers != None:
            self.numbers = sorted(self.numbers)
            self.cal5NumSum()
            self.calOutliers()
            self.createHistogram(Sample.DEFAULT_BIN_NUM)

    	self.xbar = round(self.xbar, 3)
        if self.s != None:
    	       self.s = round(self.s, 3)
        self.meanSD = round(self.meanSD, 3)
        rCI0 = round(self.confidenceInterval[0], 3)
        rCI1 = round(self.confidenceInterval[1], 3)
    	self.confidenceInterval = (rCI0, rCI1)


    def calXBar(self):
        """Calculate xbar."""
        if self.numbers == None or self.xbar != None:
            return
        self.xbar = sum(self.numbers) / self.n


    def calSampleSD(self):
        """Calculates a the sample standard deviation if numbers was given."""
        if self.numbers == None or self.s != None:
            self.s = 0
            return
        deviationsSquared = []
        for num in self.numbers:
            deviationsSquared.append((num - self.xbar) ** 2)
        try: self.s = (sum(deviationsSquared) / self.n - 1) ** 0.5
        except: self.s = 0


    def calMeanSD(self):
        """Calculates the standard deviation or standard error of xbar."""
        if self.sigma != None:
            try: self.meanSD = self.sigma / self.n ** 0.5
            except: pass
        elif self.s != None:
            try: self.meanSD = self.s / self.n ** 0.5
            except: pass


    def createConfidenceInterval(self):
        """Creates a confidence interval of the population mean."""
        self.marginOfError = self.confidenceLevel * self.meanSD
        lowEnd = self.xbar - self.marginOfError
        highEnd = self.xbar + self.marginOfError
        self.confidenceInterval = (lowEnd, highEnd)


    def cal5NumSum(self):
        """Calculates the min, median, max and IQR of the data."""
        self.min = self.numbers[0]
        self.median = self.numbers[int(self.n / 2)]
        self.max = self.numbers[-1]
        self.range = float(self.max - self.min)
        percentile25 = self.numbers[int(self.n / 4)]
        percentile75 = self.numbers[int(self.n / 4 * 3)]
        self.iqr = (percentile25, percentile75)


    def calOutliers(self):
        """Marks outliers based on 1.8 * IQR."""
        iqr = self.iqr[1] - self.iqr[0]
        lowBound = self.iqr[0] - 1.6 * iqr
        upBound = self.iqr[1] + 1.6 * iqr
        self.outliers = []
        for num in self.numbers:
            if num < lowBound or num > upBound:
                self.outliers.append(num)
        self.outliers = sorted(self.outliers)


    def createHistogram(self, numBins):
        """Creates a text based histogram based on the data."""
        #Calculate binWidth.
        binWidth = self.range / numBins
        binWidth = binWidth if binWidth > 0 else binWidth * -1
        sampleIndexStart = 0
        largestBinLenght = 0

        #Create horizontal histogram
        horzHistogram = []
        for binNum in xrange(1, numBins + 1):
            aBin = []
            for i in xrange(sampleIndexStart, int(self.n)):
                if (self.numbers[i] <= binNum * binWidth + self.min):
                    if self.numbers[i] in self.outliers:
                        aBin.append("*")
                    else:
                        aBin.append("#")
                    sampleIndexStart += 1
                else:
                    break
            horzHistogram.append(aBin)
            if len(aBin) > largestBinLenght:
                largestBinLenght = len(aBin)
            if(self.xbar >= binNum * binWidth + self.min):
                self.indexOfMean = binNum

        #Make histogram non-ragged
        nonRagged = []
        for row in horzHistogram:
            fullRow = []
            for i in xrange(largestBinLenght):
                try:
                    fullRow.append(row[i])
                except:
                    fullRow.append(" ")
            nonRagged.append(fullRow)
        self.histogram = nonRagged


    def printHistogram(self):
        for r in xrange(len(self.histogram)):
            aRow = ""
            for col in self.histogram[r]:
                aRow += col
            if r == self.indexOfMean:
                aRow += "  <--average = " + str(round(self.xbar, 3))
            elif r == 0:
                aRow += "  <--min = " + str(round(self.min, 3))
            elif r == len(self.histogram) - 1:
                aRow += "  <--max = " + str(round(self.max, 3))
            print aRow
        print



##sampNumbers = [5.7,11.9,11.7,12.4,13.4,10.2,10.7,9.0,10.0,
##               9.5,11.6,8.4,18.0,7.9,5.8,6.1,7.4,7.3,6.6,8.3,
##               9.6,4.4,23.2,10.6,10.1,11.9,9.4,11.2,9.2,9.1,
##               9.1,8.6,10.7,9.5,8.2,11.1,9.5,11.5,7.4,6.7,7.3,
##               8.1,18.7,3.8,11.5,7.8,6.3,6.4,2.2,8.7,7.8,7.6,
##               8.4,3.8,15.5,16.6,6.7,4.9,10.2,9.4,18.1,5.6,8.8,
##               14.8,8.1,7.7,5.2,6.2,7.7,9.5,8.3,20.2,11.6,14.6,
##               9.5,20.7,16.8,21.4,13.1,11.3,9.4,25.0,9.8,18.5,
##               12.1,15.6,23.4,20.2,9.9,15.8,12.5,7.3,15.6,14.0,
##               14.2,13.7,10.3]
##
##sampNumbers2 = [1000,1210,950,1078,1016,1125,1305,1310,950,975,
##                1395,1065,970,1020,1090,1290,1200,1120,1045,1110,
##                1310,1025,1060,1300,1269,979,1390,930,925,1192,890,
##                1005,915,1015,1280,995,1315,1050,1040,1040,1150,
##                1030,1000,1110,1220,885,1030,1057,1020,1010,
##                970,1050,1110,1055,1115,1435,1040,930,1425,1120,1175,
##                1230,1305,1140,1025,1060,995,1045,985,1075]
##
##sample = Sample(numbers = sampNumbers,
##                xbar = None,
##                sigma = None,
##                s = None,
##                n = len(sampNumbers),
##                nullHyp = 12,
##                confidenceLevel = Sample.Z_CLEVEL_95,
##                isRandom = True,
##                isNormal = True,
##                isIndependant = True,
##                measurementName = "age")
