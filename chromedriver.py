
import time
from selenium import webdriver
from pyvirtualdisplay import Display

# display = Display(visible=0, size=(800, 600))
# display.start()
# driver = webdriver.Chrome('/usr/bin/chromedriver')  # Optional argument, if not specified will search path.
driver = webdriver.Firefox()
driver.get('http://www.baidu.com');
time.sleep(5) # Let the user actually see something!
search_box = driver.find_element_by_name('q')
search_box.send_keys('ChromeDriver')
search_box.submit()
time.sleep(5) # Let the user actually see something!
driver.quit()