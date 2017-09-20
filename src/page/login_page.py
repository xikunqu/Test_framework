#coding:utf-8
'''
说明：登录页
'''

from selenium.webdriver.common.by import By
from src.public.basepage import BasePage
from src.public.highlightElement import highlight

class LoginPage(BasePage):

    element_status="元素不存在"
    loc_loginicon=(By.XPATH,".//*[@id='loginInfo']/h3")
    loc_name = (By.ID, "username")
    loc_password = (By.ID, "password")
    loc_loginbutton = (By.XPATH, ".//*[@id='loginInfo']/button")
    loc_nameerror = (By.ID, "loginIdShowMsg")
    loc_passworderror=(By.ID,"passWordError")
    loc_loginid=(By.PARTIAL_LINK_TEXT,"当前登录工号 :")

    # 操作
    # 通过继承覆盖（Overriding）方法，如果子类和父类的方法名相投，优先用子类自己的方法

    #找到登陆标识
    def find_loginicon(self):
        if self.is_element_exist(*self.loc_loginicon):
            return self.find_element(*self.loc_loginicon).text
        else:
            return self.element_status

    # 输入用户名:调用send_keys对象，输入用户名
    def input_username(self, username):
        name=self.find_element(*self.loc_name)
        highlight(name)
        name.clear()
        name.send_keys(username)

    # 输入密码：调用send_keys对象，输入密码
    def input_password(self, password):
        pwd=self.find_element(*self.loc_password)
        highlight(pwd)
        pwd.clear()
        pwd.send_keys(password)

    # 点击登录：调用click（）对象，点击登录
    def click_submit(self):
        login_button=self.find_element(*self.loc_loginbutton)
        highlight(login_button)
        login_button.click()

    # 用户名错误提示框
    def show_nameerror(self):
        try:
            nameerror = self.find_element(*self.loc_nameerror)
            highlight(nameerror)
            return nameerror.text
        except:
            return self.element_status

    # 密码错误提示框
    def show_passworderror(self):
        try:
            passworderror = self.find_element(*self.loc_passworderror)
            highlight(passworderror)
            return passworderror.text
        except:
            return self.element_status


    # 查找登录成功页面中的登陆工号
    def show_loginid(self):
        if self.is_element_exist(*self.loc_loginid):
            return self.find_element(*self.loc_loginid).text
        else:
            return self.element_status


