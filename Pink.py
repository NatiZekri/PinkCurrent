from selenium import webdriver

import time
import re


path = "C:\\Users\\Zekri\\Documents\\GitHub\\pinl\\chromedriver.exe"
driver = webdriver.Chrome(path)

driver.get("https://www.otcmarkets.com/stock/cmgo")


search = driver.page_source
text_on_source = re.findall(r'Pink Current Information', search)

print(text_on_source)
if text_on_source == 'Pink Current Information':
    print(driver.title + 'Pink Current')

else:
    print('no good')



time.sleep(3)
driver.quit()