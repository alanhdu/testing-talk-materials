from selenium import webdriver


driver = webdriver.Chrome()
driver.get("http://google.com")

print(driver.title)

elem = driver.find_element_by_id("lst-ib")
elem.send_keys("HELLO!")

driver.close()
