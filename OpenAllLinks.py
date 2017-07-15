import webbrowser, sys
from selenium import webdriver

browserObj = webdriver.Firefox() #TODO: need to input the path for firefox driver.
browserObj.get("https://designpsych.in")
elem = browserObj.find_elements_by_tag_name('a')
for curr in elem:
    href = curr.get_attribute('href')
    browserObj.get(href)



