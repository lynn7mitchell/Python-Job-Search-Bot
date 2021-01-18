# Python Job Search Bot

This is a script I created to filter through jobs on job sites using Python, Selenium, and SMTPLIB. The job board websites have filters but even if you search for 'Junior Developer' with the skill level at 'Entry Level' you will still get Mid Level and Senior Level Positions. This script searches for the words 'Junior' and 'Developer' and put them all in a list. The list will then be emailed to my main email from a secondary email. At the moment this is set to search Indeed.com for Remote Junior Developer positions. Feel free to change the link. I plan on updating this script to also search LinkedIn, Glassdoor, and ZipRecruiter. 

## How To Use This Script

1. Clone This Repo
2. Pip install selenium
3. Create a file called 'login.py'
4. In this file set variables for email_to, email_from, and email_from_password
5. Set email_to to the email that will receive the list of jobs
6. Set email_from to the secondary email that the list will be sent from
7. Set email_from_password to the password for the secondary email that the list will be sent from
8. Run py -3 job_search.py


