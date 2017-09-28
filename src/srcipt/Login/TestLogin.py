#coding:utf-8
'''
说明：登录页测试用例
'''
import time,os
import unittest
from selenium import webdriver
from utils.config import Config,DRIVER_PATH,DATA_PATH,REPORT_PATH
from utils.file_reader import CsvReader
import HTMLTestRunner
from utils.mail import Email
from src.page.login_page import LoginPage

class TestLogin(unittest.TestCase):

    LoginURL =Config().get('LoginURL')
    csv_path = os.path.join(DATA_PATH, 'login_data')
    csv = csv_path + '/login.csv'

    def setUp(self):
        self.browser=webdriver.Firefox()
        self.login_page = LoginPage(self.browser)
    def tearDown(self):
        self.browser.quit()

    def test_login(self):
        self.login_page.get(self.LoginURL)
        datas=CsvReader(self.csv).getlist
        n=len(datas)
        print("用户数据为%d组"%n)
        for data in datas:
            try:
                self.login_page.input_username(data[0])
                self.login_page.input_password(data[1])
                self.login_page.click_submit()
                self.loginidtext = "当前登录工号 :" + " " + data[0]
                self.assertEqual(self.login_page.show_loginid(),self.loginidtext)
                print("%s登陆成功" % data[0])
            except AssertionError:
                print("%s无法正常登陆"%data[0])
                self.login_page.save_screen_shot("login_error")

if __name__=="__main__":
    #__name__=="__main__"时不能生成测试报告
    #__name__=="TestLogin"使用自己的目录时可以生成测试报告
    suite=unittest.TestSuite()
    suite.addTest(TestLogin("test_login"))
    filename=REPORT_PATH + '\\testlogin.html'
    with open(filename,'wb') as fp:
        runner=HTMLTestRunner.HTMLTestRunner(stream=fp,title='测试报告',description='用例执行详情')
        runner.run(suite)
    '''
    e = Email(title='登陆系统测试报告',
              message='这是今天的测试报告，请查收！',
              receiver='123456@qq.com',
              server='...',
              sender='...',
              password='...',
              path=filename
              )
    e.send()
    '''
