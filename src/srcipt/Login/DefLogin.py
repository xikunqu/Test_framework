#coding:utf-8
'''
说明：登陆系统函数
'''
import os
from src.page.login_page import LoginPage
from utils.config import DATA_PATH,Config
from utils.file_reader import CsvReader

def login(browser):

    csv_path = os.path.join(DATA_PATH, 'login_data')
    csv = csv_path + '/login.csv'
    LoginURL = Config().get('LoginURL')

    login_page = LoginPage(browser)
    login_page.get(LoginURL)
    datas = CsvReader(csv).data
    login_page.input_username(datas[0][0])
    login_page.input_password(datas[0][1])
    login_page.click_submit()