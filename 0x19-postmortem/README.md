![alt text](https://i.kym-cdn.com/photos/images/original/001/731/700/ade.png)


# Postmortem

## Issue Summary
Around 9:00 AM to 10:00 AM, on October 7th our web page experienced a major outage on one of 
our database systems. Users reported data not being stored sucesfully, and not being able
to access said data when trying to load it from the database. Around 90% of users reported
reported this issue regarding saved database data.

## Timeline
* 8:14 AM - Reports come in through our QA Engineers on user complaints regarding data that was saved
not being loaded
* 9:00 AM - An even larger number of reporst come in, as the issue is being investigated
* 9:10 AM - Lead Software Engineers and Database Managers meet up in conference to discuss 
    the  issue and possible solutions.
* 9:20 AM - Database management systems are changed to our secondary back up system to maintian site running
* 9:25 AM - Main Database system is reset for possible solution yet does not solve issue
* 9:30 AM - Programming team sent in for possible solutions to the issue
* 9:45 AM - Team implemented hotfix after several tests where found to be successful
* 9:50 AM - Database system was returned to original main database
* 10:00 AM - Systems where back up and running with no issues.

## Root Cause and Resolution
Root cause of the issue was recent update to software which copied database data to secondary database. However 
due to issue data was only being saved to secondary database. Programming teams where able to solve the issue 
quickly with a hotfix.

## Preventive Measures

* Software updates must go through more rigourous testing and multiple programmers
should handle the code to verify execution.
* More Database monitoring will be done to ensure user data is being saved and loaded correctly
as well as detect any possible problems before they happen
* Established protocols of issue handling within teams of programers and team leads.
