from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()

driver.set_page_load_timeout(10)
driver.get("http://127.0.0.1:8000/cattery/cat/1/")


def set_field(id, text):
    driver.execute_script("document.getElementById('%s').value='%s'" % (id, text))


# driver.find_element_by_id("cat_name_input").send_keys("Bageera")
name = "Bageera%s" % time.time()
set_field("cat_name_input", name)
driver.find_element_by_id("btnK").send_keys(Keys.ENTER)
time.sleep(5)

assert name == driver.find_element_by_id("cat_name").text
driver.quit()
