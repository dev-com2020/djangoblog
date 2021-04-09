import time

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager


driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get(url='http://127.0.0.1:8000/admin')

def element_is_clickable():
    driver.find_element_by_xpath('//*[@id="id_username"]').send_keys("razor")


    #time.sleep(3)
    #driver.find_element_by_xpath('/html/body/div[1]/nav/div/a[2]').click()
    print("OK!")

element_is_clickable()

