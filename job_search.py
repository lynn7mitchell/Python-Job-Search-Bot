from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import smtplib
from email.message import EmailMessage
from login import email_to, email_from, email_from_password

email = EmailMessage()
email['from'] = 'Python job Search Bot'
email['to'] = email_to
email['subject'] = 'Python Job Search Bot'

driver = webdriver.Chrome()
url = driver.command_executor._url

driver.get("https://www.indeed.com/jobs?q=junior+developer&l=Remote&explvl=entry_level")

def my_function():
    titles = driver.find_elements_by_class_name('title')
    jobs = []


    for title in titles:
        job = title.find_element_by_tag_name('a')
        if 'junior' and 'developer' in job.text.lower():   
            jobs.append({'title': job.text, 'link': job.get_attribute('href')})
    # print(jobs)
    global email_string
    email_string = ''

    for job in jobs:
        email_string += '\n' + '\n' + job['title'] + ' ' + job['link'] 
    return email_string

my_function()

final_email_string = email_string
print(len(final_email_string))
driver.find_element_by_xpath("//*[@id='resultsCol']/nav/div/ul/li[3]/a").click()

my_function()

final_email_string += email_string
print(len(final_email_string))


email.set_content(final_email_string)

with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp:
    # start server
    smtp.ehlo()
    # ttls is encryption
    smtp.starttls()
    # dummy email
    smtp.login(email_from, email_from_password)
    smtp.send_message(email)
    print('it worked')
    
driver.close()
driver.quit()