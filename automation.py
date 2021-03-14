from selenium import webdriver
import time

chrome_browser = webdriver.Chrome('./chromedriver')

#chrome_browser.maximize_window()
chrome_browser.get('https://www.seleniumeasy.com/test/basic-first-form-demo.html')

assert 'Selenium Easy Demo' in chrome_browser.title

show_message_button = chrome_browser.find_element_by_class_name('btn-default')
pop_up_button = chrome_browser.find_element_by_class_name('at-cm-no-button')

assert 'Show Message' in chrome_browser.page_source

time.sleep(5)

pop_up_button.click()

user_message = chrome_browser.find_element_by_id('user-message')
user_message.clear()
user_message.send_keys('Welcome!! How are you??')

show_message_button.click()

output_message = chrome_browser.find_element_by_id('display')

assert 'Welcome!! How are you??' in output_message.text

##############################################################################################################
# Second Form
chrome_browser.execute_script("window.scrollTo(0, 5)")

sum1 = chrome_browser.find_element_by_id('sum1')
sum2 = chrome_browser.find_element_by_id('sum2')
sum1.clear(), sum2.clear()
sum1.send_keys(1)
sum2.send_keys(2)

get_total_button = chrome_browser.find_element_by_id('gettotal').find_element_by_class_name('btn-default')
get_total_button.click()

time.sleep(10)
chrome_browser.quit()
