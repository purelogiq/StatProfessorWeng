# StatProfessorWeng
Simple text based statistics in python

Application:	NORM-FERENCE
Creator:	imadueme@andrew.cmu.edu
Class:		15-112E


This program is console based. It walks the user through statistical calculations
just like a professor would.Run using Python 2.6 or 2.7.

It is able to:
	create a histogram of the numbers (if a list of numbers was given instead of summary statistics)
	calculate summary statistics of the sample
	confidence interval of sample mean
	perform a hypothesis test based on the confidence interval	
	save the histogram and statistics to file

***THERE IS SAMPLE INPUT IN THE SAMPLES FOLDER***
	This is stuff you can type to test it realistcally.
***IF RUN ON A BETTER PYTHON CONSOLE (RATHER THAN JUST UNIX TERMINAL)
	(SUCH AS IDLE)
	THE WORDS WILL APPEAR 1 AT A TIME, RATHER THAN JUST BY LINE,
	I HIGHLY RECOMMEND IT, IT LOOKS MUCH MORE FLUID AND NICE.
	IF YOU WANT TO DO THIS ALSO OPEN THE PROF MODULE, SCROLL
	DOWN SOME AND CHANGE speech_delay to about 0.4***
*In the second input dialog, type talk faster to increase the dialog speed.
*When saving a report, I recommend saving it into the samples folder to keep organized. (Enter samples/filename.txt)

MODULE OVERVIEW:

norm_ference_main:
	This is the main application. This is what controls the flow of dialog and input
	and connects the other modules together to form the final application.

prof:
	The static Prof class is responsible for showing dialog.

sample:
	The Sample class calculates and stores data based on what it was given.
	It is what handles all the statistical aspects of this application so the other
	modules can focus on the user interface and input checking.

helper:
	This module contains helper methods. Though there are other methods, most are
	centered around making IO operations simpler with error checking based on
	the given parameters.
