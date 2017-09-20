#coding:utf-8
'''
说明：登陆脚本
'''

from selenium import webdriver
from selenium.webdriver.common.by import By
from src.public.highlightElement import highlight
import time,os
from utils.config import Config,DATA_PATH
from utils.file_reader import CsvReader

LoginURL =Config().get('LoginURL')
csv_path=os.path.join(DATA_PATH,'login_data')
csv=csv_path+'/login.csv'
datas = CsvReader(csv).data
#base_path=os.path.dirname(os.path.abspath(__file__))+'\..'
#driver_path=os.path.abspath(base_path+'\drivers\chromedriver.exe')


loc_name=(By.ID,"username")
loc_password=(By.ID,"password")
loc_loginbutton=(By.XPATH,".//*[@id='loginInfo']/button")

browser=webdriver.Firefox()
browser.implicitly_wait(10)
browser.get(LoginURL)
browser.maximize_window()
#time.sleep(1)

#输入用户名
username=browser.find_element(*loc_name)
highlight(username)
username.clear()
username.send_keys(datas[0][0])

#输入密码
password=browser.find_element(*loc_password)
highlight(password)
password.clear()
password.send_keys(datas[0][1])

#点击登录按钮
loginbutton=browser.find_element(*loc_loginbutton)
highlight(loginbutton)
loginbutton.click()

time.sleep(1)
browser.quit()
