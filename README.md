# StatProfessorWeng  
Simple text based statistics in python  

Application:	NORM-FERENCE  
Creator:	imadueme@andrew.cmu.edu  
Class:		15-112E  
(Project from a entry level course)  

This program is console based. It walks the user through very simple statistical calculations just like a professor would.  
Run using Python 2.6 or 2.7.  
There is sample input in the samples folder  

MODULE OVERVIEW:  

norm_ference_main:  
  This is the main application. This is what controls the flow of dialog and input and connects the other modules together to form the final application.  

prof:  
  The static Prof class is responsible for showing dialog.  

sample:  
  The Sample class calculates and stores data based on what it was given. It is what handles all the statistical aspects of this application so the other modules can focus on the user interface and input checking.  

helper:
	This module contains helper methods. Though there are other methods, most are centered around making IO operations simpler with error checking based on the given parameters.  