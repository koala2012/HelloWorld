from selenium import webdriver

driver = webdriver.Chrome()
driver.get("http://www.baidu.com")
keyword = driver.find_element_by_id("kw")
keyword.send_keys("larrywoo")
search_btn = driver.find_element_by_id("su")
search_btn.click()
xinwen = driver.find_elements_by_xpath("//*[@id='s_tab']/a[1]")
xinwen.click()
