from selenium import webdriver
from pyvirtualdisplay import Display

driver = webdriver.Chrome()
display = Display(visible=0, size=(800, 800))  
display.start()
driver.get("http://www.baidu.com")
driver.quit()
driver.stop()
# keyword = driver.find_element_by_id("kw")
# keyword.send_keys("larrywoo")
# search_btn = driver.find_element_by_id("su")
# search_btn.click()
# xinwen = driver.find_elements_by_xpath("//*[@id='s_tab']/a[1]")
# xinwen.click()
