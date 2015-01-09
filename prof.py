#------------------------------------------------------------------------------
# Author:      Israel Madueme (imadueme@andrew.cmu.edu)
# Created:     08/05/2012
# Class:       15-112E Summer
#
# Controls dialog for Professor Lawrance Weng.
#------------------------------------------------------------------------------
from threading import Timer
import helper

class Prof:
    """Static class to control the AI dialog."""

    @staticmethod
    def speak(face, text):
        speech = [face] + text.split(" ")
        speech = helper.removeEmptyItems(speech)
        Prof.talk(speech)


    @staticmethod
    def talk(words):
        """Helper function to print a list of words 1 at a time.
        Returns when all words have been printed.
        """
        Prof.still_talking = True
        firstWordDelay = 0.3
        timer = Timer(firstWordDelay, Prof.say, args=[words])
        timer.start()
        while Prof.still_talking:
            pass


    @staticmethod
    def say(words):
        """Prints the first word in the list words then recursivly prints the
        next words after speech_delay seconds.
        """
        print words.pop(0),
        if len(words) > 0:
            timer = Timer(Prof.speech_delay, Prof.say, args=[words])
            timer.start()
        else:
            Prof.still_talking = False


    @staticmethod
    def report(text, values, face = "normal"):
        speech = text.format(values[0], values[1], values[2], values[3])
        if face == "normal": face = Prof.FACE_NORMAL
        Prof.speak(face, speech)



    #-------Class variables-------------
    speech_delay = 0.3
    still_talking = False


    #-------Faces----------------------
    FACE_NORMAL = "[0]_[0]"
    FACE_INVALID_INPUT = "[>]_[>] "
    FACE_HMM = "[-]_[-]"
    FACE_MHMM = "[~]_[~]"
    FACE_WOAH = "[.]________[.]"
    FACE_CANT_BE_RIGHT = "[=]_[=]"
    FACE_HOW_TO_DO = "[ ']~[ ']"
    FACE_OH = "[O]o[O]"
    FACE_AHA = "[!]_[!]"
    FACE_DONE = "[^]_[^]"
    FACE_SORRY = "[>]_[<]"


    #------Dialog----------------------
    TEXT_NORMFERENCE =\
        """NORM-FERENCE:
        STATISTICAL INFERENCE AND EXPLORATORY DATA ANAYLSIS
        OF ONE QUANTITATIVE SAMPLE MEAN NORMAL DISTRIBUTIONS . . .
        FOR NORMAL PEOPLE. . .

        """

    TEXT_INTRO =\
        """Hello, my name is Professor Lawrance Weng . . . not to be
        confused with the professor of 36-201 (Intro Stat) at CMU
        Professor Lawrence Wang. Though our name and profession
        are similar, we are entirely seperate beings and have very
        little else in common, except, perhaps, our glasses.
        Regardless, I will help you conduct EDA of one quantitative
        sample mean data and a hypothesis test using confidence
        intervals, don't worry if you do not understand what that means
        I will explain everything. Ready?

        """

    TEXT_OVERVIEW =\
        """Great! Here's the plan. We will analyze the 'sample' data
        by looking at a histogram of the values and some summary numbers,
        like averages and range. Then we will make a systematic guess
        about where the true 'population' average is. In order to do those
        things though, we'll need to get the data first. That's where you
        come in . . . are you ready to input the data?

        """

    TEXT_DATA_OR_DIS =\
        """Do you have a list of the numbers from the sample or
        do you only have some summary numbers of the sample?

        """

    TEXT_FILE_OR_MANUALLY =\
        """Do you have a file that has the values seperated by commas
        in any way? Or you want to enter the numbers here?

        """

    TEXT_GET_XBAR =\
        """Since you do not have the list of numbers we won't be able to
        do extra things like create a histogram or calcalute the median. But
        we can still analyize the data and test our hypothesis. To do that
        you must know the average of the sample data (x-bar).

        """

    TEXT_GET_N =\
        """Please enter the sample size (n). It is the number of
        measurments that were sampled.

        """

    TEXT_GET_SIGMA =\
        """If you know the population standard deviation (the regular distance
        from the average of the population) then it will make our calculations
        much more accurate, if you don't it is ok, we can still estimate it.

        """

    TEXT_GET_S =\
        """Since you do not know the population standard deviation and you
        didn't enter a list of numbers, you'll need to provided the sample
        standard deviation (the regular distance from the average
        of the sample).

        """

    TEXT_GET_NULL =\
        """In order to conduct a hypothesis test, well need a . . . hypothesis.
        This is what we believe the mean in the population (not the sample!) is.
        Well will look at the sample and, through the magic of confidence
        intervals, we will test to see if your hypothesized population mean
        is likely given that we obtained a sample like what we did.

        """

    TEXT_GET_CL =\
        """Before we create this "confidence interval" we will need to first
        decide how confident we want to be that our sampling method captures the
        population mean. Higher confidence though, comes with a wider interval.

        """

    TEXT_GET_ISRANDOM=\
        """Now in order for the mathematics to work we need to know if the
        sample was collected randomly. This is to prevent bias in the data.
        If it wasn't we can still do the calculations, but we will not be
        able to generalize the results to the entire population.

        """

    TEXT_GET_ISNORMAL =\
        """Again, for the mathematics to be valid, we'll need to know if the
        "sample mean distribution" is normal. Since the sample size is less
        than 30, the only way for this to now be true is for the population
        distribution itself to be normal. By normal, I mean that most values
        are near the mean and less are far from the mean, e.g. bell shaped.

        """

    TEXT_GET_ISINDEPENDANT =\
        """The last thing we need to validate is whether or not the
        measurements in the sample were independant of each other. This is to
        ensure that the probability of sampling 1 value does not affect the
        probability of sampling another value. This condition can be met if
        the sample was collected with replacement (so there are the same things
        to sample each time) or if the population size is much bigger than
        the sample size (so sampling 1 thing doesn't really affect the
        probability of sampling another thing appreciably).

        """

    TEXT_GET_LABEL =\
        """Now I just need you to tell me what the data is measureing. For
        example, is it measureing "adult weight" or "salary of teachers", etc.

        """

    TEXT_CALCULATING =\
        """Ok! Now I'll calculate the statistics.

        """

    TEXT_SAVE =\
        """You can scroll up to view the data again. You can also save it.
	Do you want to save the report?

        """

    TEXT_END =\
        """Were done! I hope this has provided some useful insight!

        """

    TEXT_HMMM =\
        """H m m m . . . .

        """

    TEXT_MHMMM =\
        """M m m h m m m . . . .

        """

    TEXT_WOAH =\
        """Woah.

        """

    TEXT_CANT_BE_RIGHT =\
        """That can't be right.

        """

    TEXT_HOW_TO_DO_THIS =\
        """How do I do this again? ?

        """

    TEXT_OOO =\
        """O o o h h right . . . I have to . . .

        """

    TEXT_AHA =\
        """AHA! ! !

        """

    TEXT_DONE =\
        """Ok I'm done with my calculations here is my report!
        Report:


        """

    REPORT_HISTOGRAM =\
        """Here is a histogram of the data, the min, average, and max are
        marked on the side. Any suspected outliers are marked with a *.


        """

    REPORT_AVERAGE =\
        """The average {0} is {1}.

        """

    REPORT_DEVIATION =\
        """About two-thirds of the measurements are within {0} from the
        average {1} of {2}.

        """

    REPORT_MEDIAN_AND_RANGE =\
        """The median {3} (middle value) is {0}.
        The middle 50% of the sample {3} data is between {1} and {2}.

        """

    REPORT_INTERVAL=\
        """I am {2}% confident that the average population {3} is
        in the interval from {0} to {1}.

        """

    REPORT_HYP_ABOVE =\
        """Sorry! Your hypothesis {0} for the population
        average {2} was too high based on our interval.
        It is greater than {1}, the upper bound of the interval.
        Because of this, I would reject that hypothesis.

        """

    REPORT_HYP_BELOW=\
        """Sorry! Your hypothesis {0} for the population
        average {2} was too low based on our interval.
        It is less than {1} the lower bound of the interval.
        Because of this, I would reject that hypothesis.

        """

    REPORT_HYP_OK =\
        """Based on our interval, your hypothesis {2} for the population
        average {3} is valid. I have no reason to reject it because it
        is between {0} and {1}.

        """

    REPORT_NOT_RANDOM =\
        """Unfortunately, since the sample was not random, you cannot
        generalize the results to the entire population. This is because the
        sample may contain bias due to the non-random selection. Sorry...

        """

    REPORT_NOT_NORMAL =\
        """Unfortunately, since the population isn't normal and the sample size
        was less than 30, it is possible that these calculations were not very
        precise. Because of this, I recommend you only use these calculations
        as rough estimates, the correct confidence interval could be wider.

        """

    REPORT_NOT_INDEPENDANT =\
        """Unfortunately, since the measurments in the sample were not
        collected independantly, I cannot gaureentee that our mathematics
        will represent the true population. Reconsider your sampling method
        before making any conclusions.

        """

    REPORT_GOOD_TEST =\
        """Nice! All the assumtions for a good experiment were met!

        """