from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver import ActionChains
import time
import pandas as pd
import getpass
# mở driver
driver = webdriver.Chrome()

# Tạo url
url = 'https://www.reddit.com/login/'

# Truy cập
driver.get(url)
time.sleep(3)

# Nhap thong tin nguoi dung
my_email = input('Please provide your email:')
my_password = getpass.getpass('Please provide your password:')

# Khởi tạo một đối tượng 'ActionChains' dùng để thực hiện chuỗi các hành động trên trình duyệt 'driver'
actionChains = ActionChains(driver)
time.sleep(1)
# Tạo vòng lập tab 5 lần để chuyển tới khung nhập email 
for i in range(5):
    actionChains.key_down(Keys.TAB).perform()
# Nhập email vào khung email
actionChains.send_keys(my_email).perform()
# Nhấn tab để xuống khung mật khẩu
actionChains.key_down(Keys.TAB).perform()
# Nhập mật khẩu vào khng mật khẩu và nhấn enter
actionChains.send_keys(my_password + Keys.ENTER).perform()
# Chờ 5s
time.sleep(5)



# Truy cap trang post bai
url2 = 'https://www.reddit.com/user/zino_ovp/submit/?type=TEXT'
driver.get(url2);
time.sleep(2)
# Dùng vòng lập tab 17 lần để tới ô nhập tiêu đề
for i in range(17):
    actionChains.key_down(Keys.TAB).perform()

# Nhập vào khung tiêu đề với nội dung là vi du post
actionChains.send_keys('Vi du post').perform()

# Tab 2 lần
actionChains.key_down(Keys.TAB)
actionChains.key_down(Keys.TAB).perform()
# Nhập nội dung bài viết
actionChains.send_keys('Le Truong Duy Khoi').perform()
# Tab 2 lần
for i in range(2):
    actionChains.key_down(Keys.TAB).perform()
    time.sleep(3)
# Nhấn enter để đăng bài
actionChains.send_keys(Keys.ENTER).perform()


time.sleep(120)
driver.quit()





