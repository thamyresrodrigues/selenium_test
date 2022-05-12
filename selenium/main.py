'''
Webdriver:
- Google chrome: chromedriver
- Firefox: geckodriver
'''

from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.common.keys import Keys

browser = webdriver.Chrome()
# open browser
browser.get('https://www.google.com/')

# find field
search_field = browser.find_element(By.XPATH, '/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input')

# write
search_field.send_keys('ibovespa')
search_field.send_keys(Keys.ENTER)

# close browser
sleep(3)
browser.quit()
