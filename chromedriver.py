
import time
from selenium import webdriver
from pyvirtualdisplay import Display
from xvfbwrapper import Xvfb

# display = Display(visible=0, size=(800, 600))
# xf = Xvfb()  #  xf = Xvfb(1920, 1080) - will create virtual display with 1920x1080 size
# xf.start()
# display.start()
driver = webdriver.Chrome('/usr/bin/chromedriver')  # Optional argument, if not specified will search path.
# driver = webdriver.Firefox()
driver.get('http://www.baidu.com');
time.sleep(5) # Let the user actually see something!
search_box = driver.find_element_by_name('wd')
search_box.send_keys('ChromeDriver')
search_box.submit()
time.sleep(5) # Let the user actually see something!
driver.quit()